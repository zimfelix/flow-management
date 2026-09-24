# Flow Management

> **Herkunft:** Diese Produkt-README gehört zu Flow Management, nicht zur kopierten Harness-Vorlage `3c936a1`; sie bestand bereits vor der ersten Integration `b80b873`. Neu im Project-Init-Schritt: Desktop-first, späteres SQL-/Analyseziel und Startbefehle. Genaue Änderungen: `git diff b80b873 -- README.md`; Übersicht: `agentic-harness/harness/adoption-log.md`.

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

Create a virtual environment and install dependencies: `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt`. Launch with `.venv/bin/python main.py`; check with `QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest -q` (offscreen is for tests, not interactive use). The desktop prototype shows recorded times only until the app exits. See `agentic-harness/harness/project.md` for the verified gate and `agentic-harness/specs/desktop-workflow.md` for the first commissioned workflow.
