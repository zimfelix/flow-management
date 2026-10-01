# Code – Python-Konventionen

**Zuständigkeit:** Konventionen für tatsächlich bearbeiteten Code und Packaging; Bausteine/Technologien in `agentic-harness/docs/architecture.md`, Checks in `agentic-harness/harness/project.md`. Herkunft: `agentic-harness/harness/adoption-log.md`.

- **Ist:** Python mit PySide6 für Desktop; `requirements.txt`/`requirements-dev.txt` installieren Abhängigkeiten. `pyproject.toml` konfiguriert Ruff (`E4`, `E7`, `E9`, `F`, `I` und Format). Typchecker, Lockfile und CI sind nicht aktiv.
- **Beim bestätigten Struktur-Refactor:** Ein installierbares `flow_management`-Paket konfigurieren, absolute Imports über diesen Paketnamen verwenden, Toolkonfiguration und Dependencies konsistent halten. Tests müssen gegen das installierte Paket funktionieren, nicht nur dank Repo-Root-Imports. Keine pauschale Neubenennung, die keine Grenze verbessert.
- **Domäne:** Öffentliche APIs typannotieren; Zustandsänderungen und Fehlerfälle explizit halten. Domänenfehler zentral, keine Widgets/SQL in Domain-Modulen. `FlowManager` koordiniert; UI zeigt Zustand und fängt fachliche Fehler ab. Lernrelevante Zustandsübergänge nachvollziehbar Schritt für Schritt schreiben. Keine Abstraktion allein wegen Länge/DRY; kleine verhaltensgleiche Änderungen getrennt von neuen Regeln prüfen.
- **Qualität:** Ruff und pytest sind aktiv; die genauen Befehle stehen im Projektprofil. Typprüfung, reproduzierbare Abhängigkeiten und CI anhand konkreter Risiken nach der Migration bewerten, erst nach Einrichtung und Nachweis ins Gate aufnehmen. Python-Mindestversion ist noch nicht festgelegt.
