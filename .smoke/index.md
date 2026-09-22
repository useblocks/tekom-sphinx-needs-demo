# Smoke-Test

Jede Direktive und jede Rolle, die in der Demo vorkommt, einmal. Baut dieser Test
durch, liegt es nicht an MyST.

## Needs anlegen

:::{term} Testbegriff
:id: GLOSS_SMOKE

Ein Begriff, damit die `mentions`-Sammlung etwas zu finden hat.
:::

% Der Importschluessel aus ubproject.toml zeigt auf das Quellverzeichnis des
% jeweiligen Builds. Hier steht deshalb der Pfad direkt.
:::{needimport} ../handbuch/_data/gefaehrdungen.json
:filter: id == "HAZ_DAMPF"
:::

:::{warn} Testhinweis
:id: WARN_SMOKE
:signalwort: WARNUNG
:covers: HAZ_DAMPF

Deckt die importierte Gefährdung ab, sonst schlägt die Schemaregel zu.
:::

:::{proc} Testanweisung
:id: PROC_SMOKE
:status: freigegeben
:geprueft_am: 2026-01-01
:geraet: <{ var.produkt.name }>
:warns: WARN_SMOKE

Verweist auf {need}`GLOSS_SMOKE`, damit `links_from_content()` greift.
:::

## Rollen

- `need`: {need}`WARN_SMOKE`
- `need_count`: {need_count}`type == "proc"`
- `variant`: {variant}`technik.tankvolumen`

## Auswertende Direktiven

:::{needextract} WARN_SMOKE
:::

:::{needtable}
:filter: type == "proc"
:columns: id, title, status
:style: table
:::

:::{needflow}
:filter: type in ["warn", "hazard"]
:link_types: covers
:::

:::{needpie}
:labels: Freigegeben, Rest
:legend:

type == "proc" and status == "freigegeben"
type == "proc" and status != "freigegeben"
:::

::::{if} var.ausstattung.milchsystem

Dieser Absatz erscheint nur, wenn die Variante ein Milchsystem hat.

:::{needextract} PROC_SMOKE
:::

::::
