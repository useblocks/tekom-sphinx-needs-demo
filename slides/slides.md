---
marp: true
theme: useblocks-slides
paginate: true
html: true
backgroundImage: url(assets/ub_Logo.svg)
backgroundPosition: top 30px right 30px
backgroundRepeat: no-repeat
backgroundSize: 150px
style: |
  /* Nur fuer diesen Vortrag. Das Firmentheme kommt aus useblocks-slides.css.
     Stichpunkte erscheinen als Bloecke, wie es das PowerPoint-Master
     vorgibt ("use blocks like these", gefuellte roundRects in #404040). */
  section ul {
    display: flex;
    flex-direction: column;
    gap: 14px;
    flex: 1;
    justify-content: flex-start;
    list-style: none;
    padding: 0;
    margin: 22px 0 0 0;
  }
  section ul > li {
    background: #292929;
    border: 1px solid #404040;
    border-radius: 10px;
    padding: 16px 24px;
    margin: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1 1 auto;
    max-height: 120px;
    font-size: 24px;
    line-height: 1.35;
  }
  /* Die Titelfolie kennt das Firmentheme nicht; sie stammt aus dem ZF-Deck.
     Alle anderen Folien tragen ihre Aussage im Action Title (BP_PRESENTATIONS)
     und nutzen .lead aus dem Baukasten. */
  section.title-slide { padding-top: 175px; }
  section.title-slide h1 {
    position: static;
    text-align: center;
    /* Das Theme deckelt H1 auf 960px. Auf der Titelfolie wird sonst innerhalb
       dieser 960px zentriert, also 120px links neben der Folienmitte. */
    width: 100%;
    max-width: none;
    font-size: 52px;
    margin: 0 0 12px 0;
  }
  section.title-slide h2 { text-align: center; font-size: 30px; color: #E4FF3D; }
  section.title-slide h3 { text-align: center; font-size: 18px; color: #656565; }
  .title-divider {
    width: 80px; height: 4px; background-color: #E4FF3D;
    margin: 18px auto; border: none; border-radius: 2px;
  }
  /* Problemfolie und Loesungsfolie sollen ohne Lesen unterscheidbar sein.
     Das Badge der Problemfolie bleibt in der Palette, aber gedaempft. */
  .badge.problem { background-color: #404040; color: #FFFFFF; }

  /* Interaktionsfolien sind im Ablauf erkennbar: hier redet das Publikum. */
  section.interaktion { background-color: #23261A; }
  section.interaktion h1 { color: #E4FF3D; }
---

<!--
Sprechernotizen stehen in diesen Kommentaren und erscheinen nur im Presenter-Modus.
Die Zeitmarken beziehen sich auf den Ablaufplan des Vortrags.
Alles Sichtbare passiert im Live-Projekt, nicht auf den Folien.

Quelltext: zeigen, nicht erklären. Pro Folie höchstens zwei Stellen. Auf ID,
Feldnamen und Verknüpfung zeigen, nie auf Doppelpunkte oder Klammern.
"md" ist eine Seite des Handbuchs, "daten" eine Datendatei, "config" eine
Konfigurationsdatei. Config kommt nur an drei Stellen vor: die Typen (Prinzip),
die Regeln (Baustein 2 und Brücke), die Anbindung ans Entwicklungsprojekt (Brücke).
Zeilenangaben gelten für den jeweils ausgecheckten Stand.
-->

<!-- _class: title-slide -->

# Docs as Code für Fortgeschrittene

## Das Potenzial von Sphinx-Needs

<div class="title-divider"></div>

### tekom-Online-Event · Stefan Schulz, Head of Solution Engineering · useblocks GmbH

<!--
Terminal vor dem Start:
  git checkout -f stand-00-ohne-needs
  make live          # Vorschau auf http://localhost:8000, baut bei jeder Änderung neu

Jeder Wechsel im Vortrag läuft mit -f. Das verwirft, was live geändert wurde,
auch die Datei, die make hazards schreibt. Ohne -f bricht ein späterer Wechsel ab
oder nimmt eine Änderung still in den nächsten Stand mit.

0-5 Ankommen.
Begrüßung, ein Satz zur Reihe.
Vorstellung auf der Tonspur, ohne eigene Folie: Werkzeugentwickler,
hauptsächlich im Automotive-Umfeld. Bei useblocks Head of Solution
Engineering, mein Team rollt unsere Docs-as-Code-Werkzeuge beim Kunden aus.
Dafür 30 Sekunden, nicht mehr.
Danach weiter zur Chatfrage auf der nächsten Folie, sie bleibt während der
Vorstellung stehen.
-->

---

<!-- _class: interaktion -->

<span class="badge">Interaktion</span>

# Wo pflegen Sie heute Ihre Warnhinweise?

Copy-Paste · Textbausteine im Redaktionssystem · anders

**Antworten bitte in den Chat.**

<!--
0-5, steht während des Ankommens und der Vorstellung auf der Tonspur.
Frage stellen, offen lassen, Antworten mitlesen. Zwei laut vorlesen,
nicht kommentieren. Darauf beziehst du dich in Baustein 2 und im Ideenraum
zurück.
-->

---

<span class="badge">Vorstellung</span>

# Sphinx-Needs kommt aus dem Engineering

- Erweiterung für Sphinx, seit 2016 offen entwickelt, MIT-Lizenz
- Gebaut, um Anforderungen, Spezifikationen und Tests nachzuverfolgen, etwa nach ISO 26262
- Heute wenden wir dasselbe auf ein Benutzerhandbuch an

<!--
30 Sekunden, nicht mehr.
Die Herkunft offen nennen: Das Werkzeug ist für sicherheitskritische Entwicklung
gebaut, und die Dinge, die es dort leistet, fehlen der Redaktion genauso.
useblocks entwickelt es, das reicht als Erwähnung; die Firma kommt am Ende
noch einmal vor.
Quelle der Angaben: sphinx-needs.readthedocs.io und github.com/useblocks/sphinx-needs
-->

---

<span class="badge problem">Das Prinzip · Problem</span>

# Derselbe Warnhinweis steht viermal im Quelltext

- Jede Änderung muss in jeder Kopie nachgezogen werden
- Der Bearbeitungsstand liegt in einer Tabelle daneben
- Bei "Heißwasser beziehen" fehlt der Hinweis zu heißen Oberflächen

<!--
Terminal:
  git checkout -f stand-00-ohne-needs

5-12 Das Prinzip.
Warnhinweis viermal im Quelltext zeigen, Excel-Ersatz in redaktion.md zeigen.
Dann zubereitung.md: Bei "Kaffeestärke wählen" steht der Hinweis zu heißen
Oberflächen, bei "Heißwasser beziehen" fehlt er. Die Tabelle in redaktion.md nennt
nur Kapitel, sie kann das nicht zeigen. Diese Stelle kommt in Baustein 2 zurück.
Nicht über Syntax reden.

Code zeigen:
  md  sicherheit.md:9 neben inbetriebnahme.md:5, derselbe Stromschlag-Text zweimal
  md  zubereitung.md:5 Hinweis bei "Kaffeestärke", zubereitung.md:31 "Heißwasser"
      ohne Hinweis
  md  redaktion.md, die Tabelle von Hand, nur überfliegen
Keine config. Hier ist noch alles gewöhnliches Markdown.
-->

---

<span class="badge">Das Prinzip · Lösung</span>

# Ab jetzt ist dieser Absatz adressierbar

<div class="lead">Ein relevanter Absatz bekommt einen Typ, eine ID und ein paar Felder. Er bleibt Text im Dokument, und alles Weitere heute folgt aus diesem einen Schritt.</div>

<!--
Terminal:
  git checkout -f stand-01-anweisungen

Dieselbe Datei wie eben, zubereitung.md: Aus dem Abschnitt "Kaffeestärke wählen"
ist ein proc mit einer ID geworden. Daneben die gebaute Seite: Der Text ist derselbe,
er steht jetzt in einem Rahmen mit Typ und ID. Zeigen, nicht erklären, nicht über
Syntax reden.
Das ist die einzige Begriffsdefinition des Vortrags. Kernsatz: Ab jetzt ist dieser
Absatz adressierbar.
In diesem Stand sind nur die Handlungsanweisungen Needs. Glossar und Warnhinweise
liegen unverändert daneben, beide kommen später dran.

Code zeigen:
  md      zubereitung.md:10 bis :11, ":::{proc} Kaffeestärke wählen" und
          ":id: PROC_STAERKE". Zwei Zeilen, mehr ist nicht neu.
  config  ubproject.toml:48 bis :53, der Block [[needs.types]] für proc.
          Ein Satz: "Welche Arten von Objekten es gibt, steht einmal hier."
Nicht zeigen: conf.py.
-->

---

<!-- _class: interaktion -->

<span class="badge">Interaktion</span>

# Welches Objekt würden Sie als Erstes zu einem Need machen?

**Chat oder Mikrofon, beides geht.**

<!--
12-17 Interaktion.
Sammeln, nicht kommentieren. Die Antworten sind dein Material für den Ideenraum
am Ende. Notiere zwei oder drei mit.
-->

---

<span class="badge problem">Baustein 1 · Problem</span>

# Wer einen Begriff umbenennt, sucht ihn heute im Volltext

- Das Glossar wird von Hand gepflegt und altert
- Wo ein Begriff überall steht, weiß nur die Volltextsuche
- Niemand merkt, wenn ein Begriff nirgends mehr vorkommt

<!--
Kein Terminal, stand-01-anweisungen steht noch.

17-30 Baustein 1.
Kein Quelltext, nur die gebaute Seite: In "Kaffeestärke wählen" ist "Bypass" ein
Link ins Glossar. Auf der Glossarseite steht aber nirgends, wo der Begriff
vorkommt. Der Hinweg ist da, der Rückweg fehlt.

Code zeigen: nichts. {term} gegen {need} zu vergleichen wäre schon Syntax.
-->

---

<span class="badge">Baustein 1 · Lösung</span>

# Das Glossar pflegt seine Rückwege selbst

<div class="lead">Auf dem Eintrag steht, in welchen Kapiteln der Begriff vorkommt. Gepflegt hat das niemand.</div>

<!--
Terminal:
  git checkout -f stand-02-glossar

Begriff einmal definieren, im Text referenzieren. Das Begriffsverzeichnis am Ende
der Seite und die Rückverweise entstehen von selbst.
Der Aha-Moment. Auf GLOSS_BRUEHGRUPPE zeigen: vier Einträge unter
"wird erwähnt in".
Zur dritten Problemzeile: Kommt ein Begriff nirgends mehr vor, bleibt die Zeile
leer. Ab Stand 04 listet die Redaktionsübersicht solche Begriffe eigens auf.
Nebenbei: In reinigung.md steht "des Milchsystems". Die Rolle nimmt einen eigenen
Text, die Verknüpfung bleibt. Flexion ist kein Hindernis.
Frage in den Raum: Wer hat schon einmal einen Begriff umbenannt und
danach gesucht, wo er überall stand?

Code zeigen, beide Dateien nebeneinander:
  md  glossar.md:5 bis :10, der Eintrag Brühgruppe mit ":id: GLOSS_BRUEHGRUPPE"
  md  zubereitung.md:20, im Fließtext steht dieselbe ID
Dann sofort zur gebauten Glossarseite, "wird erwähnt in".
Nur auf Nachfrage: reinigung.md:42 "des Milchsystems" für die Flexion,
ubproject.toml:71 [needs.links.mentions] für die Frage, woher die
Rückverweise kommen.
-->

---

<span class="badge problem">Baustein 2 · Problem</span>

# Jede Änderung am Hinweis muss in vier Kopien nachgezogen werden

- Derselbe Hinweis steht an vier Stellen im Handbuch
- Der Redaktionsleitfaden verlangt ein Signalwort, geprüft wird es nie
- Ob ein Hinweis überall steht, wo er gilt, zeigt keine Liste

<!--
Kein Terminal, stand-02-glossar steht noch. Die Warnhinweise sind hier
noch kopiert.

30-45 Baustein 2.
Den Hinweis zum Stromschlag in sicherheit.md, inbetriebnahme.md, reinigung.md
und entkalken.md zeigen: viermal derselbe Text, viermal von Hand gepflegt.
Das Signalwort steckt nur im Titel der Admonition, niemand prüft es.

Code zeigen:
  md  sicherheit.md:9 neben reinigung.md:3, derselbe Text, zweimal gepflegt
Keine config.
-->

---

<span class="badge">Baustein 2 · Lösung</span>

# Der Warnhinweis hat eine Quelle und weiß, wo er gilt

<div class="lead">Geändert wird an einer Stelle, alle Verwendungsstellen folgen. Jede Handlungsanweisung nennt ihre Hinweise.</div>

<!--
Terminal:
  git checkout -f stand-03-warnhinweise

Eine Quelle, vier Verwendungsstellen. Live den Hinweis ändern, Seite neu laden,
Änderung erscheint überall.
Das Signalwort steht jetzt im Kopf des Hinweises, weil es ein eigenes Feld ist.
Der Pfeil rechts am Hinweis klappt auf, wofür er gilt ("gilt für").
Zurück zu "Heißwasser beziehen": Der Hinweis steht jetzt dort. Das war die Stelle
vom Anfang.

Code zeigen:
  md  sicherheit.md:18 bis :26, WARN_OBERFLAECHE mit ":signalwort: VORSICHT".
      Hier live den Text ändern.
  md  zubereitung.md:40 bis :45, bei "Heißwasser" holt ":::{needextract}" den
      Hinweis, und ":warns:" nennt ihn an der Anweisung
Nicht zeigen: den Darstellungsblock in ubproject.toml:77. Nur auf Nachfrage, warum
das Signalwort im Kopf steht.
-->

---

<span class="badge">Baustein 2 · Lösung</span>

# Der Redaktionsleitfaden bekommt Zähne

<div class="lead">Ein Warnhinweis ohne gültiges Signalwort lässt den Build scheitern.</div>

<!--
Terminal für den Fehlerfall:
  make check         # bricht ab, sobald das Signalwort ungültig ist

In sicherheit.md ein Signalwort kaputt machen, etwa "Vorsicht" statt "VORSICHT",
bauen lassen, Meldung vorlesen. Sie steht auf Deutsch in schemas.json:
"Jeder Warnhinweis braucht ein Signalwort: GEFAHR, WARNUNG, VORSICHT oder ACHTUNG."
Kurz halten. Zurückbauen ist nicht nötig, der nächste Wechsel verwirft die Änderung:
  git checkout -f stand-04-auswertung

Die Redaktionsübersicht kommt jetzt aus den Daten, die handgepflegte Tabelle vom
Anfang ist gelöscht. Unter "Wo steht welcher Warnhinweis?" steht jetzt jede
Handlungsanweisung, nicht nur das Kapitel. Bei "Heiße Oberflächen" ist
PROC_HEISSWASSER dabei. Genau das konnte die Tabelle vom Anfang nicht zeigen.
Und eine Zeile ist leer: "Verletzungsgefahr am Mahlwerk" gilt für keine
Anweisung. Das stand vorher auch schon so, nur hat es niemand gesehen.

Code zeigen:
  config  schemas.json:11 und :19, auf Stand 03. Nur "message" und die Liste der
          Signalwörter, der Rest ist Gerüst. Der Redaktionsleitfaden als Datei.
  md      sicherheit.md:20, dort das Signalwort kaputt machen
  md      nach dem Wechsel auf Stand 04: redaktion.md:28 bis :38, die Tabelle
          "Wo steht welcher Warnhinweis?". Auf ":filter:" und ":columns:" zeigen,
          das ist das Filtern aus der Ankündigung.
-->

---

<!-- _class: interaktion -->

<span class="badge">Interaktion</span>

# Jetzt Ihre Fragen

Jetzt ist Zeit für das, was bis hierhin offen geblieben ist.

**Chat oder Mikrofon, ich gehe der Reihe nach durch.**

<!--
45-50 Interaktion.
Chat abarbeiten. Wenn nichts kommt: die Antworten aus der Einstiegsfrage
aufgreifen und eine davon auf das Gezeigte beziehen.
-->

---

<span class="badge problem">Baustein 3 · Problem</span>

# Drei Varianten, drei kopierte Handbücher

- Compact hat kein Milchsystem, die Anleitung dazu steht trotzdem drin
- Technische Daten weichen ab und werden von Hand nachgezogen
- Jede Korrektur ist dreimal Gelegenheit, eine zu vergessen

<!--
Terminal:
  git checkout -f stand-05-varianten
  make alle-varianten   # _build/pro, _build/plus, _build/compact

50-65 Baustein 3.
Für dieses Problem gibt es keinen Vorher-Stand im Repo. Es auf der Tonspur
schildern, jeder im Publikum kennt es.
Merkmale als Needs, Ausstattungsliste je Variante.

Code zeigen: nichts, das Problem kennt das Publikum.
-->

---

<span class="badge">Baustein 3 · Lösung</span>

# Eine Quelle, drei konfigurierbare Handbücher

<div class="lead">Im Compact fehlt alles zum Milchsystem. Technische Daten und Ausstattungstabelle stimmen von selbst.</div>

<!--
Der stärkste rein visuelle Moment:
zweimal bauen, beide Handbücher nebeneinander legen.
Im Compact fehlen der Abschnitt "Milchgetränke" und "Milchsystem reinigen"
vollständig, die technischen Daten stimmen, die Ausstattungstabelle auch.
Sicherheitshinweise und Glossar gelten für die Baureihe und bleiben bewusst stehen.

Code zeigen:
  daten  _data/varianten/compact.json, ganz. Das ist die Variante: "milchsystem":
         false, Tank 1,4 l. Kein Code, eine Datenliste.
  md  zubereitung.md:25, "::::{if} var.ausstattung.milchsystem" vor dem
      Abschnitt Milchgetränke
  md  varianten.md:10, der Tank als {variant}`technik.tankvolumen` in der Tabelle
Nicht zeigen: conf.py:22 und den Filter in varianten.md:18. Den Aufruf mit -D
sieht man im Terminal bei make alle-varianten.

Falls jemand fragt, warum die Ausstattung zweimal steht (JSON-Datei und
has_features am Variant-Need): Die JSON-Datei steuert, was in den Bau kommt.
Die Variant-Needs beschreiben die ganze Baureihe, auch die Varianten, die gerade
nicht gebaut werden. Dass beide übereinstimmen, prüft heute niemand, und genau
dort würde man als Nächstes eine Regel ergänzen.
-->

---

<span class="badge problem">Die Brücke · Problem</span>

# Wer prüft, dass zu jeder Gefährdung ein Warnhinweis existiert?

- Die Gefährdungen entstehen in der Entwicklung
- Die Warnhinweise entstehen in der Redaktion
- Dazwischen liegt heute ein PDF-Anhang und ein Review-Termin

<!--
Terminal:
  git checkout -f stand-06-bruch
  make hazards       # Risikobeurteilung bauen, Gefährdungen ins Handbuch kopieren
  make check         # meldet die unabgedeckte Gefährdung

65-75 Die Brücke.
Import als Datei, nicht als PDF-Anhang. Build meldet: zu HAZ_UEBERLAUF fehlt
der Warnhinweis. In der Redaktionsübersicht das Diagramm zeigen: Jeder Hinweis
zeigt auf seine Gefährdung, HAZ_UEBERLAUF steht allein.
Live beheben: in sicherheit.md einen sechsten warn mit covers: HAZ_UEBERLAUF
anlegen, grün.
Ehrliche Grenze, falls jemand nachfragt: Die Regel prüft, dass es einen Hinweis
gibt, nicht an welcher Stelle er steht. Im Endstand gilt er für alle drei Bezüge.
Weiter zum Endstand, der Wechsel verwirft den Live-Fix:
  git checkout -f stand-07-final

Code zeigen:
  md      risikobeurteilung/index.md:48 bis :53, HAZ_UEBERLAUF im anderen Projekt
  md      redaktion.md:56, ":::{needimport} gefaehrdungen". Eine Zeile holt die
          Liste, kein Pfad, kein PDF.
  config  schemas.json:56 bis :58, auf Stand 06. Nur Name und "message" der Regel,
          die Meldung im Terminal ist genau dieser Satz.
  md      Live-Fix: sicherheit.md:49 bis :56, WARN_MAHLWERK kopieren, ID, Titel und
          ":covers: HAZ_UEBERLAUF" anpassen

Fertiger Hinweis zum Einfügen am Ende von sicherheit.md (so steht er auf Stand 07):

:::{warn} Verbrühungsgefahr durch überlaufendes Getränk
:id: WARN_UEBERLAUF
:signalwort: VORSICHT
:covers: HAZ_UEBERLAUF

Starten Sie einen Bezug nur mit einem ausreichend großen, hitzebeständigen Gefäß.
Läuft das Getränk über, kann heiße Flüssigkeit über die Tassenablage laufen.
:::
-->

---

<span class="badge">Die Brücke · Lösung</span>

# Dieselbe Maschine, andere Domäne

<div class="lead">Dieselben 85 bis 95 °C, dieselben drei Kaffeestärken. Einmal als Handbuch, einmal als Anforderung.</div>

<!--
Schwesterprojekt öffnen: github.com/useblocks/sphinx-needs-demo, docs/coffee-machine/.
Ein Satz: beide Seiten beschreiben dasselbe Produkt und wissen Unterschiedliches
darüber. Das Handbuch kennt Mahlwerk und Entkalkung, drüben steht davon nichts.
In der Redaktionsübersicht die Tabelle "Brücke zum Entwicklungsprojekt": Nur die
Kaffeestärken haben drüben eine Entsprechung (SWREQ_BREW_STRENGTH). Die leeren
Zeilen sind die Aussage.
ubCode läuft nur als schnellere Vorschau mit, kein Produktblock.

Code zeigen:
  config  ubproject.toml:218 bis :221, [[needs.external_needs]]. Eine Datei aus dem
          anderen Projekt, mehr Kopplung gibt es nicht.
  md      varianten.md:26 bis :28, FEAT_KAFFEESTAERKE mit
          ":realisiert_durch: SWREQ_BREW_STRENGTH". Eine ID aus der Entwicklung
          im Handbuch.
Ein Satz zu den Anbindungen an Jira, Codebeamer und Azure DevOps reicht.
-->

---

<!-- _class: interaktion -->

<span class="badge">Interaktion</span>

# Was würden Sie in Ihrer Dokumentation zu einem Objekt machen?

<!--
75-90 Ideenraum und Q&A.
Starte mit drei eigenen Ideen, dann öffnen. Vorrat, falls es stockt:
Übersetzungsstatus je Informationseinheit · Screenshot-Inventar ("was muss ich
nach dem Redesign neu machen?") · Marktzulassungen je Land · Schulungsunterlagen
aus denselben Bausteinen · Ersatzteilkataloge · Personas mit ihren Kapiteln ·
Prüfprotokolle · Redaktionsleitfaden-Regeln als prüfbare Objekte.
-->

---

<span class="badge">Links</span>

# Zum Weiterlesen

- Sphinx-Needs: <https://sphinx-needs.readthedocs.io>
- Dieses Demo-Projekt: <https://github.com/useblocks/tekom-demo>
- Dieselbe Maschine aus Entwicklungssicht: <https://github.com/useblocks/sphinx-needs-demo>
- Weiterführende Beispiele: <https://x-as-code.useblocks.com/index.html>
- ubCode: <https://ubcode.useblocks.com>

<!--
Diese Folie wird als PDF verteilt. Links vorlesen ist unnötig, aber sagen,
dass es sie gibt.
-->
