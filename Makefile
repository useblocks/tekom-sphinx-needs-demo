# Demo-Projekt zum tekom-Vortrag "Docs as Code für Fortgeschrittene"
#
# Alle Ziele laufen über uv. Ein einzelnes `make setup` genügt zum Start.

SPHINX   = uv run sphinx-build
HANDBUCH = handbuch
RISIKO   = risikobeurteilung
BUILD    = _build
SCHWESTER = ../sphinx-needs-demo
# Global installiert: npm i -g @marp-team/marp-cli
# NO_UPDATE_NOTIFIER schaltet die Update-Pruefung beim Start ab — die fragt
# sonst bei jedem Aufruf die npm-Registry und bleibt dabei regelmaessig haengen.
MARP      = NO_UPDATE_NOTIFIER=1 marp
THEME     = --theme slides/useblocks-slides.css --allow-local-files

.PHONY: setup check hazards sw-projekt live pro plus compact alle-varianten \
        slides referent folien-bilder fallback clean

## Abhängigkeiten installieren und Graphviz prüfen
setup:
	uv sync
	@command -v dot >/dev/null || { \
		echo "FEHLER: Graphviz fehlt. Installieren mit: brew install graphviz"; exit 1; }
	@echo "Setup fertig."

## Smoke-Test: rendern alle Direktiven in MyST? Jede Warnung ist ein Fehler.
# -E erzwingt einen frischen Lauf: geänderte Linktypen überleben den Cache nicht.
# .smoke/ kommt erst mit stand-07-final dazu, risikobeurteilung/ mit stand-06-bruch.
# Fehlt die conf.py, wird der Ordner übersprungen, damit das Ziel auf jedem Demo-Stand
# läuft. Der Ordner allein reicht nicht: Nach dem Zurückwechseln bleibt er mit dem
# ignorierten Cache liegen.
check:
	@if [ -f .smoke/conf.py ]; then $(SPHINX) -W -E -b html .smoke $(BUILD)/smoke; fi
	@if [ -f $(RISIKO)/conf.py ]; then $(SPHINX) -W -E -b html $(RISIKO) $(BUILD)/check-risiko; fi
	$(SPHINX) -W -E -b html $(HANDBUCH) $(BUILD)/check-handbuch
	@echo "Smoke-Test bestanden."

## Risikobeurteilung bauen und die Gefährdungen ins Handbuch kopieren
hazards:
	$(SPHINX) -b html $(RISIKO) $(RISIKO)/$(BUILD)/html
	uv run python scripts/gefaehrdungen_kopieren.py \
		$(RISIKO)/$(BUILD)/html/needs.json $(HANDBUCH)/_data/gefaehrdungen.json

## Auszug aus dem Schwesterprojekt erneuern (Wartungsziel, kein Bauziel).
## Fehlt das Nachbarrepo, passiert nichts — der eingecheckte Auszug bleibt.
sw-projekt:
	@if [ -d "$(SCHWESTER)/docs/coffee-machine" ]; then \
		uv run python scripts/sw_projekt_auszug.py \
			"$(SCHWESTER)" \
			"$(HANDBUCH)/_data/sw-projekt.json"; \
	else \
		echo "Kein Schwesterprojekt unter $(SCHWESTER) gefunden — Auszug bleibt unverändert."; \
	fi

## Live-Vorschau für die Bühne
live:
	uv run sphinx-autobuild --port 8000 --open-browser $(HANDBUCH) $(BUILD)/live

pro plus compact:
	$(SPHINX) -b html $(HANDBUCH) $(BUILD)/$@ \
		-D needs_variant_data_file=_data/varianten/$@.json

alle-varianten: pro plus compact
	@echo "Drei Handbücher aus einer Quelle: $(BUILD)/pro, $(BUILD)/plus, $(BUILD)/compact"

## Folien nach HTML und PDF. Marp baut nur das HTML, den Rest macht Playwright.
slides:
	@# --theme auf die eine Datei, nicht --theme-set auf den Ordner: Marp scannt
	@# den Ordner sonst komplett und bleibt an grossen Fremddateien haengen.
	@# Das Logo kommt per backgroundImage aus dem Front Matter und wird relativ
	@# zur Ausgabe aufgeloest, nicht relativ zur Quelle. Also mitkopieren.
	@mkdir -p $(BUILD)/slides/assets
	@cp slides/assets/ub_Logo.svg $(BUILD)/slides/assets/
	$(MARP) slides/slides.md $(THEME) -o $(BUILD)/slides/slides.html < /dev/null
	uv run --with playwright python scripts/folien_export.py pdf

## Referentensicht: Folien lokal ausliefern, im Browser mit "p" die zweite Ansicht
## oeffnen. Sprechernotizen, Timer und naechste Folie stehen dort. Das PDF kann das
## nicht, es kennt keine Notizen.
referent:
	@echo "Deck auf http://localhost:8080/slides.md, dort im Browser \"p\" druecken."
	$(MARP) -s slides/ $(THEME)

## Jede Folie als Einzelbild zum Durchsehen
folien-bilder: slides
	uv run --with playwright python scripts/folien_export.py bilder

## Alle Demo-Stände als fertiges HTML, falls auf der Bühne etwas klemmt
fallback:
	@./scripts/fallback.sh

clean:
	rm -rf $(BUILD) $(RISIKO)/$(BUILD) $(HANDBUCH)/$(BUILD)
