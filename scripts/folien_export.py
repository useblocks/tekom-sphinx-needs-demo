"""Erzeugt Folienbilder und das PDF aus der von Marp gebauten HTML-Datei.

Marps eigener PNG- und PDF-Export startet einen Browser und bleibt dabei
regelmaessig haengen. Die HTML-Ausgabe braucht keinen Browser. Dieses Skript
uebernimmt den Rest mit Playwrights eigenem Chromium.

Aufruf:
    uv run --with playwright python scripts/folien_export.py [bilder|pdf|alles]
"""

import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

WURZEL = Path(__file__).resolve().parent.parent
HTML = WURZEL / "_build" / "slides" / "slides.html"
BILDER = WURZEL / "_build" / "folien"
PDF = WURZEL / "_build" / "slides" / "slides.pdf"
BREITE, HOEHE = 1280, 720

# Die Bedienleiste des Marp-Players gehoert weder aufs Bild noch ins PDF.
OHNE_LEISTE = ".bespoke-marp-osc { display: none !important; }"


def anzahl_folien(html: str) -> int:
    return len(re.findall(r"<svg[^>]*data-marpit-svg", html))


def main() -> int:
    was = sys.argv[1] if len(sys.argv) > 1 else "alles"
    if not HTML.exists():
        print(f"Erst die Folien bauen: make slides ({HTML} fehlt)")
        return 1

    gesamt = anzahl_folien(HTML.read_text(encoding="utf-8"))
    BILDER.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        seite = browser.new_page(viewport={"width": BREITE, "height": HOEHE})

        if was in ("bilder", "alles"):
            for nummer in range(1, gesamt + 1):
                seite.goto(f"{HTML.as_uri()}#{nummer}")
                seite.add_style_tag(content=OHNE_LEISTE)
                seite.wait_for_timeout(120)
                seite.screenshot(path=str(BILDER / f"folie-{nummer:02d}.png"))
            print(f"{gesamt} Folien nach {BILDER}")

        if was in ("pdf", "alles"):
            seite.goto(HTML.as_uri())
            seite.add_style_tag(content=OHNE_LEISTE)
            seite.wait_for_timeout(200)
            seite.pdf(
                path=str(PDF),
                width=f"{BREITE}px",
                height=f"{HOEHE}px",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            )
            print(f"PDF nach {PDF}")

        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
