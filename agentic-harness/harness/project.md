# Projektprofil – aktive Grenzen, Werkzeuge, Befehle

> **Status:** Pending Project Init – der erste Desktop-Prototyp und sein pytest-Gate existieren; Zielarchitektur, Ist-zu-Ziel-Abgleich und nächste Refactor-Grenze sind für die weitere Implementierung noch nicht bestätigt.

**Zuständigkeit:** Bestätigte Projektgrenzen und Einstieg in tatsächlich geltende Werkzeuge und Prüfungen. Architektur, Code- und Testkonventionen stehen unter `agentic-harness/docs/`.

> **Herkunft:** Quellstand `3c936a1` enthielt ein leeres Profil mit `Pending Project Init`. `b80b873` ergänzte Domänenfakten, `2bfac53` Desktop-Prototyp und pytest-Gate. Dieser Schritt kennzeichnet den noch fehlenden Ziel-/Ist-Abgleich; siehe `agentic-harness/harness/adoption-log.md`.

## Produkt und Grenzen

- **Bekannt:** Felix nutzt die lokale Desktop-Anwendung selbst, um Arbeitszeiten mit Start-, Pausen-, Fortsetzen- und Ende-Aktionen zu erfassen und sichtbare Zeitpunkte nachzusehen. Die erste Oberfläche ist Desktop mit Buttons, nicht Terminal. Sie erfasst Zeitpunkte beim Klicken, auch wenn das Fenster zwischendurch nicht im Fokus ist, solange die Anwendung läuft.
- **Grenze des ersten Prototyps (nicht als vollständiger MVP bestätigt):** Noch keine Persistenz über Neustarts, automatische Erkennung von Computeraktivität, OS-Autostart, Tray-Funktion, nachträgliche Korrekturen oder Auswertung. Als erste Daten sind erfundene Testdaten zulässig; keine echten Nutzerdaten oder externen Schreibzugriffe erforderlich. Ob und welche Hintergrundfunktionen zur bedienungsfertigen Ziel-App gehören, bleibt zu klären.
- **Später relevant:** SQL-Persistenz (SQLite oder andere Lösung), Browser- und Data-Science-Auswertung. Die genauen Anforderungen an Hintergrundbetrieb, Mitternacht und Zeitzonen bleiben offen und werden nicht als heutiges Verhalten behauptet.
- **Lernmodus:** Ein extern sichtbares Domänenverhalten nach dem anderen. Bei einer Feature-Idee zuerst Auslöser und sichtbare Änderung beschreiben; vor Umsetzung Eingaben, gelesenen und veränderten Zustand, ungültige Fälle und Invarianten klären. Materiell unterschiedliche Lösungen mit Trade-offs und einer verhältnismäßigen Empfehlung vorstellen. Felix liefert für neues Kernverhalten das fachliche Modell; der Agent kann Boilerplate oder die vereinbarte Umsetzung übernehmen. Nach der Umsetzung das Verständnis mit einem angemessenen aktiven Check prüfen, ohne Routinearbeit zum Quiz zu machen.

## Technik und Betrieb

- **Bekannt:** Python-Domäne in `backend/`, Desktop-UI in `frontend/desktop_ui.py` mit PySide6 (`requirements.txt`), Einstieg `main.py`; Terminal-UI ist leer. `FlowManager` hat noch keine Koordinationsfunktion. Details unter `agentic-harness/docs/architecture.md`.
- **Umgebung:** Python 3.14.7 und `pytest` in der lokalen `.venv` verwendet. Dies legt keine unterstützte Mindestversion fest. Einrichtung: `python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt`. Start: `.venv/bin/python main.py` in einer Desktop-Session; interaktiver Start noch nicht manuell visuell geprüft.
- **Offen:** Unterstützte Python-Version und Zielplattformen jenseits der aktuellen macOS-Umgebung. Keine weiteren Integrationen für den aktuellen Prototyp.
- **Vor der nächsten Produktfunktion:** Zielarchitektur und Code-Abstand unter `agentic-harness/docs/architecture.md` durchgehen; entscheiden, welche Koordination außerhalb des Widgets nötig ist und welcher kleinste verhaltensgleiche Refactor zuerst ansteht. Werkzeugkandidaten und aktiven Qualitätsstandard unter `agentic-harness/docs/code.md` unterscheiden. Der dokumentierte erste Vorschlag ist noch kein umgesetzter Refactor und keine bestätigte Stack-Entscheidung.

## Daten und Freigaben

- **Bekannt:** Das erste MVP hält Zeitpunkte nur im laufenden Prozess; bei Beenden gehen sie verloren. Keine Secrets, externen Dienste, Zugriffsrechte oder externen Schreibaktionen für diesen Ablauf nötig. Zukünftige Speicherung und Umgang mit echten Daten erst vor ihrer Einführung klären.

## Prüf-Einstieg

- **Gate-Befehl (Domäne und Desktop-Adapter, headless):** `QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest -q`. In der eingerichteten Umgebung: 23 bestanden. Qt-offscreen prüft Widget-Verhalten, nicht die visuelle Erscheinung auf einem Bildschirm.
- **Fehlersensitivität geprüft:** Ein temporärer pytest-Test außerhalb des Repos mit `assert False` führte wie erwartet zu Exit-Code 1; die Datei wurde anschließend entfernt. Dies belegt die Fehlererkennung des Test-Einstiegs, nicht jedes Akzeptanzkriterium. Ein Qt-offscreen-Smoke-Test zeigte das Fenster und beendete den Event-Loop mit Exit-Code 0.
- **Offen:** Interaktive Sichtprüfung auf einem Desktop und weitere Evidenz für das erste Produkt-Spec. Kein `Implemented` ohne Nachweise für alle AK und erforderliche Checks.
- **Testpraxis:** `agentic-harness/docs/testing.md`; Codekonventionen und noch nicht aktive Werkzeugkandidaten: `agentic-harness/docs/code.md`. Ruff, Typcheck und CI gehören derzeit **nicht** zum Gate. Zusätzliche Checks erst nach Einrichtung, positiver und sinnvoll negativer Prüfung eintragen.

## Kontextpflege

Nach bedeutsamen Entscheidungen oder Änderungen dauerhaftes Projektwissen mit `/update-context` prüfen; bei Projektabschluss einen Konsistenzcheck durchführen. Bestehende Aussagen aktualisieren oder ersetzen statt Gesprächsprotokolle, temporäre Aufgabenstände oder bereits aus dem Code ersichtliche Details anzuhängen. `/compact` dient nur der Gesprächskomprimierung.
