"""
Fingerprint-Datenbank für AI-Text-Detektor
===========================================
Strukturierte Phrase-Patterns und Strukturindikatoren je Modell und Sprache.

Jeder Eintrag besteht aus:
  - phrases: Liste von Regex-Patterns (case-insensitive gematcht)
  - weight:  Gewichtung dieses Musters im Scoring (1.0 = Standard)

Sprachen: "en" (Englisch), "de" (Deutsch)
Modelle:  claude, chatgpt, copilot, gemini, generic_ai
"""

from typing import Dict, List, Tuple

# ── Typen ────────────────────────────────────────────────────────────────────

# (pattern, weight)
PhraseEntry = Tuple[str, float]

# Struktur: { modell: { sprache: [ (pattern, weight), ... ] } }
FingerprintDB = Dict[str, Dict[str, List[PhraseEntry]]]


# ── Fingerprint-Datenbank ────────────────────────────────────────────────────

FINGERPRINTS: FingerprintDB = {

    # ── Claude (Anthropic) ───────────────────────────────────────────────────
    "claude": {
        "en": [
            (r"\bcertainly\b", 2.0),
            (r"\bi['']d be happy to\b", 2.0),
            (r"\bnuanced\b", 1.5),
            (r"\bstraightforward\b", 1.5),
            (r"\bcomprehensive overview\b", 2.0),
            (r"\bit['']s important to note\b", 1.5),
            (r"\bit['']s worth noting\b", 1.2),
            (r"\bI['']ll do my best\b", 1.5),
            (r"\blet me (break|walk|explain)\b", 1.5),
            (r"\bhere['']s a (breakdown|summary|overview)\b", 1.5),
            (r"\bI should (mention|point out|clarify)\b", 1.5),
            (r"\bthis is a (complex|nuanced|fascinating)\b", 1.5),
            (r"\ba few (key|important|crucial) (points|things|aspects)\b", 1.2),
            (r"\bwhat['']s particularly (interesting|notable|important)\b", 1.5),
            (r"\bI appreciate (your|the) (question|context|perspective)\b", 2.0),
            (r"\bI['']m Claude\b", 3.0),
        ],
        "de": [
            (r"\bnatürlich\b", 1.5),
            (r"\bgerne erkläre ich\b", 2.0),
            (r"\bumfassend\b", 1.2),
            (r"\bes ist wichtig (zu beachten|anzumerken|hervorzuheben)\b", 1.5),
            (r"\bich helfe (dir|Ihnen) gerne\b", 2.0),
            (r"\blass(en Sie) mich (erklären|klarstellen)\b", 1.5),
            (r"\bich bin Claude\b", 3.0),
            (r"\bim Folgenden (erkläre|beschreibe|zeige)\b", 1.2),
            (r"\bein (paar|einige) (wichtige|zentrale|wesentliche) (Punkte|Aspekte)\b", 1.2),
            (r"\bwas (besonders|vor allem) (interessant|wichtig|erwähnenswert) (ist|erscheint)\b", 1.5),
        ],
    },

    # ── ChatGPT / GPT-4 (OpenAI) ─────────────────────────────────────────────
    "chatgpt": {
        "en": [
            (r"\bdelve into\b", 2.5),
            (r"\bdive into\b", 1.5),
            (r"\bas of my (last |knowledge )?update\b", 2.5),
            (r"\bin conclusion\b", 1.5),
            (r"\bIn summary\b", 1.2),
            (r"\bmy training data\b", 2.5),
            (r"\bI don['']t have (access|the ability|real.time)\b", 2.0),
            (r"\bcurrently,? I (can['']t|cannot|am unable to)\b", 1.5),
            (r"\bI['']m an AI (language model|assistant|tool)\b", 3.0),
            (r"\bI['']m ChatGPT\b", 3.0),
            (r"\bAbsolutely[!,]?\b", 2.0),
            (r"\bGreat (question|point|choice)[!,]?\b", 2.0),
            (r"\bOf course[!,]?\b", 1.5),
            (r"\bSure[!,]? (here|let me|I can)\b", 1.5),
            (r"\bHere['']s (a|an|the) (step.by.step|comprehensive|detailed|breakdown)\b", 1.5),
            (r"\bLet['']s (break this down|explore|dive)\b", 1.5),
        ],
        "de": [
            (r"\btauchen wir (ein|tiefer)\b", 2.0),
            (r"\bes ist erwähnenswert\b", 1.5),
            (r"\bzusammenfassend lässt sich sagen\b", 2.0),
            (r"\bnach meinem (letzten |aktuellen )?Trainingsstand\b", 2.5),
            (r"\bich bin ein KI.?(Sprachmodell|Assistent)\b", 3.0),
            (r"\bich bin ChatGPT\b", 3.0),
            (r"\bAbsolut[!,]?\b", 1.5),
            (r"\bNatürlich[!,]? (hier|lass|ich)\b", 1.5),
            (r"\bHier ist (eine? )?(schrittweise|detaillierte|umfassende)\b", 1.5),
            (r"\bgerne[,!]?\b", 1.2),
        ],
    },

    # ── GitHub Copilot (Microsoft/OpenAI) ────────────────────────────────────
    "copilot": {
        "en": [
            (r"\blet me walk you through\b", 2.5),
            (r"\bhere['']s (the|a) (code|implementation|solution|snippet)\b", 2.0),
            (r"\byou can (use|try|implement|replace)\b", 1.2),
            (r"\bthis (function|method|code) (will|does|returns)\b", 1.5),
            (r"\bmake sure (to|that)\b", 1.2),
            (r"\bdon['']t forget to\b", 1.5),
            (r"\bI['']ll (generate|provide|create|write) (a|the) (function|code|snippet|implementation)\b", 2.0),
            (r"\bI['']m GitHub Copilot\b", 3.0),
            (r"\bI['']m (an AI|your) (coding|programming) (assistant|companion|partner)\b", 2.5),
        ],
        "de": [
            (r"\blass mich (dich|Sie) (durchführen|erklären|zeigen)\b", 2.0),
            (r"\bhier ist (der|ein) (Code|die Implementierung|die Lösung)\b", 2.0),
            (r"\bdu kannst (verwenden|versuchen|ersetzen)\b", 1.2),
            (r"\bvergiss nicht\b", 1.2),
            (r"\bich bin GitHub Copilot\b", 3.0),
        ],
    },

    # ── Gemini (Google DeepMind) ──────────────────────────────────────────────
    "gemini": {
        "en": [
            (r"\bI understand (your|the) (question|request|point)\b", 2.0),
            (r"\bhere['']s a breakdown\b", 2.0),
            (r"\bhere['']s what I (found|know|can tell you)\b", 1.5),
            (r"\bas a (large |multimodal )?language model\b", 2.0),
            (r"\bI['']m Gemini\b", 3.0),
            (r"\bI['']m Bard\b", 2.5),
            (r"\bthis is a (multi.part|complex) (question|topic|task)\b", 1.5),
            (r"\bTo answer (your|this)\b", 1.2),
            (r"\bregarding (your (question|inquiry|request))\b", 1.5),
            (r"\bI (can|will) provide (a|you with)( a)? (comprehensive|detailed|thorough)\b", 1.5),
        ],
        "de": [
            (r"\bich verstehe (deine|Ihre) (Frage|Anfrage|Anforderung)\b", 2.0),
            (r"\bhier ist eine (Übersicht|Aufschlüsselung|Zusammenfassung)\b", 2.0),
            (r"\bals (großes |multimodales )?(Sprachmodell|KI.Modell)\b", 2.0),
            (r"\bich bin Gemini\b", 3.0),
            (r"\bich bin Bard\b", 2.5),
            (r"\bzu (Ihrer|deiner) (Frage|Anfrage)\b", 1.2),
        ],
    },

    # ── Allgemeine KI-Indikatoren (modellunabhängig) ──────────────────────────
    "generic_ai": {
        "en": [
            (r"\bfurthermore\b", 1.2),
            (r"\bmoreover\b", 1.2),
            (r"\badditionally\b", 1.0),
            (r"\bin addition\b", 1.0),
            (r"\bnotably\b", 1.2),
            (r"\bit is (essential|crucial|vital|imperative) (to|that)\b", 1.5),
            (r"\bplease (note|be aware|keep in mind)\b", 1.2),
            (r"\bultimately\b", 1.0),
            (r"\bbroadly speaking\b", 1.5),
            (r"\bmore (specifically|importantly|notably)\b", 1.2),
            (r"\b(key|important|main) (takeaway|point|consideration)s?\b", 1.5),
            (r"\bin the context of\b", 1.0),
            (r"\bfeel free to\b", 1.5),
            (r"\bhope (this helps|that helps|that answers)\b", 1.5),
            (r"\bdon['']t hesitate to (ask|reach out)\b", 2.0),
        ],
        "de": [
            (r"\bdarüber hinaus\b", 1.2),
            (r"\baußerdem\b", 1.0),
            (r"\bzusätzlich\b", 1.0),
            (r"\binsbesondere\b", 1.0),
            (r"\bes ist (wesentlich|entscheidend|unerlässlich)\b", 1.5),
            (r"\bbitte (beachten Sie|beachte|beachten)\b", 1.2),
            (r"\bletzten Endes\b", 1.0),
            (r"\bim (Kontext|Rahmen) (von|der)\b", 1.0),
            (r"\bfühl dich frei\b", 1.5),
            (r"\bich hoffe[,]? (das|dass) (hilft|beantwortet)\b", 1.5),
            (r"\bzögere nicht(, (zu fragen|mich zu kontaktieren))?\b", 2.0),
            (r"\bass zusammenfassend\b", 1.2),
            (r"\bim Großen und Ganzen\b", 1.2),
        ],
    },
}


# ── Strukturmuster-Schwellenwerte ─────────────────────────────────────────────

STRUCTURE_THRESHOLDS = {
    # Durchschnittliche Satzlänge (Wörter) — KI neigt zu längeren Sätzen
    "avg_sentence_length_high": 22,   # > 22 → leichter KI-Hinweis
    "avg_sentence_length_very_high": 30,  # > 30 → starker KI-Hinweis

    # Anteil von Aufzählungszeichen (- / * / •) an allen Zeilen
    "bullet_ratio_high": 0.20,        # > 20 % → leichter KI-Hinweis
    "bullet_ratio_very_high": 0.35,   # > 35 % → starker KI-Hinweis

    # Übergangswörter-Dichte (pro 100 Wörter)
    "transition_density_high": 3.0,   # > 3 → leichter KI-Hinweis
    "transition_density_very_high": 6.0,  # > 6 → starker KI-Hinweis

    # Lexikalische Diversität (unique_words / total_words)
    # KI-Texte tendieren zu etwas niedrigerer Diversität als Fachtexte
    "lexical_diversity_low": 0.45,    # < 45 % → leichter KI-Hinweis
}


# ── Übergangswörter für Strukturanalyse ──────────────────────────────────────

TRANSITION_WORDS = {
    "en": [
        "furthermore", "moreover", "additionally", "however", "therefore",
        "consequently", "nevertheless", "nonetheless", "subsequently",
        "in conclusion", "in summary", "to summarize", "in addition",
        "on the other hand", "as a result", "for example", "for instance",
        "in other words", "that said", "having said that",
    ],
    "de": [
        "darüber hinaus", "außerdem", "zusätzlich", "jedoch", "daher",
        "folglich", "dennoch", "nichtsdestotrotz", "anschließend",
        "zusammenfassend", "abschließend", "zusammenfassend lässt sich",
        "einerseits", "andererseits", "als ergebnis", "zum beispiel",
        "mit anderen worten", "gleichwohl", "insgesamt",
    ],
}

