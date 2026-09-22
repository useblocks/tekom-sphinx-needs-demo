project = "BrewMaster Pro 3000 – Risikobeurteilung"
copyright = "2026, BrewMaster Appliances GmbH"
author = "Sicherheitsingenieurwesen"
language = "de"

extensions = [
    "myst_parser",
    "sphinx_needs",
]

myst_enable_extensions = ["colon_fence"]

needs_from_toml = "ubproject.toml"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"

# Dasselbe Stylesheet wie im Handbuch: Eine Gefährdung sieht in beiden
# Projekten gleich aus.
html_static_path = ["../styles"]
html_css_files = ["needs.css"]

html_title = "Risikobeurteilung"
