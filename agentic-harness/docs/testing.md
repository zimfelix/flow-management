# Testing – Flow Management

**Zuständigkeit:** Welche Verhaltensprüfungen sinnvoll sind, wie sie geplant werden und was ein Fehlschlag bedeutet. Der konkrete Gate-Befehl und sein Status stehen in `agentic-harness/harness/project.md`; Abschlussregeln in `agentic-harness/harness/verification/gate.md`.

> **Herkunft:** Vorlage `3c936a1`: Testing-Platzhalter; `b80b873`: bisheriger projektbezogener Test-Workflow; `2bfac53`: Desktop-Widget-Tests. Danach verdichtet und von tatsächlich eingerichteten Engineering-Checks abgegrenzt. Siehe `agentic-harness/harness/adoption-log.md`.

## Verantwortung und Ablauf

Felix bestätigt fachliches Verhalten in Alltagssprache, nicht pytest-Syntax. Der Agent schlägt passende Fälle vor, schreibt und prüft die Tests und berichtet Ergebnisse und Lücken. Offene Produktentscheidungen werden nicht aus dem aktuellen Code als Soll abgeleitet.

Bei testwürdigem Verhalten vor dem Testcode kurz klären: **Aufgabe → Normalfall und Ergebnis → relevanter Fehler-/Grenzfall → was unverändert bleibt**. Bestehende Tests sichten; Fälle zu Vertrag, Rückgabewerten, Mutationen und Fehlern zuordnen und Felix in Alltagssprache vorlegen. Keine Tests für leere Platzhalter, Formatierung oder bloße Quoten. Bei unklarem Soll zuerst entscheiden, nicht Erwartungen erfinden.

Standard bei neuen Features: Verhalten vereinbaren → implementieren und verstehen → Testfälle abstimmen → Tests schreiben. TDD nur auf ausdrücklichen Wunsch. Bei Bugfixes nach Möglichkeit zuerst einen reproduzierenden Regressionstest. Einen kritischen Test bei Bedarf durch temporären kleinen Fehler auf Sensitivität prüfen, wiederherstellen und erneut ausführen.

## Testebenen und konkrete Praxis

- **Domäne (Standard):** eine öffentliche Operation mit Normalfall, passendem Fehler und unverändertem Zustand prüfen; zusammenhängende Abläufe gezielt ergänzen. Feste Datums-/Zeitwerte, keine unnötigen Mocks.
- **Desktop-Adapter (aktiv):** echte Button-Klicks und sichtbaren Widget-Zustand mit injizierter kontrollierter Uhr prüfen; für headless Tests `QT_QPA_PLATFORM=offscreen`. Das ersetzt **keine** visuelle/interaktive Prüfung auf einem Desktop. `tests/test_desktop_ui.py` deckt einen ersten Ablauf ab; `tests/test_break_period.py` ist leer.
- **Später, wenn vorhanden:** Persistenz mit temporärer echter SQLite-Datenbank statt Mock-Ketten prüfen; wenige vollständige UI-/Daten-Workflows, wenn diese Schnittstellen stabil sind. Nicht alle Ebenen für jede Änderung verlangen.

Tests bleiben unabhängig, beschreiben extern sichtbares Verhalten über öffentliche APIs, benennen einen Zweck und prüfen relevante exakte Fehlertypen. Bei abgewiesenen Mutationen den bisherigen Zustand prüfen; Objektidentität prüfen, wenn sie zum Vertrag gehört. Keine gültigen Tests löschen, abschwächen oder skippen, um grün zu werden.

## Ausführung und Fehler

Erst den engsten betroffenen Test, dann das vollständige Gate aus `agentic-harness/harness/project.md` ausführen, soweit praktikabel. Nur **eingerichtete und tatsächlich ausgeführte** Checks als bestanden melden. Ruff, Typchecker, Lockfile und CI sind noch keine aktiven Checks; vorgeschlagene Qualitätswerkzeuge stehen in `agentic-harness/docs/code.md`.

Bei Fehlschlag zuerst Ursache klassifizieren: `SPEC` (Soll unklar/falsch), `CODE` (gültiges Soll verletzt), `CHECKER` (Test/Check prüft falsch), `HARNESS` (Umgebung/Entdeckung/Ausführung). `agentic-harness/harness/verification/fail.md` beachten; Produktionscode nicht für einen falschen Checker verbiegen. Ergebnis kurz berichten: Verhalten und Testfälle, ausgeführte Befehle mit Resultat, nicht abgedeckte Risiken. Ein bestandener Build oder eine leere Testsuite beweisen keine Nutzerfunktion.
