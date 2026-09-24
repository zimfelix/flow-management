# Code – projektbezogene Codekonventionen

**Zuständigkeit:** Dauerhafte Konventionen für den vorhandenen Python-Domänencode; Architektur und Testpraxis stehen in `architecture.md` und `testing.md`.

- Öffentliche Domänen-APIs erhalten Typannotationen. Bestehender Code erfüllt dies nicht überall; bei Änderungen gezielt nachziehen, nicht ungefragt großflächig umschreiben.
- Pro Klasse eine zusammenhängende Domänenverantwortung wahren. Unterschiedliche Änderungsgründe trennen, aber keine Abstraktion ohne konkreten Bedarf einführen.
- Präzise Domänennamen und explizite Zustandsübergänge bevorzugen. Mutationen von Eingaben und Domänenzustand sichtbar halten.
- Bei neuem, lernrelevantem Domänencode nachvollziehbaren schrittweisen Kontrollfluss und aussagekräftige Zwischenvariablen bevorzugen, wenn das Verständnis dadurch steigt; bloß wiederholende Ausführlichkeit vermeiden.
- Kleine Duplikation akzeptieren, bis der gemeinsame Begriff stabil ist. Kommentare für Gründe, Randbedingungen und offene Entscheidungen nutzen, nicht zum Nacherzählen der Syntax.
- Bei verhaltensgleichen Refactorings die kleinste passende Änderung vornehmen und fachfremdes Aufräumen vermeiden.
- Domänenfehler liegen derzeit in `backend.exceptions`; Domänenmodule verwenden diese spezifischen Fehlertypen statt eigene Meldungen beim Auslösen zusammenzubauen.
- Terminal- und Desktop-UI sollen Domänenregeln nicht übernehmen; Persistenz ist noch nicht implementiert. Es sind keine Formatier- oder Lintwerkzeuge im Projekt konfiguriert.
