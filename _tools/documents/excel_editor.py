#!/usr/bin/env python3
"""
Excel-Editor
============
Allgemeine Funktionen zum Lesen, Suchen, Bearbeiten und Exportieren von
Excel-Dateien (.xlsx) mit openpyxl.

Enthaltene Funktionen
---------------------
- :func:`open_workbook`       – Workbook öffnen (read/write)
- :func:`get_header_map`      – Spaltenüberschriften → Spaltenindex
- :func:`find_rows`           – Zeilen per Filterfunktion suchen
- :func:`update_row`          – Zellen einer Zeile per Spaltennamen aktualisieren
- :func:`insert_row_after`    – Zeile nach einer bestimmten Zeile einfügen
- :func:`save_workbook`       – Workbook speichern (Original oder Kopie)
- :func:`xlsx_to_csv`         – Sheet als UTF-8 CSV exportieren
- :func:`xlsx_to_md`          – Sheet als Markdown-Tabelle exportieren

Voraussetzungen (in requirements.txt)
--------------------------------------
  openpyxl>=3.1.0

Verwendung
----------
>>> from _tools.documents.excel_editor import open_workbook, find_rows, update_row, save_workbook
>>> wb, ws = open_workbook("meine_datei.xlsx")
>>> header = get_header_map(ws)
>>> rows = find_rows(ws, header, lambda r: r.get("Feature") == "MACK Abstract")
>>> update_row(ws, rows[0], header, {"sh:targetClass": "frbr:Expression"})
>>> save_workbook(wb, "meine_datei.xlsx", suffix="_updated")
"""

import csv
import shutil
from datetime import date
from pathlib import Path
from typing import Any, Callable


# ------------------------------------------------------------------ #
#  Öffnen                                                              #
# ------------------------------------------------------------------ #

def open_workbook(path: Path | str, sheet_name: str | None = None):
    """
    Öffnet eine .xlsx-Datei und gibt (Workbook, Worksheet) zurück.

    Args:
        path:       Pfad zur .xlsx-Datei.
        sheet_name: Name des zu öffnenden Sheets. Wenn None, wird das
                    aktive (erste) Sheet verwendet.

    Returns:
        Tupel (openpyxl.Workbook, openpyxl.worksheet.worksheet.Worksheet)

    Raises:
        ImportError:  Wenn openpyxl nicht installiert ist.
        FileNotFoundError: Wenn die Datei nicht existiert.
        KeyError:     Wenn sheet_name angegeben, aber nicht vorhanden.
    """
    try:
        import openpyxl  # type: ignore
    except ImportError:
        raise ImportError(
            "openpyxl ist nicht installiert. Bitte 'pip install openpyxl' ausführen."
        )

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {path}")

    wb = openpyxl.load_workbook(path)
    ws = wb[sheet_name] if sheet_name else wb.active
    return wb, ws


# ------------------------------------------------------------------ #
#  Header-Map                                                          #
# ------------------------------------------------------------------ #

def get_header_map(ws, header_row: int = 1) -> dict[str, int]:
    """
    Liest die Spaltenüberschriften eines Worksheets und gibt ein
    Dict {Spaltenname → Spaltenindex (1-basiert)} zurück.

    Args:
        ws:         openpyxl Worksheet.
        header_row: Zeilennummer der Überschriftenzeile (Standard: 1).

    Returns:
        Dict mit Spaltennamen als Schlüssel und 1-basiertem Spaltenindex
        als Wert. Leere Zellen werden übersprungen.
    """
    header_map: dict[str, int] = {}
    for cell in ws[header_row]:
        if cell.value is not None:
            header_map[str(cell.value)] = cell.column
    return header_map


# ------------------------------------------------------------------ #
#  Zeilen suchen                                                       #
# ------------------------------------------------------------------ #

def find_rows(
    ws,
    header: dict[str, int],
    match_fn: Callable[[dict[str, Any]], bool],
    start_row: int = 2,
) -> list[int]:
    """
    Sucht alle Zeilen, auf die eine Filterfunktion zutrifft.

    Args:
        ws:        openpyxl Worksheet.
        header:    Header-Map aus :func:`get_header_map`.
        match_fn:  Funktion, die ein Dict {Spaltenname → Zellwert} entgegen-
                   nimmt und True/False zurückgibt.
        start_row: Erste zu prüfende Zeile (Standard: 2, damit Überschrift
                   übersprungen wird).

    Returns:
        Liste von 1-basierten Zeilennummern der Treffer.
    """
    col_to_name = {v: k for k, v in header.items()}
    results: list[int] = []

    for row_idx in range(start_row, ws.max_row + 1):
        row_data: dict[str, Any] = {}
        for col_idx, name in col_to_name.items():
            cell = ws.cell(row=row_idx, column=col_idx)
            row_data[name] = cell.value
        if match_fn(row_data):
            results.append(row_idx)

    return results


# ------------------------------------------------------------------ #
#  Zeile aktualisieren                                                 #
# ------------------------------------------------------------------ #

def update_row(
    ws,
    row_idx: int,
    header: dict[str, int],
    updates: dict[str, Any],
) -> None:
    """
    Aktualisiert ausgewählte Zellen einer Zeile per Spaltenname.

    Args:
        ws:       openpyxl Worksheet.
        row_idx:  1-basierter Zeilenindex der zu ändernden Zeile.
        header:   Header-Map aus :func:`get_header_map`.
        updates:  Dict {Spaltenname → neuer Wert}. Unbekannte Spaltennamen
                  werden mit einer Warnung übersprungen.
    """
    for col_name, new_value in updates.items():
        if col_name not in header:
            print(f"  [WARNUNG] Spalte '{col_name}' nicht im Header – übersprungen.")
            continue
        ws.cell(row=row_idx, column=header[col_name], value=new_value)


# ------------------------------------------------------------------ #
#  Zeile einfügen                                                      #
# ------------------------------------------------------------------ #

def insert_row_after(
    ws,
    after_row_idx: int,
    header: dict[str, int],
    data: dict[str, Any],
) -> int:
    """
    Fügt eine neue Zeile direkt nach ``after_row_idx`` ein.

    Alle nachfolgenden Zeilen werden nach unten verschoben. Die neue Zeile
    wird mit den Werten aus ``data`` befüllt.

    Args:
        ws:            openpyxl Worksheet.
        after_row_idx: 1-basierter Zeilenindex, nach dem eingefügt wird.
        header:        Header-Map aus :func:`get_header_map`.
        data:          Dict {Spaltenname → Wert} für die neue Zeile.
                       Nicht angegebene Spalten bleiben leer.

    Returns:
        1-basierter Zeilenindex der neu eingefügten Zeile.
    """
    new_row_idx = after_row_idx + 1
    ws.insert_rows(new_row_idx)

    for col_name, value in data.items():
        if col_name not in header:
            print(f"  [WARNUNG] Spalte '{col_name}' nicht im Header – übersprungen.")
            continue
        ws.cell(row=new_row_idx, column=header[col_name], value=value)

    return new_row_idx


# ------------------------------------------------------------------ #
#  Speichern                                                           #
# ------------------------------------------------------------------ #

def save_workbook(
    wb,
    original_path: Path | str,
    suffix: str | None = None,
    date_stamp: bool = True,
    overwrite: bool = False,
) -> Path:
    """
    Speichert ein Workbook.

    Standardmäßig wird eine neue Datei mit Datumsstempel erstellt und die
    Originaldatei nicht überschrieben.

    Args:
        wb:            openpyxl Workbook.
        original_path: Pfad zur Originaldatei (wird für Namensgebung genutzt).
        suffix:        Optionaler Suffix vor dem Datum, z.B. ``"_updated"``
                       → ``datei_updated_20260304.xlsx``.
        date_stamp:    Wenn True, wird das heutige Datum an den Dateinamen
                       angehängt (Standard: True).
        overwrite:     Wenn True, wird ``original_path`` direkt überschrieben
                       (``suffix`` und ``date_stamp`` werden ignoriert).

    Returns:
        Pfad der gespeicherten Datei.
    """
    original_path = Path(original_path)

    if overwrite:
        save_path = original_path
    else:
        stem = original_path.stem
        ext = original_path.suffix
        parts = [stem]
        if suffix:
            parts.append(suffix.lstrip("_"))
        if date_stamp:
            parts.append(date.today().strftime("%Y%m%d"))
        save_path = original_path.parent / f"{'_'.join(parts)}{ext}"

    wb.save(save_path)
    print(f"  Gespeichert: {save_path}")
    return save_path


# ------------------------------------------------------------------ #
#  Export: CSV                                                         #
# ------------------------------------------------------------------ #

def xlsx_to_csv(
    path: Path | str,
    sheet_name: str | None = None,
    output_path: Path | str | None = None,
    delimiter: str = ",",
) -> Path:
    """
    Exportiert ein Worksheet als UTF-8 CSV-Datei.

    Args:
        path:        Pfad zur .xlsx-Datei.
        sheet_name:  Name des Sheets (None → aktives Sheet).
        output_path: Zielpfad der CSV. Wenn None, wird die CSV neben der
                     XLSX mit gleichem Stammnamen gespeichert.
        delimiter:   Trennzeichen (Standard: Komma).

    Returns:
        Pfad der erstellten CSV-Datei.
    """
    _, ws = open_workbook(path, sheet_name)
    path = Path(path)
    output_path = Path(output_path) if output_path else path.with_suffix(".csv")

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=delimiter)
        for row in ws.iter_rows(values_only=True):
            writer.writerow([v if v is not None else "" for v in row])

    print(f"  CSV exportiert: {output_path}")
    return output_path


# ------------------------------------------------------------------ #
#  Export: Markdown                                                    #
# ------------------------------------------------------------------ #

def xlsx_to_md(
    path: Path | str,
    sheet_name: str | None = None,
    output_path: Path | str | None = None,
    header_row: int = 1,
) -> Path:
    """
    Exportiert ein Worksheet als Markdown-Tabelle.

    Args:
        path:        Pfad zur .xlsx-Datei.
        sheet_name:  Name des Sheets (None → aktives Sheet).
        output_path: Zielpfad der .md-Datei. Wenn None, wird die Datei neben
                     der XLSX mit gleichem Stammnamen gespeichert.
        header_row:  Zeilennummer der Überschriftenzeile (Standard: 1).

    Returns:
        Pfad der erstellten Markdown-Datei.

    Notes:
        Pipezeichen (``|``) in Zellwerten werden durch ``/`` ersetzt, um
        die Markdown-Tabellenstruktur nicht zu beschädigen.
    """
    _, ws = open_workbook(path, sheet_name)
    path = Path(path)
    output_path = Path(output_path) if output_path else path.with_suffix(".md")

    def _sanitize(v: Any) -> str:
        """Wandelt Zellwert in sicheren Markdown-String um."""
        s = str(v) if v is not None else ""
        return s.replace("|", "/")

    lines: list[str] = []
    for row_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
        cells = [_sanitize(c) for c in row]
        line = "|" + "|".join(cells) + "|"
        lines.append(line)
        if row_idx == header_row:
            sep = "|" + "|".join(":---" for _ in cells) + "|"
            lines.append(sep)

    with output_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"  Markdown exportiert: {output_path}")
    return output_path

