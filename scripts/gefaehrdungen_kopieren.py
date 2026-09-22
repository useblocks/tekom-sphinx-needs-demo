"""Kopiert die needs.json der Risikobeurteilung ins Handbuch.

Der Zeitstempel aus dem Build wird dabei entfernt: Sonst änderte sich die
eingecheckte Datei bei jedem Lauf, auch wenn keine Gefährdung anders ist.

Aufruf: python scripts/gefaehrdungen_kopieren.py <quelle.json> <ziel.json>
"""

import json
import sys
from pathlib import Path


def main() -> int:
    quelle, ziel = Path(sys.argv[1]), Path(sys.argv[2])
    daten = json.loads(quelle.read_text(encoding="utf-8"))
    daten.pop("created", None)
    for version in daten.get("versions", {}).values():
        version.pop("created", None)

    ziel.write_text(
        json.dumps(daten, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    anzahl = sum(len(v.get("needs", {})) for v in daten.get("versions", {}).values())
    print(f"{anzahl} Gefährdungen übernommen: {ziel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
