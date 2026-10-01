# Projektprofil – Flow Management

**Zuständigkeit:** Aktiver Meilenstein, Grenzen und ausführbare Befehle. Details gezielt laden, nicht hier duplizieren. Herkunft: `agentic-harness/harness/adoption-log.md`.

## Ziel und Grenze

- **Nutzer:** Felix. **Jetzt:** lokale, flüchtige Desktop-Zeiterfassung per Start/Pause/Fortsetzen/Ende und Zeitliste. Daten gehen beim Beenden verloren; keine echten Daten oder externen Schreibaktionen erforderlich.
- **Später:** Speicherung mit einer SQL-Datenbank, anschließend Web-/Data-Science-Auswertung. Tray, Autostart, Aktivitätserkennung, Mitternacht/Zeitzonen und weitere Zielplattformen vor ihrer Umsetzung klären.
- **Lernmodus:** Ein sichtbares Verhalten nach dem anderen; Felix entscheidet fachliche Regeln, der Agent übersetzt sie in Code und passende Tests. Vor neuem Kernverhalten Eingaben, Zustandswechsel, Fehler und Invarianten klären; anschließend Verständnis angemessen prüfen.

## Struktur und Werkzeuge

- **Ist:** `backend/` (Domäne + FlowManager), `frontend/desktop_ui.py` (PySide6), `main.py`, flaches `tests/`; Python 3.14.7 in der aktuellen macOS-Umgebung. Aktueller Datenfluss: `agentic-harness/docs/architecture.md`.
- **Bestätigtes Ziel, noch nicht umgesetzt:** installierbares Paket `src/flow_management/` mit `domain/`, `application/` und `ui/desktop/` sowie entsprechend gegliederte `tests/`. Erst Paketlayout, Imports und Testentdeckung migrieren und prüfen; **kein** vorauseilendes DB-/Web-/Analyse-Paket. Dies ist trotz früherem UI-/Manager-Refactor ein offener Strukturauftrag, kein abgeschlossener Refactor. Soll-Dateibaum: `agentic-harness/docs/architecture.md`.
- **Aktiv:** PySide6 (`requirements.txt`), pytest und Ruff (`requirements-dev.txt`, `pyproject.toml`). Packaging/Editable-Installation, Typchecker, Lockfile und CI sind **nicht** eingerichtet. Konventionen: `agentic-harness/docs/code.md`; Tests: `agentic-harness/docs/testing.md`.

## Einstieg und Gate (gegenwärtiger Ist-Stand)

- Umgebung: `python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt`; Start aus Repo-Root: `.venv/bin/python main.py`. **Nach src-Migration** Einstieg/Installation neu prüfen und hier ersetzen.
- Gate aus Repo-Root: `.venv/bin/ruff check .`; `.venv/bin/ruff format --check .`; `QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest -q`. Zuletzt: alle bestanden, 27 Tests. Für alle drei Checks wurde ein absichtlicher Fehlschlag erkannt. Kein Ersatz für interaktive Desktop-Sichtprüfung; `agentic-harness/specs/desktop-workflow.md` bleibt `Modified`.
- **Vor Abschluss der Strukturmigration:** tatsächlichen Dateibaum, `pip install -e .`, Imports/Testentdeckung von außerhalb des Repo-Roots und das angepasste Gate prüfen. Nichts davon ist bisher nachgewiesen.
