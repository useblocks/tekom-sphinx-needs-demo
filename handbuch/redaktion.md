# Redaktionsübersicht

Diese Seite richtet sich nicht an die Nutzerin, sondern an die Redaktion. Sie entsteht
vollständig aus den Daten der Anleitung. Hier wird nichts von Hand gepflegt.

Die Anleitung enthält {need_count}`type == "proc"` Handlungsanweisungen, davon
{need_count}`type == "proc" and status == "freigegeben"` freigegeben.

## Bearbeitungsstand

:::{needpie} Handlungsanweisungen nach Status
:labels: Entwurf, Review, Freigegeben

type == "proc" and status == "entwurf"
type == "proc" and status == "review"
type == "proc" and status == "freigegeben"
:::

## Offene Entwürfe

:::{needtable}
:filter: status == "entwurf"
:columns: id, title as "Titel", autor as "Autor"
:style: table
:sort: id
:::

## Wo steht welcher Warnhinweis?

Die Liste entsteht aus den Verknüpfungen der Handlungsanweisungen. Sie nennt jede
Anweisung, für die ein Hinweis gilt, nicht nur das Kapitel.

:::{needtable}
:filter: type == "warn"
:columns: title as "Warnhinweis", signalwort as "Signalwort", warns_back as "gilt für"
:style: table
:sort: title
:::

## Begriffe ohne Verwendung

Glossarbegriffe, die in keiner Handlungsanweisung erwähnt werden.

:::{needtable}
:filter: type == "term" and len(mentions_back) == 0
:columns: title as "Begriff", id
:style: table
:filter_warning: Jeder Begriff wird mindestens einmal erwähnt.
:::

## Gefährdungen aus der Risikobeurteilung

Die folgenden Gefährdungen stammen aus dem Projekt der Risikobeurteilung und werden
als Datei importiert.

:::{needimport} gefaehrdungen
:filter: type == "hazard"
:::

## Abdeckung der Gefährdungen

Jede Gefährdung muss von mindestens einem Warnhinweis abgedeckt sein. Die Regel steht
in `schemas.json` und wird bei jedem Build geprüft.

:::{needflow} Warnhinweise und Gefährdungen
:filter: type in ["warn", "hazard"]
:link_types: covers
:config: lefttoright
:::

## Brücke zum Entwicklungsprojekt

Dieselbe Maschine wird im Projekt der Softwareentwicklung dokumentiert. Wo es dort eine
Entsprechung gibt, ist sie hier verknüpft. Wo keine steht, bleibt die Tabelle leer.
Die leeren Zeilen sind der interessante Teil.

:::{needtable}
:filter: type == "feature"
:columns: id, title as "Merkmal", realisiert_durch as "Im Entwicklungsprojekt"
:style: table
:sort: title
:::

Umgekehrt weiß das Entwicklungsprojekt nichts von Mahlwerk, Milchsystem oder
Entkalkungsprogramm. Beide Seiten beschreiben dasselbe Produkt und wissen
Unterschiedliches darüber.
