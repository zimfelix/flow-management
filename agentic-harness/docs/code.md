# Code – projektbezogene Codekonventionen

**Zuständigkeit:** Dauerhafte Konventionen für Python-Domäne und Desktop-Adapter; Architektur und Testpraxis stehen in `architecture.md` und `testing.md`.

> **Herkunft:** Vorlage `3c936a1`: Platzhalter; `b80b873`: Domänen-Heuristiken; `2bfac53`: Desktop-Konvention. Danach ergänzt: getrennte aktive und vorgeschlagene Engineering-Standards. Siehe `agentic-harness/harness/adoption-log.md`.

- Öffentliche Domänen-APIs erhalten Typannotationen. Bestehender Code erfüllt dies nicht überall; bei Änderungen gezielt nachziehen, nicht ungefragt großflächig umschreiben.
- Pro Klasse eine zusammenhängende Domänenverantwortung wahren. Unterschiedliche Änderungsgründe trennen, aber keine Abstraktion ohne konkreten Bedarf einführen.
- Präzise Domänennamen und explizite Zustandsübergänge bevorzugen. Mutationen von Eingaben und Domänenzustand sichtbar halten.
- Bei neuem, lernrelevantem Domänencode nachvollziehbaren schrittweisen Kontrollfluss und aussagekräftige Zwischenvariablen bevorzugen, wenn das Verständnis dadurch steigt; bloß wiederholende Ausführlichkeit vermeiden.
- Kleine Duplikation akzeptieren, bis der gemeinsame Begriff stabil ist. Kommentare für Gründe, Randbedingungen und offene Entscheidungen nutzen, nicht zum Nacherzählen der Syntax.
- Bei verhaltensgleichen Refactorings die kleinste passende Änderung vornehmen und fachfremdes Aufräumen vermeiden.
- Domänenfehler liegen derzeit in `backend.exceptions`; Domänenmodule verwenden diese spezifischen Fehlertypen statt eigene Meldungen beim Auslösen zusammenzubauen.
- Die Desktop-UI in `frontend/desktop_ui.py` verwendet PySide6 (`requirements.txt`), nimmt Zeitpunkte am Button-Klick entgegen, ruft die öffentliche Domänen-API auf und zeigt deren Zustand und fachliche Fehler an. Domänenregeln bleiben im Backend; Widgets und Persistenz gehören nicht hinein.
- Die Terminal-UI ist nicht implementiert; Persistenz ebenso wenig.

## Qualitätswerkzeuge: aktiv vs. zu entscheiden

- **Aktiv:** Python mit Typannotationen an öffentlichen Domänen-APIs als Konvention; pytest als ausgeführter Check (`agentic-harness/harness/project.md`). PySide6 ist die aktuelle Desktop-Abhängigkeit. Weder Formatierer/Linter, statischer Typchecker, Lockfile noch CI sind eingerichtet; eine grüne Testsuite belegt diese Qualitäten nicht.
- **Kandidaten, noch keine Standards:** `pyproject.toml` als gebündelte Python-Projektkonfiguration und reproduzierbare Abhängigkeiten; Ruff für Format/Lint; ein Typchecker (z. B. mypy **oder** Pyright); ein CI-Job mit dem lokal bewährten Gate. Wähle für den nächsten Refactor den kleinsten wirksamen Satz, dokumentiere Version/Scope und prüfe tatsächlichen Nutzen und Fehlerfälle, bevor er Pflicht-Gate wird. Kein massenhaftes Formatieren ohne passenden Änderungszweck.
- **Spätere Stack-Entscheidungen:** Datenbank-, Web- und Analyse-Werkzeuge gehören zu den Meilensteinen unter `agentic-harness/docs/architecture.md`, nicht zum heutigen Code-Gate.
