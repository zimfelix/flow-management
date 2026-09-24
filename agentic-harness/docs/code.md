# Code – projektbezogene Codekonventionen

**Zuständigkeit:** Dauerhafte Konventionen für Python-Domäne und Desktop-Adapter; Architektur und Testpraxis stehen in `architecture.md` und `testing.md`.

> **Herkunft:** Quellstand `3c936a1` enthielt hier nur Titel und Codekonventions-Platzhalter. In `b80b873` wurde er durch Flow-Management-Domänen-Heuristiken ersetzt. Neu im Project-Init-Schritt: Desktop-Adapter-Konvention mit PySide6. Vergleich: `agentic-harness/harness/adoption-log.md`.

- Öffentliche Domänen-APIs erhalten Typannotationen. Bestehender Code erfüllt dies nicht überall; bei Änderungen gezielt nachziehen, nicht ungefragt großflächig umschreiben.
- Pro Klasse eine zusammenhängende Domänenverantwortung wahren. Unterschiedliche Änderungsgründe trennen, aber keine Abstraktion ohne konkreten Bedarf einführen.
- Präzise Domänennamen und explizite Zustandsübergänge bevorzugen. Mutationen von Eingaben und Domänenzustand sichtbar halten.
- Bei neuem, lernrelevantem Domänencode nachvollziehbaren schrittweisen Kontrollfluss und aussagekräftige Zwischenvariablen bevorzugen, wenn das Verständnis dadurch steigt; bloß wiederholende Ausführlichkeit vermeiden.
- Kleine Duplikation akzeptieren, bis der gemeinsame Begriff stabil ist. Kommentare für Gründe, Randbedingungen und offene Entscheidungen nutzen, nicht zum Nacherzählen der Syntax.
- Bei verhaltensgleichen Refactorings die kleinste passende Änderung vornehmen und fachfremdes Aufräumen vermeiden.
- Domänenfehler liegen derzeit in `backend.exceptions`; Domänenmodule verwenden diese spezifischen Fehlertypen statt eigene Meldungen beim Auslösen zusammenzubauen.
- Die Desktop-UI in `frontend/desktop_ui.py` verwendet PySide6 (`requirements.txt`), nimmt Zeitpunkte am Button-Klick entgegen, ruft die öffentliche Domänen-API auf und zeigt deren Zustand und fachliche Fehler an. Domänenregeln bleiben im Backend; Widgets und Persistenz gehören nicht hinein.
- Die Terminal-UI ist nicht implementiert; Persistenz ebenso wenig. Es sind keine Formatier- oder Lintwerkzeuge im Projekt konfiguriert.
