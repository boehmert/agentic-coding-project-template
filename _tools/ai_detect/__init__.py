"""
_tools.ai_detect – Stylometrischer AI-Text-Detektor
====================================================
Erkennt, ob ein Text KI-generiert ist, und ordnet ihn einem Modell zu
(Claude, ChatGPT, Copilot, Gemini) — rein lokal, kein API-Schlüssel erforderlich.

Öffentliche API:
    from _tools.ai_detect import AITextDetector, TextReader, FileResult, generate_report
"""

from _tools.ai_detect.detector import AITextDetector, DetectionResult
from _tools.ai_detect.reader import TextReader
from _tools.ai_detect.reporter import FileResult, generate_report

__all__ = [
    "AITextDetector",
    "DetectionResult",
    "TextReader",
    "FileResult",
    "generate_report",
]

