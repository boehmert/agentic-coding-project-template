"""
AI-Text-Detektor – Analyse-Engine
==================================
Analysiert Texte auf stylometrische Fingerprints und erkennt,
welches KI-Modell (Claude, ChatGPT, Copilot, Gemini) den Text wahrscheinlich
erzeugt hat.

Verwendung:
    from _tools.ai_detect.detector import AITextDetector

    detector = AITextDetector()
    result = detector.analyze("Certainly, I'd be happy to explain this...")
    print(result.top_model)       # "claude"
    print(result.ai_probability)  # 0.87
    print(result.evidence)        # ["[claude/en] 'certainly' (Gewicht 2.0)", ...]
"""

import re
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from _tools.ai_detect.fingerprints import (
    FINGERPRINTS,
    STRUCTURE_THRESHOLDS,
    TRANSITION_WORDS,
)


# ── Ergebnis-Datenklasse ──────────────────────────────────────────────────────

@dataclass
class DetectionResult:
    """Ergebnis der Analyse eines einzelnen Textes."""

    model_scores: Dict[str, float]   = field(default_factory=dict)
    """Normalisierter Score je Modell (0–100)."""

    top_model: str                   = ""
    """Wahrscheinlichstes Modell (z.B. 'claude', 'chatgpt', 'unknown')."""

    confidence: str                  = "niedrig"
    """Konfidenz der Zuordnung: 'hoch', 'mittel', 'niedrig'."""

    ai_probability: float            = 0.0
    """Gesamtwahrscheinlichkeit KI-generierter Text (0.0–1.0)."""

    evidence: List[str]              = field(default_factory=list)
    """Liste der gefundenen Fingerprints als lesbare Belege."""

    language: str                    = "unknown"
    """Erkannte Sprache: 'en', 'de' oder 'unknown'."""

    structure_hints: List[str]       = field(default_factory=list)
    """Strukturelle Auffälligkeiten (Satzlänge, Bullet-Ratio etc.)."""


# ── Haupt-Klasse ──────────────────────────────────────────────────────────────

class AITextDetector:
    """
    Analysiert einen Text stylometrisch auf KI-Urheberschaft.

    Alle Analysen sind rein lokal – kein API-Zugang erforderlich.

    Attribute:
        phrase_weight:     Gewichtung der Phrasen-Scores im Gesamtergebnis.
        structure_weight:  Gewichtung der Strukturanalyse im Gesamtergebnis.
        min_text_length:   Minimale Textlänge (Zeichen) für sinnvolle Analyse.
    """

    phrase_weight: float    = 0.70
    structure_weight: float = 0.30
    min_text_length: int    = 100

    # ── Öffentliche API ───────────────────────────────────────────────────────

    def analyze(self, text: str) -> DetectionResult:
        """
        Analysiert den übergebenen Text und gibt ein DetectionResult zurück.

        Args:
            text: Der zu analysierende Rohtext (beliebige Länge).

        Returns:
            DetectionResult mit Scores, Top-Modell, Konfidenz und Belegen.
        """
        result = DetectionResult()

        if not text or len(text.strip()) < self.min_text_length:
            result.confidence = "niedrig"
            result.top_model = "unknown"
            result.evidence = ["Text zu kurz für aussagekräftige Analyse."]
            return result

        lang = self._detect_language(text)
        result.language = lang

        phrase_scores, evidence = self._score_phrases(text, lang)
        structure_score, structure_hints = self._score_structure(text, lang)
        generic_score, generic_evidence = self._score_generic_ai(text, lang)

        evidence.extend(generic_evidence)
        result.evidence = evidence
        result.structure_hints = structure_hints

        result.model_scores = self._combine_scores(
            phrase_scores, structure_score, generic_score
        )

        result.top_model, result.confidence = self._determine_top_model(
            result.model_scores
        )

        result.ai_probability = self._calc_ai_probability(
            result.model_scores, generic_score, structure_score
        )

        return result

    # ── Spracherkennung ───────────────────────────────────────────────────────

    def _detect_language(self, text: str) -> str:
        """
        Heuristik: zählt typische Stopwörter beider Sprachen.
        Kein externer Dependency nötig.
        """
        text_lower = text.lower()

        de_words = [
            r"\bund\b", r"\bder\b", r"\bdie\b", r"\bdas\b", r"\bist\b",
            r"\bin\b", r"\bzu\b", r"\bvon\b", r"\bmit\b", r"\bich\b",
            r"\bsie\b", r"\bnicht\b", r"\bein\b", r"\beine\b", r"\bwird\b",
            r"\bhat\b", r"\baber\b", r"\bals\b", r"\bfür\b", r"\bauf\b",
        ]
        en_words = [
            r"\bthe\b", r"\band\b", r"\bto\b", r"\bof\b", r"\bin\b",
            r"\bis\b", r"\bit\b", r"\bfor\b", r"\bas\b", r"\bwith\b",
            r"\bthat\b", r"\bare\b", r"\bthis\b", r"\bbe\b", r"\bor\b",
            r"\bfrom\b", r"\bnot\b", r"\bcan\b", r"\byou\b", r"\bwill\b",
        ]

        de_count = sum(
            len(re.findall(pat, text_lower)) for pat in de_words
        )
        en_count = sum(
            len(re.findall(pat, text_lower)) for pat in en_words
        )

        if de_count == 0 and en_count == 0:
            return "en"
        if de_count > en_count * 1.5:
            return "de"
        if en_count > de_count * 1.5:
            return "en"

        # Tie-breaking: typische deutsche Sonderzeichen
        umlaut_count = len(re.findall(r"[äöüÄÖÜß]", text))
        return "de" if umlaut_count > 3 else "en"

    # ── Phrasen-Scoring ───────────────────────────────────────────────────────

    def _score_phrases(
        self, text: str, lang: str
    ) -> tuple[Dict[str, float], List[str]]:
        """
        Berechnet Rohscores für jedes Modell basierend auf Phrase-Matches.
        Normalisiert auf 1000 Zeichen, damit kurze und lange Texte vergleichbar sind.
        """
        text_lower = text.lower()
        factors = max(len(text) / 1000.0, 1.0)

        raw_scores: Dict[str, float] = {}
        evidence: List[str] = []

        for model, lang_map in FINGERPRINTS.items():
            if model == "generic_ai":
                continue  # separat behandelt

            score = 0.0
            patterns = lang_map.get(lang, [])
            # Fallback auf Englisch, wenn Sprache nicht vorhanden
            if not patterns and lang != "en":
                patterns = lang_map.get("en", [])

            for pattern, weight in patterns:
                matches = re.findall(pattern, text_lower, re.IGNORECASE)
                if matches:
                    hit_score = weight * len(matches)
                    score += hit_score
                    sample = matches[0]
                    evidence.append(
                        f"[{model}/{lang}] '{sample}' × {len(matches)}"
                        f" (Gewicht {weight:.1f})"
                    )

            # Normalisieren: pro 1000 Zeichen
            raw_scores[model] = score / factors

        # Auf 0–100 skalieren
        max_score = max(raw_scores.values(), default=1.0)
        if max_score > 0:
            scaled = {m: (s / max_score) * 100 for m, s in raw_scores.items()}
        else:
            scaled = {m: 0.0 for m in raw_scores}

        return scaled, evidence

    # ── Strukturanalyse ───────────────────────────────────────────────────────

    def _score_structure(
        self, text: str, lang: str
    ) -> tuple[float, List[str]]:
        """
        Bewertet strukturelle Eigenschaften des Textes.
        Gibt Score (0–100) und Liste von Hinweisen zurück.
        """
        hints: List[str] = []
        score = 0.0
        max_points = 0.0

        lines = text.splitlines()
        words = re.findall(r"\w+", text)
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 10]

        # --- Durchschnittliche Satzlänge ---
        if sentences:
            sentence_word_counts = [
                len(re.findall(r"\w+", s)) for s in sentences
            ]
            avg_len = sum(sentence_word_counts) / len(sentence_word_counts)
            max_points += 20
            thr = STRUCTURE_THRESHOLDS
            if avg_len > thr["avg_sentence_length_very_high"]:
                score += 20
                hints.append(
                    f"Sehr lange Sätze (Ø {avg_len:.1f} Wörter) — starker KI-Hinweis"
                )
            elif avg_len > thr["avg_sentence_length_high"]:
                score += 10
                hints.append(
                    f"Lange Sätze (Ø {avg_len:.1f} Wörter) — leichter KI-Hinweis"
                )

        # --- Bullet-Point-Ratio ---
        if lines:
            bullet_lines = sum(
                1 for line in lines
                if re.match(r"^\s*[-*•]\s+", line) or re.match(r"^\s*\d+\.\s+", line)
            )
            ratio = bullet_lines / len(lines)
            max_points += 20
            thr = STRUCTURE_THRESHOLDS
            if ratio > thr["bullet_ratio_very_high"]:
                score += 20
                hints.append(
                    f"Sehr hoher Aufzählungsanteil ({ratio:.0%}) — starker KI-Hinweis"
                )
            elif ratio > thr["bullet_ratio_high"]:
                score += 10
                hints.append(
                    f"Hoher Aufzählungsanteil ({ratio:.0%}) — leichter KI-Hinweis"
                )

        # --- Übergangswörter-Dichte ---
        if words:
            tw_list = TRANSITION_WORDS.get(lang, TRANSITION_WORDS["en"])
            tw_count = sum(
                text.lower().count(tw.lower()) for tw in tw_list
            )
            density = (tw_count / len(words)) * 100
            max_points += 20
            thr = STRUCTURE_THRESHOLDS
            if density > thr["transition_density_very_high"]:
                score += 20
                hints.append(
                    f"Sehr hohe Übergangswort-Dichte ({density:.1f}/100 Wörter)"
                    " — starker KI-Hinweis"
                )
            elif density > thr["transition_density_high"]:
                score += 10
                hints.append(
                    f"Erhöhte Übergangswort-Dichte ({density:.1f}/100 Wörter)"
                    " — leichter KI-Hinweis"
                )

        # --- Lexikalische Diversität ---
        if words:
            unique_ratio = len(set(w.lower() for w in words)) / len(words)
            max_points += 20
            thr = STRUCTURE_THRESHOLDS
            if unique_ratio < thr["lexical_diversity_low"]:
                score += 15
                hints.append(
                    f"Geringe lexikalische Diversität ({unique_ratio:.0%})"
                    " — leichter KI-Hinweis"
                )

        # Auf 0–100 normalisieren
        if max_points > 0:
            return (score / max_points) * 100, hints
        return 0.0, hints

    # ── Allgemeine KI-Indikatoren ─────────────────────────────────────────────

    def _score_generic_ai(
        self, text: str, lang: str
    ) -> tuple[float, List[str]]:
        """
        Bewertet allgemeine KI-typische Phrasen (modellunabhängig).
        Gibt Score (0–100) und Belege zurück.
        """
        text_lower = text.lower()
        factors = max(len(text) / 1000.0, 1.0)
        evidence: List[str] = []
        raw_score = 0.0

        patterns = FINGERPRINTS.get("generic_ai", {}).get(lang, [])
        if not patterns:
            patterns = FINGERPRINTS.get("generic_ai", {}).get("en", [])

        for pattern, weight in patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            if matches:
                raw_score += weight * len(matches)
                sample = matches[0]
                evidence.append(
                    f"[generic_ai/{lang}] '{sample}' × {len(matches)}"
                    f" (Gewicht {weight:.1f})"
                )

        # Normalisieren: sigmoid-ähnliche Kurve auf 0–100
        normalized = min((raw_score / factors) * 20, 100)
        return normalized, evidence

    # ── Score-Kombination ─────────────────────────────────────────────────────

    def _combine_scores(
        self,
        phrase_scores: Dict[str, float],
        structure_score: float,
        generic_score: float,
    ) -> Dict[str, float]:
        """
        Kombiniert Phrasen-, Struktur- und Generic-Score zu Gesamt-Scores.

        Struktur- und Generic-Score erhöhen ALLE Modell-Scores proportional,
        da sie kein einzelnes Modell begünstigen.
        """
        boost = (structure_score * self.structure_weight +
                 generic_score * 0.15)

        combined: Dict[str, float] = {}
        for model, score in phrase_scores.items():
            raw = score * self.phrase_weight + boost
            combined[model] = round(min(raw, 100.0), 2)

        return combined

    # ── Top-Modell bestimmen ──────────────────────────────────────────────────

    def _determine_top_model(
        self, scores: Dict[str, float]
    ) -> tuple[str, str]:
        """
        Bestimmt das wahrscheinlichste Modell und die Konfidenz.

        Konfidenz-Logik:
            hoch:   Top-Score > 40 UND Abstand zu Platz 2 > 20 Punkte
            mittel: Top-Score > 20 UND Abstand zu Platz 2 > 10 Punkte
            niedrig: sonst (alle Scores nah beieinander oder sehr niedrig)
        """
        if not scores or all(v == 0 for v in scores.values()):
            return "unknown", "niedrig"

        sorted_models = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_model, top_score = sorted_models[0]
        second_score = sorted_models[1][1] if len(sorted_models) > 1 else 0.0
        gap = top_score - second_score

        if top_score > 40 and gap > 20:
            confidence = "hoch"
        elif top_score > 20 and gap > 10:
            confidence = "mittel"
        else:
            confidence = "niedrig"

        return top_model, confidence

    # ── KI-Gesamtwahrscheinlichkeit ───────────────────────────────────────────

    def _calc_ai_probability(
        self,
        model_scores: Dict[str, float],
        generic_score: float,
        structure_score: float,
    ) -> float:
        """
        Berechnet eine Gesamtwahrscheinlichkeit, dass der Text KI-generiert ist.
        Wert zwischen 0.0 und 1.0.
        """
        top_score = max(model_scores.values(), default=0.0)
        combined = (
            top_score * 0.50
            + generic_score * 0.30
            + structure_score * 0.20
        )
        # Auf [0, 1] bringen
        return round(min(combined / 100.0, 1.0), 3)

