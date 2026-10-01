# Lernstand – Agentic Harness V3 im Flow-Management-Test

**Zuständigkeit:** Lokaler Zwischenspeicher für Erkenntnisse aus diesem Harness-Test. Kein Produkt-Backlog und keine Änderung der globalen Agentenregeln oder der Vorlage in `../agentic-harness-v3/`. Die verbindlichen Anpassungen der Testkopie stehen in `agentic-harness/harness/init.md` und den zuständigen Projektdokumenten; Herkunft unter `agentic-harness/harness/adoption-log.md`.

> **Herkunft:** Angelegt in `2ba1579`; Änderungen an diesem Lernstand: `agentic-harness/harness/adoption-log.md`. Bestätigtes und offene Hypothesen bleiben getrennt.

## Ziel des Versuchs

```text
1. Schwächen der bestehenden Harness-Vorlage an Flow Management erkennen
   → 2. anhand der Erkenntnisse den Agentic Harness gezielt verbessern
   → 3. den verbesserten Harness in einem weiteren Testprojekt erproben
```

Erst die Testkopie in diesem Repository präzisieren und hier erneut an Feature-/Refactor-Arbeit erproben. Die eigenständige Vorlage `../agentic-harness-v3/` bleibt vorerst unverändert; eine spätere Übernahme erfordert Prüfung und ausdrücklichen Auftrag. Das Ziel ist ein übertragbarer Init für bestehende ebenso wie für neue Projekte, nicht ein auf Flow Management zugeschnittener universeller Core.

## Bestätigte Beobachtungen aus dem ersten Durchlauf

- Der bisherige Init prüfte vorhandenen Code, Tests und ersten Ablauf, forderte aber **keinen expliziten Vergleich von Produktvision, technischer Zielarchitektur und vorhandenem Code**. Dadurch wurde der Ist-Zustand gut dokumentiert, ohne den gewünschten professionellen Zielzustand und Modernisierungsbedarf vor der Implementierung zu klären.
- `agentic-harness/docs/architecture.md` beschrieb hauptsächlich bestehende Domänenklassen und den neuen Desktop-Adapter. Das war keine abgestimmte Zielarchitektur. `agentic-harness/docs/code.md` nannte Heuristiken, aber keinen gewählten, überprüfbaren Qualitätsstandard für das Projekt.
- Ein PySide6-Prototyp wurde ergänzt, bevor Zuständigkeit für app-weiten Zustand, Datenlebensdauer, UI-Hintergrundverhalten, Zielplattform und Refactor-Reihenfolge durchgängig geklärt waren. `DesktopWindow` hält derzeit `WorkDay`-Objekte und aktiven Zustand; `FlowManager` ist ungenutzt. Die 23 erfolgreichen Tests belegten den aktuellen Prototyp, **nicht** dessen architektonische Eignung oder die visuelle Bedienbarkeit.
- Die vorhandene Test-Doku war deutlich ausführlicher als der konkrete Engineering-Einstieg: `docs/testing.md` (im Harness) hatte ca. 170 Zeilen, aber Format-/Lint- und Typprüfungen, reproduzierbare Abhängigkeiten und CI waren weder entschieden noch als aktive Checks eingerichtet. Viele Worte ersetzen keinen durchlaufenen Qualitätscheck.
- Der Harness unterscheidet korrekt zwischen Ist, geplant und offen. Diese Trennung muss erhalten bleiben: Professionelle Tools sind proportional auszuwählen, nicht als pauschales Pflichtpaket oder bereits installierte Fakten zu erfinden.
- Ein früher Dialog fragte Init-Fragen nacheinander. Felix bevorzugt einen gebündelten Fragenblock und anschließende autonome Ableitung aus seinen Antworten, mit Nachfragen nur bei blockierenden fachlichen Entscheidungen. Diese Regel ist bereits in der Testkopie von `init.md` ergänzt.

## Präzisierung, die dieser Testkopie hinzugefügt wird

Bei **bestehendem Code vor weiterer Produktimplementierung**: (1) Nutzerproblem, Ziel und gewünschte Phasen von der vorhandenen Implementation trennen; (2) Soll-Bausteine, Zuständigkeiten, Datenfluss, Persistenz-/Betriebsgrenzen und angemessene Engineering-Checks für den ersten Schritt vorschlagen; (3) den Ist-Code samt Tests gegen dieses Soll bewerten; (4) konkrete Lücken und riskante Annahmen benennen; (5) einen kleinen priorisierten Modernisierungsschritt vor oder zusammen mit dem nächsten Feature vereinbaren. Für neue Projekte gilt derselbe Ziel- und Qualitätscheck ohne Bestandsanalyse. Begründete Empfehlungen als **Kandidat** markieren, bis entschieden; spätere Technik nur als Entscheidungspunkt dokumentieren.

Professionell bedeutet hier überprüfbare Standards und saubere Verantwortungsteilung, nicht automatisch ein großes Framework. Beispielkandidaten zur Prüfung: `pyproject.toml` und reproduzierbare Abhängigkeiten, Ruff für Lint/Format, ein Typchecker, pytest plus CI; für lokale Speicherung SQLite (eine SQL-Datenbank), für spätere Web-Auswertung eine bedarfsabhängige Web-API oder serverseitige Oberfläche und für Analyse später pandas/Notebooks. Die konkreten Tools, Versionen und Gates sind **noch nicht freigegeben oder eingerichtet**; diese Liste ist ein Vergleichsrahmen, keine Stack-Entscheidung.

Dokumentationsregel: universeller Entscheidungsablauf in `harness/init.md`, bestätigte Projektrichtung in `harness/project.md`, Ist/Soll/Abstand in `docs/architecture.md`, geltende gegenüber vorgeschlagenen Checks in `docs/code.md` und `docs/testing.md`, ausführliche Lernerkenntnisse hier. Keine Gesprächsprotokolle in den Core kopieren. Herkunft der Markdown-Änderungen weiter in `harness/adoption-log.md` nachführen.

## Bestätigter zweiter Befund: Strukturentscheidung ohne Strukturabgleich

Felix erlaubte zunächst eine vollständige Umstrukturierung und verlangte eine Struktur für spätere Features; ein `src/`-Layout war dabei noch **nicht ausdrücklich vorgegeben**. Nach der Umsetzung bestätigte er ein installierbares Python-Paket unter `src/` mit Domänen-, Anwendungs- und Desktop-Modulen sowie gegliederten Tests als das gemeinte Ziel. Der Agent behielt `backend/`, `frontend/` und eine flache Testsuite bei, ohne den konkreten Ziel-Dateibaum vorher abzugleichen, obwohl ein größerer Refactor erlaubt war. `agentic-harness/harness/project.md` wurde vor der Umsetzung für diesen verkleinerten Umfang als abgeschlossen behandelt. Ursache ist **nicht**, dass `src/` universell professioneller wäre, sondern dass der vereinbarte **gewünschte Strukturumfang nicht als prüfbares Ergebnis gegen den tatsächlichen Dateibaum abgeglichen** wurde. „Kleinste passende Änderung“ darf einen beauftragten Strukturwechsel nicht stillschweigend auf einen internen Klassen-Refactor reduzieren.

**In der Flow-Management-Testkopie präzisiert:** `harness/init.md` fordert vor einem Strukturumbau Soll-Dateibaum, Ist-Abgleich, Paketinstallation und Testlayout; `harness/core.md` bindet den beauftragten Umfang, `harness/verification/` prüft beim Abschluss echte Dateien, Imports und Testentdeckung. `docs/architecture.md` enthält den gewünschten `src/flow_management/`-Baum, `docs/code.md` Packaging-Konventionen und `docs/testing.md` das Testlayout. `src/` ist eine **bestätigte Entscheidung dieses Projekts**, keine Pflicht für jedes Projekt. Der Produktcode ist **noch nicht migriert**; die praktische Wirksamkeit der präzisierten Verification bleibt bis zu diesem Refactor offen.

## Dritter Befund: Informationsdichte und Ladegrenzen

Wenig Markdown-Zeilen bedeuten nicht wenig Kontext: In der Testkopie hatten AGENTS, Core, Init und Projektprofil zusammen über 11.000 Zeichen, einzelne Regeln bis zu 820 Zeichen pro Zeile. Das Profil wiederholte Moduldetails/Tests und Chronik; knappe Herkunftstexte in ständig geladenen Dateien verdrängten handlungsrelevante Entscheidungen. Die Eingangsdateien verlinkten zwar thematisch, aber `init.md` wurde nur über `Pending Project Init` geladen; nach Entfernen dieses Status fehlte für ausdrücklich beauftragte Strukturumbauten ein **unabhängiger Abschlussabgleich**.

**In der Testkopie umgesetzt:** Einstiegsdateien auf Aufgabe → relevante Doku begrenzt; Projektprofil auf Grenzen, offene Strukturabweichung und Befehle, Architecture auf Ist/Soll-Baum und Technologien, Code auf Packaging/Code-Konventionen, Testing auf Layout/Tests reduziert. Herkunft als kurzer Verweis ins optionale `harness/adoption-log.md`; der lokale Lernstand bleibt nur für Harness-Aufgaben. Die Verification wurde gezielt um Struktur-Nachweis ergänzt, **nicht** bereits im src-Migrationsdurchlauf erprobt. Aussagekraft anhand eines echten Struktur-Refactors prüfen, statt Wortzahlen als Qualitätsziel einzuführen.

## Offen für den nächsten Durchlauf

- **Offen (Produktentscheidung):** Was bedeutet „im Hintergrund laufen“ für die bedienungsfertige Zielversion konkret – minimiertes Fenster, Tray, Systemstart, Aktivitätserkennung? Wie wichtig ist verlustfreie Speicherung bereits im ersten nutzbaren Meilenstein? Welche Zielplattformen außer der aktuellen macOS-Umgebung?
- **Erprobt (Architekturabgleich):** Der nächste beauftragte Meilenstein ist flüchtig. Nach abgeschlossener Profilklärung koordiniert `FlowManager` Uhr, Tage und Session ohne Qt; das Widget sendet Aktionen und stellt dar. Domänen-, Manager- und Qt-Tests sowie Ruff-Lint/-Formatcheck laufen. Das belegt die konkrete Trennung, nicht bereits die spätere Persistenzarchitektur oder visuelle Bedienbarkeit.
- **Offen (späterer Architekturabgleich):** Datenlebensdauer über Neustarts, Über-Mitternacht-Regel und Zeitzonen vor Speicherung entscheiden; prüfen, ob die Trennung im nächsten Feature Bestand hat.
- **Offen (Engineering):** Python-Mindestversion, installierbares Paket, Abhängigkeitsstrategie und Typprüfung wählen; Ruff-Lint/-Format und pytest sind inzwischen aktiv, ein automatisiertes CI noch nicht. CI erst auf reproduzierbarer lokaler Prüfung aufbauen.
- **Offen (Harness-Test):** Beim nächsten Feature-/Refactor-Durchlauf prüfen, ob Init und Projektprofil nun eine klare Ziel-/Ist-/Lückenentscheidung auslösen und ob die Docs kurz und handlungsrelevant bleiben. Danach im nächsten Testprojekt auf Übertragbarkeit prüfen, bevor Änderungen in die separate Vorlage übernommen werden.
