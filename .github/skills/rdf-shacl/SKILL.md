---
name: rdf-shacl
description: "RDF/SHACL Working Skill: Serialization formats, SHACL shape syntax, workspace tools, and domain conventions. Activated for RDF, SHACL, Turtle, Shape, Triple, Graph work."
metadata:
  trigger: RDF, SHACL, Turtle, Shape, Triple, Graph, rdflib, pyshacl, Validation, N-Triples, JSON-LD
  author: Author
---

# RDF & SHACL Working Knowledge

Practical knowledge for working with RDF graphs and SHACL validation.

---

## 1. RDF-Serialisierungsformate

| Format | Endung | Beschreibung | Einsatz im Workspace |
|---|---|---|---|
| **Turtle** | `.ttl` | Terse RDF Triple Language — menschenlesbar | Primary format for RDF data and shapes |
| **JSON-LD** | `.jsonld` | JSON für Linked Data | API-Austausch, Web-Integration |
| **N-Triples** | `.nt` | Ein Triple pro Zeile — maschinell einfach | Bulk-Import/Export |
| **RDF/XML** | `.rdf`, `.xml` | XML-Serialisierung | Legacy-Systeme |
| **Notation 3** | `.n3` | Superset von Turtle | Selten verwendet |
| **TriG** | `.trig` | Named Graphs in Turtle-Syntax | Multi-Graph-Szenarien |

---

## 2. Turtle Kurzreferenz

```turtle
@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex:      <http://example.org/ontology/> .
@prefix sh:      <http://www.w3.org/ns/shacl#> .

# Subject — Predicate — Object
<http://example.org/work/123>
    rdf:type           ex:Work ;
    dcterms:title      "Beispieldokument"@de ;
    dcterms:language   "nl" ;
    ex:hasSubject <http://example.org/subject/tax> .
```

**Syntax-Regeln:**
- Statements enden mit `.`
- Mehrere Predicates zum selben Subject: `;` als Trenner
- Mehrere Objects zum selben Predicate: `,` als Trenner
- Strings: `"text"` oder `"text"@de` (mit Sprachtag) oder `"text"^^xsd:date` (mit Datentyp)

---

## 3. SHACL-Shape-Grundstruktur

```turtle
@prefix sh:      <http://www.w3.org/ns/shacl#> .
@prefix ex:      <http://example.org/ontology/> .

# Shape-Definition
ex:WorkShape
    a sh:NodeShape ;
    sh:targetClass ex:Work ;
    sh:property [
        sh:path     dcterms:title ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
        sh:message  "Work muss genau einen Titel haben" ;
    ] ;
    sh:property [
        sh:path     ex:hasSubject ;
        sh:minCount 1 ;
        sh:nodeKind sh:IRI ;
        sh:message  "Work muss mindestens ein Subject haben" ;
    ] .
```

### Häufige SHACL-Constraints

| Constraint | Bedeutung | Beispiel |
|---|---|---|
| `sh:minCount` | Mindestanzahl | `sh:minCount 1` (Pflichtfeld) |
| `sh:maxCount` | Maximalanzahl | `sh:maxCount 1` (nur ein Wert) |
| `sh:datatype` | Erwarteter Datentyp | `sh:datatype xsd:string` |
| `sh:nodeKind` | Art des Knotens | `sh:nodeKind sh:IRI` (muss URI sein) |
| `sh:class` | Erwartete Klasse | `sh:class ex:Subject` |
| `sh:in` | Erlaubte Werte | `sh:in ("nl" "be" "de")` |
| `sh:pattern` | Regex-Pattern | `sh:pattern "^[A-Z]{2}-"` |
| `sh:hasValue` | Muss diesen Wert haben | `sh:hasValue ex:Work` |
| `sh:or` | Eins von mehreren | `sh:or ( [...] [...] )` |

---

## 4. Workspace-Tools

### `_tools/rdf/rdf_processor.py`

| Funktion | Zweck | Aufruf |
|---|---|---|
| `load_graph(path)` | RDF-Datei → rdflib.Graph | `from _tools.rdf.rdf_processor import load_graph` |
| `graph_summary(graph)` | Markdown-Zusammenfassung (Namespaces, Subjects, Predicates) | `summary = graph_summary(g)` |
| `validate_shacl(data, shapes, output)` | SHACL-Validierung → (conforms, report) | `ok, report = validate_shacl(data_path, shapes_path)` |

**Input-Pfade:** `inbox/rdf-shacl/`
**Output-Pfade:** `output/reports/`

**Format-Erkennung:** Automatisch per Dateiendung:
| Endung | rdflib-Format |
|---|---|
| `.ttl`, `.turtle` | `turtle` |
| `.jsonld`, `.json` | `json-ld` |
| `.nt` | `nt` |
| `.rdf`, `.xml` | `xml` |
| `.n3` | `n3` |

**Shape-Datei-Erkennung:** Dateien mit diesen Namensmustern werden als SHACL-Shapes behandelt:
`-shapes.ttl`, `.shacl.ttl`, `_shapes.ttl`, `-shacl.ttl`

### Benötigte Pakete

```
rdflib   – pip install rdflib
pyshacl  – pip install pyshacl
```

---

## 5. Domain-Specific Conventions

Replace this section with your project's RDF/SHACL conventions.

### Namespace-Prefixes (Example)

| Prefix | URI | Usage |
|---|---|---|
| `ex:` | `http://example.org/` | Your domain namespace |
| `dcterms:` | `http://purl.org/dc/terms/` | Dublin Core Terms |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` | Controlled Vocabularies |

### Shape Organisation
- One shape file per domain entity
- Naming: `{entity}_shape.ttl` (snake_case)
- New shapes follow `{Entity}Shape` naming convention (PascalCase)

### Validation Workflow
```text
1. Load data graph:   load_graph("inbox/rdf-shacl/data.ttl")
2. Load shape graph:  (auto-detected by filename pattern)
3. Validate:          validate_shacl(data_path, shapes_path)
4. Generate report:   output/reports/validation_report.md
```

---

## 6. Referenzen

| Thema | Pfad |
|---|---|
| Terminologie-Glossar | `_tools/validate/glossary.yaml` |
| SHACL W3C Spec | `https://www.w3.org/TR/shacl/` |


