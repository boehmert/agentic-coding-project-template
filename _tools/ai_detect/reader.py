"""
Text-Extraktor für AI-Detektor
================================
Liest .txt, .md und .docx Dateien und liefert den Rohtext zurück.

Verwendung:
    from _tools.ai_detect.reader import TextReader

    reader = TextReader()
    text = reader.read(Path("inbox/ai-detect/sample.docx"))
"""

import re
from pathlib import Path
from typing import Optional


class TextReader:
    """
    Liest verschiedene Textformate und gibt den Rohtext zurück.

    Unterstützte Formate:
        .txt  — direktes Lesen (UTF-8)
        .md   — Markdown-Syntax bereinigt (Links, Codeblöcke, HTML-Tags entfernt)
        .docx — via python-docx (Absätze extrahiert)
    """

    SUPPORTED_SUFFIXES = {".txt", ".md", ".docx"}
    DEFAULT_ENCODING = "utf-8"

    # ── Öffentliche API ───────────────────────────────────────────────────────

    def read(self, path: Path) -> str:
        """
        Liest eine Datei und gibt den bereinigten Rohtext zurück.

        Args:
            path: Pfad zur Datei (.txt, .md oder .docx).

        Returns:
            Den extrahierten Text als String.

        Raises:
            ValueError: Wenn das Dateiformat nicht unterstützt wird.
            FileNotFoundError: Wenn die Datei nicht existiert.
            RuntimeError: Wenn die Datei nicht gelesen werden kann.
        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Datei nicht gefunden: {path}")

        suffix = path.suffix.lower()
        if suffix not in self.SUPPORTED_SUFFIXES:
            raise ValueError(
                f"Nicht unterstütztes Format: '{suffix}'. "
                f"Erlaubt: {', '.join(sorted(self.SUPPORTED_SUFFIXES))}"
            )

        try:
            if suffix == ".txt":
                return self._read_txt(path)
            elif suffix == ".md":
                return self._read_md(path)
            elif suffix == ".docx":
                return self._read_docx(path)
        except (OSError, UnicodeDecodeError) as exc:
            raise RuntimeError(f"Fehler beim Lesen von '{path}': {exc}") from exc

        return ""

    # ── Interne Leser ─────────────────────────────────────────────────────────

    def _read_txt(self, path: Path) -> str:
        """Liest eine einfache Textdatei (UTF-8, Fallback auf latin-1)."""
        try:
            return path.read_text(encoding=self.DEFAULT_ENCODING)
        except UnicodeDecodeError:
            return path.read_text(encoding="latin-1")

    def _read_md(self, path: Path) -> str:
        """
        Liest eine Markdown-Datei und bereinigt die Syntax,
        sodass nur der Prosa-Text für die Analyse bleibt.
        """
        try:
            text = path.read_text(encoding=self.DEFAULT_ENCODING)
        except UnicodeDecodeError:
            text = path.read_text(encoding="latin-1")

        return self._strip_markdown(text)

    def _read_docx(self, path: Path) -> str:
        """
        Liest eine Word-Datei (.docx) via python-docx.
        Extrahiert alle Absatz-Texte und verbindet sie mit Zeilenumbrüchen.
        """
        try:
            import docx  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "python-docx ist nicht installiert. "
                "Bitte ausführen: pip install python-docx"
            ) from exc

        doc = docx.Document(str(path))
        paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n".join(paragraphs)

    # ── Markdown-Bereinigung ──────────────────────────────────────────────────

    @staticmethod
    def _strip_markdown(text: str) -> str:
        """
        Entfernt Markdown-Syntax und gibt lesbaren Prosa-Text zurück.
        Belässt Aufzählungszeichen (- / *) als strukturelles Signal für den Detektor.
        """
        # Fenced Code Blocks entfernen (```...```)
        text = re.sub(r"```[\s\S]*?```", "", text)
        # Inline Code entfernen
        text = re.sub(r"`[^`]+`", "", text)
        # HTML-Tags entfernen
        text = re.sub(r"<[^>]+>", "", text)
        # Markdown-Links: [text](url) → text
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        # Bilder: ![alt](url) → alt
        text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
        # Überschriften: # Titel → Titel
        text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
        # Fett/Kursiv: **text** / *text* / __text__ / _text_ → text
        text = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text)
        text = re.sub(r"_{1,3}([^_]+)_{1,3}", r"\1", text)
        # Horizontale Linien entfernen
        text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
        # Mehrfache Leerzeilen komprimieren
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()

    # ── Hilfsmethoden ─────────────────────────────────────────────────────────

    @classmethod
    def is_supported(cls, path: Path) -> bool:
        """Gibt True zurück, wenn die Datei vom Reader unterstützt wird."""
        return Path(path).suffix.lower() in cls.SUPPORTED_SUFFIXES

    @classmethod
    def collect_files(cls, directory: Path) -> list[Path]:
        """
        Gibt alle unterstützten Dateien in einem Verzeichnis zurück (rekursiv).

        Args:
            directory: Verzeichnis, in dem gesucht wird.

        Returns:
            Sortierte Liste der gefundenen Dateipfade.
        """
        if not directory.is_dir():
            return []

        files = []
        for suffix in cls.SUPPORTED_SUFFIXES:
            files.extend(directory.rglob(f"*{suffix}"))

        return sorted(files)

