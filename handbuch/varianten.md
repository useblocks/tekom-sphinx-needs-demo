# Varianten und technische Daten

Diese Anleitung gilt für die Baureihe BrewMaster Pro 3000. Sie halten die Variante
**{variant}`produkt.name`** in den Händen.

## Technische Daten

| Angabe | Wert |
|---|---|
| Wassertank | {variant}`technik.tankvolumen` |
| Bohnenbehälter | {variant}`technik.bohnenbehaelter` |
| Netzspannung | {variant}`technik.netzspannung` |
| Leistungsaufnahme | {variant}`technik.leistung` |

## Ausstattung Ihres Geräts

:::{needtable}
:filter: type == "feature" and ("VAR_" + var.produkt.id.upper()) in has_features_back
:columns: title as "Merkmal", id
:style: table
:sort: title
:::

## Produktmerkmale der Baureihe

:::{feature} Drei Kaffeestärken
:id: FEAT_KAFFEESTAERKE

Stärkewahl schwach, mittel und stark mit je 180 ml Bezugsmenge.
:::

:::{feature} Milchsystem
:id: FEAT_MILCHSYSTEM

Ansaugschlauch, Aufschäumer und Auslauf für Milchgetränke mit automatischem
Spülprogramm.
:::

:::{feature} App-Steuerung
:id: FEAT_APP

Bedienung und Getränkeprofile über die BrewMaster-App per Bluetooth.
:::

:::{feature} Heißwasserbezug
:id: FEAT_HEISSWASSER

Separater Heißwasserauslauf für Tee und Vorwärmen der Tassen.
:::

:::{feature} Doppeltassenbezug
:id: FEAT_DOPPELTASSE

Zwei Tassen in einem Durchlauf, mit geteiltem Auslauf.
:::

:::{feature} Keramikmahlwerk
:id: FEAT_KERAMIKMAHLWERK

Verschleißarmes Mahlwerk mit zwölf einstellbaren Stufen für den
{need}`GLOSS_MAHLGRAD`.
:::

## Varianten der Baureihe

:::{variant} BrewMaster Pro 3000
:id: VAR_PRO
:has_features: FEAT_KAFFEESTAERKE, FEAT_MILCHSYSTEM, FEAT_HEISSWASSER, FEAT_DOPPELTASSE, FEAT_KERAMIKMAHLWERK

Die Grundvariante mit Milchsystem und großem Wassertank.
:::

:::{variant} BrewMaster Pro 3000 Plus
:id: VAR_PLUS
:has_features: FEAT_KAFFEESTAERKE, FEAT_MILCHSYSTEM, FEAT_APP, FEAT_HEISSWASSER, FEAT_DOPPELTASSE, FEAT_KERAMIKMAHLWERK

Wie die Grundvariante, zusätzlich mit App-Steuerung.
:::

:::{variant} BrewMaster Pro 3000 Compact
:id: VAR_COMPACT
:has_features: FEAT_KAFFEESTAERKE, FEAT_HEISSWASSER, FEAT_KERAMIKMAHLWERK

Die schmale Variante ohne Milchsystem, mit kleinerem Tank und Bohnenbehälter.
:::
