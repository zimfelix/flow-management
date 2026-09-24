# Desktop-Arbeitszeit erfassen

> **Zuständigkeit:** Erster beauftragter, lokal bedienbarer Arbeitsablauf für Felix.

> **Herkunft:** Produktspec aus Felix' Auftrag seit `2bfac53`, nicht aus der Vorlage `3c936a1`. Dieser Schritt aktualisiert nur Nachweise für die neue Struktur; Soll-Verhalten unverändert. Siehe `agentic-harness/harness/adoption-log.md`.

- **State:** Modified
- **Ziel und Nutzer:** Felix möchte seine Arbeitszeit in einer Desktop-Anwendung mit Buttons erfassen, die auch bei nicht fokussiertem Fenster weiterläuft.
- **Beschreibung:** In einer geöffneten Anwendung Arbeitsbeginn, Pausenbeginn, Fortsetzung und Arbeitsende per Button festhalten und den aktuellen Status sowie die bisher erfassten Zeitpunkte sehen. Ein Klick verwendet den aktuellen lokalen Zeitpunkt. Die Erfassung beruht auf den vom Nutzer ausgelösten Aktionen, nicht auf automatischer Erkennung von Computeraktivität.
- **Nicht im Umfang:** Persistenz über App-Neustarts, Autostart beim Systemstart, Tray-Integration, automatische Aktivitätserkennung, nachträgliche Korrekturen, Web-Auswertung und echtes Hintergrund-Tracking bei beendeter App. Sitzungen über Mitternacht und Zeitzonenregeln bleiben für spätere Klärung offen.

## Akzeptanzkriterien

- **AK1:** Beim Start erscheint ein Desktop-Fenster mit erkennbaren Aktionen und dem Zustand „Keine aktive Session“; noch keine Session wird automatisch gestartet.
- **AK2:** „Arbeit starten“ legt zum aktuellen Zeitpunkt eine aktive Arbeits-Session für das Datum des Starts an; Status und sichtbare Zeiteinträge spiegeln sie wider.
- **AK3:** Während der Arbeit startet „Pause beginnen“ eine Pause zum aktuellen Zeitpunkt; „Arbeit fortsetzen“ beendet die Pause und startet eine neue Arbeitsperiode. Status und angezeigte Zeitpunkte werden aktualisiert.
- **AK4:** „Arbeit beenden“ schließt zum aktuellen Zeitpunkt die laufende Session (auch aus einer Pause heraus); danach ist wieder ein neuer Start möglich und der vergangene Eintrag bleibt sichtbar, solange die App läuft.
- **AK5:** Nicht zum aktuellen Zustand passende Aktionen sind nicht auswählbar; bei einem fachlichen Fehler bleibt der bisherige Zustand erhalten und der Fehler wird im Fenster angezeigt.

## Nachweise

- **AK1:** `tests/test_desktop_ui.py::test_window_starts_without_session_and_only_allows_start` bestanden; interaktive Sichtprüfung auf einem Desktop offen.
- **AK2–AK4:** `tests/test_desktop_ui.py::test_buttons_record_work_break_resume_and_end_with_visible_times` bestanden; `test_end_during_break_keeps_entry_and_allows_new_start` bestanden.
- **AK5:** `tests/test_desktop_ui.py::test_invalid_time_keeps_work_running_and_displays_domain_error` bestanden; deaktivierte Buttons in den übrigen Fällen geprüft.
- **Ergänzend:** `tests/test_flow_manager.py` prüft denselben Ablauf ohne Qt, einschließlich abgewiesener Änderungen.
- **Gate:** `.venv/bin/ruff check .`, `.venv/bin/ruff format --check .` → bestanden; `QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest -q` → 27 bestanden. Negative Checks für alle drei Befehle schlugen erwartungsgemäß fehl. Interaktive Sichtprüfung und Verhalten bei nicht fokussiertem Fenster noch nicht belegt; deshalb `Modified`.
