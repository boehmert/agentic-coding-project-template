---
name: document-pipeline
description: "Dokumenten-Verarbeitungs-Pipeline: Format-Konvertierung, Word/PDF/Excel/HTML/PPTX → Markdown, Excel-Bearbeitung. Aktiviert bei Dokumenten-Import, -Konvertierung oder -Verarbeitung."
metadata:
  trigger: Dokument konvertieren, Word, PDF, Excel, PPTX, HTML, Markdown-Export, Format-Erkennung
  author: Author
---

# Document Pipeline

Wissen über die Dokumenten-Verarbeitungs-Tools im Workspace. Drei Module für unterschiedliche Aufgaben.

---

## 1. Modul-Übersicht

| Modul | Pfad | Zweck |
|---|---|---|
| **converter** | `_tools/documents/converter.py` | Universal-Konverter: beliebiges Format → Markdown |
| **doc_processor** | `_tools/documents/doc_processor.py` | Word (.docx) und PDF-Verarbeitung im Detail |
| **excel_editor** | `_tools/documents/excel_editor.py` | Excel lesen, suchen, bearbeiten, exportieren |

---

## 2. Universal Converter (`converter.py`)

### Unterstützte Formate

| Format | Endung | Erkennung | Methode |
|---|---|---|---|
| Word (OOXML) | `.docx` | Magic bytes `PK` | python-docx |
| Word (HTML-Export) | `.doc` | Magic bytes `<!D` | BeautifulSoup |
| Word (OLE2 binary) | `.doc` | Magic bytes `D0 CF` | pandoc (extern) |
| PDF | `.pdf` | Magic bytes `%PDF` | pypdf |
| PowerPoint | `.pptx` | Magic bytes `PK` + Endung | python-pptx |
| Excel | `.xlsx`, `.xls` | Magic bytes `PK` + Endung | openpyxl |
| HTML | `.html`, `.htm` | Magic bytes `<ht` | BeautifulSoup |
| Text/Markdown | `.txt`, `.md` | — | Pass-through |

**Format-Erkennung:** Per Magic Bytes (erste 16 Bytes), nicht per Dateiendung. Korrekte Erkennung auch bei falsch benannten Dateien (z.B. `.doc` das eigentlich HTML ist).

### Verwendung

```python
from _tools.documents.converter import to_markdown, convert_directory
from pathlib import Path

# Einzelne Datei
out = to_markdown(Path("inbox/jira/PROJECT-1280.doc"), Path("output/context"))

# Ganzes Verzeichnis
convert_directory(Path("inbox/jira"), Path("output/context"))
```

**Input-Pfade:** Beliebig, typisch `inbox/`
**Output-Pfade:** Beliebig, typisch `output/context/` oder `output/reports/`

---

## 3. Document Processor (`doc_processor.py`)

### Funktionen

| Funktion | Zweck |
|---|---|
| `read_docx(path)` | Word-Datei → Rohtext (Absätze durch Newlines getrennt) |
| `_para_to_md(para)` | Einzelner docx-Absatz → Markdown (Headings, Text) |
| `_dedup_row(row)` | Doppelte Zellen in Tabellen bereinigen (merged cells) |
| `_kv_table_to_md(data)` | 2-Spalten Key/Value Tabelle → Markdown Definition List |

### Benötigte Pakete

```
python-docx  – Word-Dokumente
pypdf        – PDF-Dokumente
jinja2       – Template-Rendering
```

---

## 4. Excel Editor (`excel_editor.py`)

### Funktionen

| Funktion | Zweck | Beispiel |
|---|---|---|
| `open_workbook(path, sheet)` | → (Workbook, Worksheet) | `wb, ws = open_workbook("data.xlsx")` |
| `get_header_map(ws)` | Spaltenüberschriften → Index-Map | `header = get_header_map(ws)` |
| `find_rows(ws, header, fn)` | Zeilen per Filterfunktion suchen | `rows = find_rows(ws, h, lambda r: r["Feature"] == "X")` |
| `update_row(ws, row, header, data)` | Zellen per Spaltennamen ändern | `update_row(ws, row, h, {"Status": "Done"})` |
| `insert_row_after(ws, row)` | Neue Zeile einfügen | — |
| `save_workbook(wb, path, suffix)` | Speichern (Original oder Kopie) | `save_workbook(wb, "data.xlsx", suffix="_updated")` |
| `xlsx_to_csv(path)` | Sheet → UTF-8 CSV | — |
| `xlsx_to_md(path)` | Sheet → Markdown-Tabelle | — |

### Benötigte Pakete

```
openpyxl>=3.1.0
```

---

## 5. Typische Workflows

### Jira-Attachments konvertieren
```text
1. Dateien liegen in inbox/jira/
2. converter.to_markdown() erkennt Format automatisch
3. Output als .md in output/context/
4. Weiterverarbeitung durch Agents oder Prompts
```

### Excel-Daten bearbeiten
```text
1. open_workbook("inbox/data.xlsx")
2. get_header_map() für Spaltenreferenzen
3. find_rows() zum Filtern
4. update_row() für Änderungen
5. save_workbook() mit _updated Suffix (Original bleibt)
```

### Batch-Konvertierung
```text
convert_directory(Path("inbox/documents"), Path("output/markdown"))
→ Alle unterstützten Formate werden automatisch konvertiert
```

---

## 6. Referenzen

| Thema | Pfad |
|---|---|
| Converter | `_tools/documents/converter.py` |
| Doc Processor | `_tools/documents/doc_processor.py` |
| Excel Editor | `_tools/documents/excel_editor.py` |
| Requirements | `requirements.txt` |


