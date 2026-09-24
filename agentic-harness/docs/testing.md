# Testing – Verhalten und Teststruktur

**Zuständigkeit:** Testauswahl, Layout und Isolation. Aktuelles Gate: `agentic-harness/harness/project.md`; Abschlussregel: `agentic-harness/harness/verification/gate.md`. Herkunft: `agentic-harness/harness/adoption-log.md`.

Felix bestätigt fachliches Verhalten in Alltagssprache; der Agent plant, schreibt, prüft und berichtet Tests. Vor testwürdigem Verhalten kurz klären: **Aufgabe → Normalfall → relevanter Fehlerfall → unveränderter Zustand**. Geplante Fälle Felix vor Testcode zeigen, vorhandene Tests sichten. Keine Erwartungen aus dem aktuellen Code erfinden, keine Tests für leere Platzhalter oder Quoten.

## Ist und Soll

- **Ist:** pytest in flachem `tests/`; feste Zeitpunkte für Domäne/Manager, kontrollierte Uhr und echte Button-Klicks für Desktop. Qt-Tests headless mit `QT_QPA_PLATFORM=offscreen`. `tests/test_break_period.py` ist leer.
- **Bei der src-Migration:** Tests nach `tests/domain/`, `tests/application/`, `tests/ui/` den jeweiligen öffentlichen Grenzen zuordnen; leere Testdatei entfernen. Domäne und Anwendung ohne Qt importierbar/testbar halten. UI-Tests dürfen Qt benötigen; keine Testpfade als Import-Hack verwenden. Nach `pip install -e .` Import und Testentdeckung auch außerhalb des Repo-Roots prüfen.
- **Später:** Persistenz mit temporärer echter Datenbank testen, wenn vorhanden; wenige End-to-End-Abläufe erst bei stabiler Anwendung. Offscreen ersetzt keine interaktive Desktop-Sichtprüfung.

## Ausführung und Fehler

Standard: Verhalten vereinbaren → implementieren → fokussierte Tests planen/schreiben → engsten Test und vollständiges Gate ausführen. TDD nur auf Wunsch; bei Bugfix möglichst erst ein reproduzierender Regressionstest. Tests über öffentliche APIs, unabhängig und deterministisch halten; genaue Ausnahmen und unveränderten Zustand bei abgelehnten Aktionen prüfen. Gültige Tests nicht für Grün abschwächen.

Bei Fehlschlag `SPEC` (Soll), `CODE`, `CHECKER` oder `HARNESS` (Umgebung) unterscheiden; Vorgehen: `agentic-harness/harness/verification/fail.md`. Tatsächlich ausgeführte Befehle, Resultate und nicht abgedeckte Risiken melden. Ein Build, eine leere Suite oder Ruff allein beweist kein Nutzerverhalten.
