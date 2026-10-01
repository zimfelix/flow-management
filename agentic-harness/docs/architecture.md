# Architektur – Ist, Soll und offene Grenzen

**Zuständigkeit:** Bausteine, Abhängigkeiten, Paketstruktur und begründete Technologieentscheidungen. Herkunft: `agentic-harness/harness/adoption-log.md`.

## Ist (noch nicht migriert)

```text
main.py → frontend/desktop_ui.py (PySide6)
            → backend/flow_manager.py (Uhr, aktive Session, Arbeitstage)
                → backend/work_day.py → work_session.py → time_period.py
backend/exceptions.py → Domänenfehler; tests/ → flache Suite
```

`FlowManager` koordiniert im Speicher; `WorkDay` besitzt Sessions, `WorkSession` Arbeits-/Pausenperioden und Zustandswechsel. Die UI ruft Manager-Aktionen auf und zeigt Ergebnisse/Fehler; keine SQL- oder Qt-Abhängigkeit im Backend. `frontend/terminal_ui.py` und `tests/test_break_period.py` sind leer. Noch keine Persistenz; App-Ende verliert alle Einträge.

## Bestätigtes Soll für den Struktur-Refactor (noch nicht umgesetzt)

```text
pyproject.toml                 # installierbares Python-Paket, Toolkonfiguration
src/flow_management/
  domain/                     # WorkDay, WorkSession, Perioden, Fehler
  application/                # FlowManager: Uhr, aktive Session, Tage
  ui/desktop/                 # PySide6-Fenster
  __main__.py                 # App-Einstieg, sofern beim Packaging passend
tests/
  domain/                     # Domänenverträge
  application/                # Qt-freier Ablauf
  ui/                         # Desktop-Interaktion (offscreen)
```

Abhängigkeit: `ui → application → domain`; Domäne importiert weder Qt noch eine Datenbank. Der Einstieg verdrahtet die Komponenten. Beim Umzug bestehende Module/Tests zuordnen, Imports auf `flow_management...` umstellen, Paket installierbar machen und Testentdeckung **nach Installation von außerhalb des Repo-Roots** prüfen. Ob der Einstieg `__main__.py`, ein Konsolenskript oder beides wird, beim Packaging entscheiden; bestehendes Verhalten erhalten. Kein leerer Ordner nur für späteres Wachstum.

## Spätere Meilensteine (nicht Bestandteil des aktuellen Pakets)

- Für lokale Speicherung ist SQLite **ein SQL-Datenbanksystem** und ein naheliegender Kandidat; Schema, Migration und tatsächliche Adaptergrenze erst mit Speicherverhalten wählen. Andere Anforderungen können andere Datenbanken begründen.
- Browser-Oberfläche und Analyse benötigen konkrete Nutzerabläufe, bevor Web-Framework oder Datenwerkzeuge gewählt und Pakete angelegt werden.
- Tray/Autostart/Aktivitätserkennung, Sessions über Mitternacht, Zeitzonen und Aufbewahrung sind fachlich offen; keine heutige Implementierung oder Plattformzusage daraus ableiten.
