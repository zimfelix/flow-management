# Flow Management – V2-Experiment

> **Herkunft:** Projekt-README vor `b80b873`, nicht aus Vorlage `3c936a1`. `2bfac53` ergänzte Desktop-first und Startbefehle; dieser Schritt präzisiert Struktur und Qualitätsprüfungen. Details: `agentic-harness/harness/adoption-log.md` und Git-Diffs.

This branch develops a separate V2 in the same repository. `main` remains the original learning project. The confirmed `src/flow_management/` migration is documented but **not yet implemented**; see `agentic-harness/docs/architecture.md`.

- Build a local application for tracking work time.
- Organize time as work days, sessions, and breaks.
- Start with pure Python domain logic before adding interfaces.
- Define `WorkDay`, `WorkSession`, `BreakPeriod`, and `FlowManager` responsibilities.
- Define behavior before implementation and add valuable tests afterward using the project testing workflow.
- First usable interface is now a desktop application with buttons; the earlier terminal-first goal is superseded for the first workflow. Terminal UI remains optional, not an MVP prerequisite.
- The first in-memory workflow records button-triggered work and break timestamps while the process runs; it does not detect computer activity or keep recording after the app exits.
- Add persistence (SQLite or another SQL solution) after the core workflow is stable, then later build analysis through a browser and data-science work. Background/tray behavior and system autostart are later decisions.
- Integrate useful session-notes concepts near the end.
- Learn OOP, state lifecycles, architecture, testing, and SQL through the project.
- Use Pi directly while refining a minimal prompt-engineering workflow.

## Current local prototype

Create a virtual environment and install dependencies: `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt`. Launch with `.venv/bin/python main.py`. From the repo root, run `.venv/bin/ruff check .`, `.venv/bin/ruff format --check .` and `QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest -q` (offscreen is for tests, not interactive use). The desktop version retains recorded times only until the app exits.

## Structure and later extensions

```text
main.py → frontend/desktop_ui.py (PySide6 buttons and display)
                     → backend/flow_manager.py (in-memory coordination and clock)
                         → backend/work_day.py → work_session.py → time_period.py
tests/ → domain, manager and desktop interaction
```

No unused database, web or analysis packages are pre-created. SQL persistence and later browser/data-science analysis will use separate boundaries when their behavior is decided; see `agentic-harness/docs/architecture.md`. `agentic-harness/harness/project.md` records the current verification gate and `agentic-harness/specs/desktop-workflow.md` the commissioned workflow.
