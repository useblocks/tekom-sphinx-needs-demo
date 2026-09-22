# Konfiguration des Sphinx-Builds.
# Alles, was Sphinx-Needs betrifft, steht in ubproject.toml.

project = "BrewMaster Pro 3000"
copyright = "2026, BrewMaster Appliances GmbH"
author = "Technische Redaktion"
language = "de"

extensions = [
    "myst_parser",
    "sphinx_needs",
]

# Colon-Fences sind ohne diese Zeile nicht verfuegbar.
myst_enable_extensions = ["colon_fence"]

# Sphinx-Needs-Konfiguration aus der TOML-Datei.
needs_from_toml = "ubproject.toml"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"

# Das Stylesheet liegt ausserhalb des Projekts: Handbuch und Risikobeurteilung
# teilen sich eine Datei, damit ein Need in beiden Projekten gleich aussieht.
html_static_path = ["_static", "../styles"]
html_css_files = ["needs.css"]

html_title = "BrewMaster Pro 3000"
