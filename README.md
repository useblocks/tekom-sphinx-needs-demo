# BrewMaster Pro 3000: Demo zum tekom-Vortrag

Beispielprojekt und Folien zum tekom-Online-Event **„Docs as Code für Fortgeschrittene:
Das Potenzial von Sphinx-Needs"**.

Gezeigt wird ein Benutzerhandbuch, in dem Glossarbegriffe, Warnhinweise,
Handlungsanweisungen, Produktmerkmale und Varianten adressierbare Objekte sind statt
kopierter Textstellen.

## Einrichten

Vorausgesetzt werden [uv](https://docs.astral.sh/uv/) und Graphviz
(`brew install graphviz` bzw. `apt-get install graphviz`).

```bash
make setup     # Abhängigkeiten installieren, Graphviz prüfen
make check     # Smoke-Test: rendern alle Direktiven?
make live      # Live-Vorschau auf http://localhost:8000
```

## Die Projekte im Repo

| Ordner | Inhalt |
|---|---|
| `handbuch/` | Das Benutzerhandbuch. Hauptprojekt der Demo. |
| `risikobeurteilung/` | Winziges zweites Projekt mit den Gefährdungen. Liefert `handbuch/_data/gefaehrdungen.json`. |
| `styles/` | Ein Stylesheet für die Darstellung der Needs, von beiden Sphinx-Projekten eingebunden. |
| `slides/` | Das Marp-Deck. |
| `scripts/` | Zwei Wartungsskripte, auf der Bühne unsichtbar. |

## Bauen

```bash
make hazards          # Risikobeurteilung bauen, Gefährdungen ins Handbuch kopieren
make plus             # eine Variante bauen -> _build/plus/
make alle-varianten   # alle drei Varianten nebeneinander
make slides           # Folien nach HTML und PDF (braucht Node/npx)
make referent         # Folien lokal ausliefern, Referentensicht im Browser
make fallback         # jeden Demo-Stand einmal als fertiges HTML
```

Die Variante wird ausschließlich über `needs_variant_data_file` gewählt:

```bash
uv run sphinx-build -b html handbuch _build/compact \
  -D needs_variant_data_file=_data/varianten/compact.json
```

## Demo-Stände

Jeder Abschnitt des Vortrags hat einen Git-Tag. Alle Stände bauen fehlerfrei, außer
`stand-06-bruch`. Der enthält die Schemaverletzung absichtlich.

| Tag | Vortragsabschnitt | Zustand |
|---|---|---|
| `stand-00-ohne-needs` | 5–12 Das Prinzip, Problemfolie | Normales Sphinx-Handbuch, Warnhinweise kopiert, Redaktionstabelle von Hand gepflegt, bei „Heißwasser beziehen" fehlt ein Hinweis |
| `stand-01-anweisungen` | 5–12 Das Prinzip, Lösungsfolie | Handlungsanweisungen sind `proc`-Needs. Glossar und Warnhinweise bleiben, wie sie waren |
| `stand-02-glossar` | 17–30 Baustein 1, Problemfolie Baustein 2 | Glossarbegriffe sind `term`-Needs, Glossarseite entsteht, „wird erwähnt in" funktioniert |
| `stand-03-warnhinweise` | 30–45 Baustein 2 | Warnhinweise sind Needs, per `needextract` wiederverwendet |
| `stand-04-auswertung` | 30–45 Baustein 2 | Redaktionsseite generiert, handgepflegte Tabelle gelöscht |
| `stand-05-varianten` | 50–65 Baustein 3 | Variantendaten, drei Handbücher aus einer Quelle |
| `stand-06-bruch` | 65–75 Die Brücke | Gefährdungen importiert, `HAZ_UEBERLAUF` unabgedeckt, Build meldet es |
| `stand-07-final` | 65–75 Die Brücke | Sechster Warnhinweis ergänzt, alles grün, Verknüpfung ins Entwicklungsprojekt |

```bash
git checkout -f stand-03-warnhinweise   # zu einem Stand springen
git checkout -f main                    # zurück
```

`-f` verwirft alles, was auf der Bühne live geändert wurde, auch die von `make hazards`
neu geschriebene Gefährdungsdatei. Ohne `-f` bricht der Wechsel ab, sobald der nächste
Stand eine geänderte Datei ebenfalls ändert, oder er nimmt die Änderung still mit.

## Referentensicht

`make referent` liefert das Deck unter <http://localhost:8080/slides.md> aus. Im Browser
öffnet die Taste `p` ein zweites Fenster mit Sprechernotizen, Timer und der nächsten Folie.
Dieses Fenster kommt auf den Laptop, das erste auf den Beamer.

Das PDF kann das nicht, es kennt keine Notizen. Wer sie trotzdem im PDF braucht, exportiert
mit `marp slides/slides.md --pdf --pdf-notes`; die Notizen liegen dann als Kommentare im
PDF und sind in Vorschau oder Acrobat in der Seitenleiste zu sehen.

## Das Schwesterprojekt

Dieselbe Maschine wird in
[useblocks/sphinx-needs-demo](https://github.com/useblocks/sphinx-needs-demo) aus Sicht
der Softwareentwicklung dokumentiert, mit Anforderungen, Architektur und Testfällen.
Brühtemperatur, Kaffeestärken und Sicherheitsabschaltung stimmen in beiden Projekten
überein.

Die Verbindung ist eine einzige eingecheckte Datei, `handbuch/_data/sw-projekt.json`.
Das Nachbarrepo wird zum Bauen nicht gebraucht. Liegt es daneben, erneuert
`make sw-projekt` den Auszug.

## Technische Notizen

- Markup ist MyST/Markdown mit Colon-Fences (`myst_enable_extensions = ["colon_fence"]`
  in `conf.py`). Verschachtelte Direktiven brauchen vier Doppelpunkte außen.
- Die Sphinx-Needs-Konfiguration steht vollständig in `handbuch/ubproject.toml`,
  die Schemaregeln in `handbuch/schemas.json`.
- Diagramme laufen über Graphviz (`flow_engine = "graphviz"`), nicht über PlantUML.
  Kein Java, kein Netzzugriff beim Bauen.
- `.smoke/` ist ein Einseitenprojekt, das jede verwendete Direktive und Rolle einmal
  rendert. `make check` baut es mit `-W`.
