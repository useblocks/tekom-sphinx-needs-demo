# Reinigung

:::{needextract} WARN_NETZ
:::

:::{proc} Tresterbehälter leeren
:id: PROC_TRESTER
:status: freigegeben
:autor: M. Brandt
:geprueft_am: 2026-04-28

1. Öffnen Sie die Servicetür an der rechten Geräteseite.
2. Ziehen Sie den {need}`GLOSS_TRESTERBEHAELTER` zusammen mit der Restwasserschale
   heraus.
3. Entleeren Sie beide, spülen Sie sie aus und setzen Sie sie wieder ein.

Das Gerät meldet den vollen Behälter nach zwölf Portionen.
:::

:::{needextract} WARN_OBERFLAECHE
:::

:::{proc} Brühgruppe spülen
:id: PROC_BRUEHGRUPPE
:status: freigegeben
:autor: M. Brandt
:geprueft_am: 2026-04-28
:warns: WARN_OBERFLAECHE, WARN_NETZ

1. Schalten Sie das Gerät aus und lassen Sie es abkühlen.
2. Entnehmen Sie die {need}`GLOSS_BRUEHGRUPPE` über die Servicetür.
3. Spülen Sie sie unter fließendem Wasser ohne Spülmittel und lassen Sie sie
   abtropfen.
:::

::::{if} var.ausstattung.milchsystem

:::{needextract} WARN_DAMPF
:::

:::{proc} Milchsystem reinigen
:id: PROC_MILCHSYSTEM
:status: review
:autor: S. Ostermann
:requires: FEAT_MILCHSYSTEM
:warns: WARN_DAMPF

1. Starten Sie nach jedem Milchbezug das Spülprogramm des {need}`Milchsystems <GLOSS_MILCHSYSTEM>`.
2. Zerlegen Sie den Aufschäumer einmal wöchentlich.
3. Reinigen Sie die Einzelteile in warmem Wasser und setzen Sie sie trocken wieder
   zusammen.
:::

::::
