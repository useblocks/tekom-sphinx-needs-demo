# Smoke-Test: prueft, dass alle im Vortrag verwendeten Direktiven und Rollen
# in MyST-Colon-Fences fehlerfrei rendern. Wird mit -W gebaut, jede Warnung
# laesst den Test scheitern.
#
# Konfiguration, Typen und Schemaregeln kommen aus dem Handbuch-Projekt.

project = "Smoke-Test"
extensions = ["myst_parser", "sphinx_needs"]
myst_enable_extensions = ["colon_fence"]

needs_from_toml = "../handbuch/ubproject.toml"
needs_variant_data_file = "../handbuch/_data/varianten/plus.json"

exclude_patterns = ["_build"]
html_theme = "furo"
