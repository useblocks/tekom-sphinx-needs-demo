# Variantendaten

Jede Datei beschreibt eine Produktvariante des BrewMaster Pro 3000. Ausgewählt wird
die Variante ueber `needs_variant_data_file`. Der Default (`plus.json`) steht in
`conf.py`, einzelne Bauten ueberschreiben ihn:

```bash
sphinx-build -b html handbuch _build/compact -D needs_variant_data_file=_data/varianten/compact.json
```

Der Pfad ist relativ zum Quellverzeichnis `handbuch/`. `-D` ist groß geschrieben,
`-d` wäre der Doctree-Cache.

| Variante | Milchsystem | App | Doppeltasse | Tank |
|---|---|---|---|---|
| `pro.json` | ja | nein | ja | 2,2 l |
| `plus.json` | ja | ja | ja | 2,2 l |
| `compact.json` | nein | nein | nein | 1,4 l |

Die Ausstattung steht an zwei Stellen: hier als Schalter für den Bau und in
`varianten.md` als `has_features` der Variant-Needs. Die Schalter entscheiden, was
in den Bau kommt. Die Variant-Needs beschreiben die ganze Baureihe, auch die
Varianten, die gerade nicht gebaut werden. Beide müssen übereinstimmen, geprüft
wird das bisher nicht.

Die Daten werden an vier Stellen gelesen:

- in Feldwerten als `<{ var.produkt.name }>`
- im Fließtext als `` :variant:`technik.tankvolumen` `` (ohne `var.`-Präfix)
- als Bedingung ganzer Abschnitte in der `if`-Direktive
- in Filtern von `needtable` und `needflow`
