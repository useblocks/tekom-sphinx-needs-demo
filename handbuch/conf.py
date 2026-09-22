# Konfiguration des Sphinx-Builds.

project = "BrewMaster Pro 3000"
copyright = "2026, BrewMaster Appliances GmbH"
author = "Technische Redaktion"
language = "de"

extensions = [
    "myst_parser",
]

myst_enable_extensions = ["colon_fence"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"

# Das Stylesheet liegt ausserhalb des Projekts: Handbuch und Risikobeurteilung
# teilen sich eine Datei, damit ein Need in beiden Projekten gleich aussieht.
html_static_path = ["_static", "../styles"]
html_css_files = ["needs.css"]

html_title = "BrewMaster Pro 3000"
