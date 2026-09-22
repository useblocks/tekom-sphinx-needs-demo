# Redaktionsübersicht

Diese Seite richtet sich nicht an die Nutzerin, sondern an die Redaktion. Sie entsteht
vollständig aus den Daten der Anleitung — hier wird nichts gepflegt.

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
