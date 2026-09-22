"""Erzeugt den eingecheckten Auszug aus dem Schwesterprojekt sphinx-needs-demo.

Das Handbuch bindet die erzeugte Datei als External Needs ein und verlinkt damit
auf die Entwicklungsdokumentation desselben Produkts — ohne das Nachbarrepo zur
Bauzeit zu brauchen.

Gelesen werden die Quelldateien unter docs/coffee-machine/, nicht ein Build:
Das Schwesterprojekt braucht Java und PlantUML, die Demo soll das nicht.

Aufruf: python scripts/sw_projekt_auszug.py <schwesterprojekt> <ziel.json>
"""

import json
import re
import sys
from pathlib import Path

# Nur diese Typen sind für die Brücke interessant.
TYP_NAMEN = {
    "req": "Anforderung",
    "swreq": "SW-Anforderung",
    "component": "Komponente",
    "interface": "Schnittstelle",
    "test": "Testfall",
}
TYPEN = tuple(TYP_NAMEN)

DIREKTIVE = re.compile(r"^\s*\.\.\s+(" + "|".join(TYPEN) + r")::\s*(.+?)\s*$")
FELD = re.compile(r"^\s*:(\w[\w-]*):\s*(.*?)\s*$")


def needs_aus_datei(pfad: Path, docname: str) -> dict[str, dict]:
    needs: dict[str, dict] = {}
    aktuell: dict | None = None
    for zeile in pfad.read_text(encoding="utf-8").splitlines():
        treffer = DIREKTIVE.match(zeile)
        if treffer:
            # Aus Sicht des Handbuchs ist drüben alles ein Objekt des
            # Entwicklungsprojekts. Der Originaltyp bleibt als Feld erhalten,
            # damit das Handbuch nicht fünf Softwaretypen kennen muss.
            aktuell = {
                "type": "extern",
                "quelltyp": TYP_NAMEN[treffer.group(1)],
                "title": treffer.group(2),
                "docname": docname,
            }
            continue
        if aktuell is None:
            continue
        feld = FELD.match(zeile)
        if feld and feld.group(1) == "id":
            aktuell["id"] = feld.group(2)
            needs[aktuell["id"]] = aktuell
        elif not zeile.strip():
            aktuell = None
    return needs


def main() -> int:
    quelle = Path(sys.argv[1]) / "docs" / "coffee-machine"
    ziel = Path(sys.argv[2])

    needs: dict[str, dict] = {}
    for datei in sorted(quelle.glob("*.rst")):
        needs.update(needs_aus_datei(datei, f"coffee-machine/{datei.stem}"))

    ziel.write_text(
        json.dumps(
            {
                "created": "Auszug aus sphinx-needs-demo, erzeugt von scripts/sw_projekt_auszug.py",
                "current_version": "1.0",
                "project": "Sphinx-Needs Demo (Entwicklungsprojekt)",
                "versions": {"1.0": {"needs": needs, "version": "1.0"}},
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"{len(needs)} Needs aus dem Schwesterprojekt übernommen: {ziel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
