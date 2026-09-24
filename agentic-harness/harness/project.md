# Projektprofil – aktive Grenzen, Werkzeuge, Befehle

> **Status:** Pending Project Init – erster Nutzerablauf, Grenzen und Prüf-Einstieg sind noch nicht vollständig geklärt. Vorgehen: `agentic-harness/harness/init.md`.

**Zuständigkeit:** Bestätigte Projektgrenzen und Einstieg in die tatsächlich geltenden Werkzeuge und Prüfungen. Architektur, Code- und Testkonventionen stehen unter `agentic-harness/docs/`.

## Produkt und Grenzen

- **Bekannt:** Laut `README.md` Lernprojekt für eine lokale Anwendung zur Erfassung von Arbeitszeit in Work Days, Sessions und Pausen. Domänenlogik vor Oberfläche und Persistenz; Terminal-UI vor Desktop-UI; SQLite erst nach stabilem In-Memory-Ablauf. `README.md` beschreibt Richtung, nicht vollständig implementiertes Verhalten.
- **Offen:** Nutzer, konkreter erster Ablauf, MVP und Nicht-Ziele.
- **Lernmodus:** Ein extern sichtbares Domänenverhalten nach dem anderen. Bei einer Feature-Idee zuerst Auslöser und sichtbare Änderung beschreiben; vor Umsetzung Eingaben, gelesenen und veränderten Zustand, ungültige Fälle und Invarianten klären. Materiell unterschiedliche Lösungen mit Trade-offs und einer verhältnismäßigen Empfehlung vorstellen. Felix liefert für neues Kernverhalten das fachliche Modell; der Agent kann Boilerplate oder die vereinbarte Umsetzung übernehmen. Nach der Umsetzung das Verständnis mit einem angemessenen aktiven Check prüfen, ohne Routinearbeit zum Quiz zu machen.

## Technik und Betrieb

- **Bekannt:** Python-Quellcode in `backend/`, leere Einstiegspunkte in `frontend/` und `main.py`; `pytest` ist in `requirements-dev.txt` aufgeführt. Aktueller Aufbau und geplante Grenzen: `agentic-harness/docs/architecture.md`.
- **Offen:** Python-Version, ausführbarer Startbefehl, weitere Integrationen und Betriebsform. Ein produktiver Anwendungsablauf ist noch nicht implementiert.

## Daten und Freigaben

- **Offen:** Echte Daten, Secrets, Berechtigungen sowie externe Schreibaktionen. Vor riskanten externen Änderungen gesondert klären; aus „lokal“ keine Freigabe ableiten.

## Prüf-Einstieg

- **Bekannt:** Bestehende Tests unter `tests/` für Teile der Domäne; `tests/test_break_period.py` ist leer. Projektpraxis unter `agentic-harness/docs/testing.md`, Codekonventionen unter `agentic-harness/docs/code.md`.
- **Offen:** Ausführbaren Prüf-Befehl, vollen Suite-Erfolg und absichtlich fehlschlagenden Check noch prüfen und erst dann als Gate eintragen. Kein `Implemented` aus der bloßen Anwesenheit von Tests ableiten.

## Kontextpflege

Nach bedeutsamen Entscheidungen oder Änderungen dauerhaftes Projektwissen mit `/update-context` prüfen; bei Projektabschluss einen Konsistenzcheck durchführen. Bestehende Aussagen aktualisieren oder ersetzen statt Gesprächsprotokolle, temporäre Aufgabenstände oder bereits aus dem Code ersichtliche Details anzuhängen. `/compact` dient nur der Gesprächskomprimierung.
