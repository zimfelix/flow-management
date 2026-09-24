# Architektur – tatsächlichen Produktaufbau erklären

**Zuständigkeit:** Tatsächliche Produktbausteine, Verantwortlichkeiten, Datenflüsse und offene Architekturentscheidungen. Geplante Teile bleiben klar vom Ist-Zustand getrennt.

> **Herkunft:** Quellstand `3c936a1` enthielt hier nur Titel und Architektur-Platzhalter. Die erste Integration `b80b873` ersetzte den Platzhalter durch das vorhandene Flow-Management-Domänenmodell. Neu im Project-Init-Schritt: Desktop-Einstieg, In-Memory-Datenfluss und Desktop-first statt Terminal-first. Vergleich: `agentic-harness/harness/adoption-log.md`.

## Produkt und aktueller Stand

Flow Management ist eine lokale Anwendung für Felix zur Erfassung von Arbeitszeit. Das bestehende Backend bildet die Domäne ab. Ein erster Desktop-Einstieg nutzt es nun direkt; Persistenz ist noch nicht vorhanden.

```text
backend.exceptions
└── Domänenfehler und ihre Meldungen

backend.work_day
└── WorkDay
    └── WorkSession
        ├── WorkPeriod
        └── BreakPeriod

frontend.desktop_ui → WorkDay → WorkSession → Perioden
main.py → Qt-Anwendung und DesktopWindow

backend.flow_manager
└── FlowManager (derzeit nur Platzhalter; nicht im Desktop-Ablauf)
```

- `backend.time_period` definiert `Period` mit Startzeit und optionaler Endzeit sowie die Unterklassen `WorkPeriod` und `BreakPeriod`. Eine Periode kann nicht zweimal beendet oder vor ihrer Startzeit beendet werden.
- `WorkSession` besitzt ihre Arbeits- und Pausenperioden und verwaltet den aktiven Zeitraum. `start_break()` und `resume_work()` beenden den bisherigen Zeitraum, erzeugen und speichern den nächsten und setzen ihn als aktiv. `set_end()` beendet den aktiven Zeitraum und die Session.
- `WorkDay` speichert ein Datum und seine Sessions. Es kann eine Session starten, beenden, pausieren und fortsetzen. Es verhindert mehr als eine aktive Session und delegiert Session-Übergänge an `WorkSession`.
- `FlowManager` enthält derzeit lediglich eine Liste von `WorkDay`-Objekten; Koordinationsverhalten ist nicht implementiert.
- `main.py` startet eine PySide6-Anwendung. `DesktopWindow` in `frontend/desktop_ui.py` verwaltet die Button-Aktionen, zeigt Status und Zeitpunkte und hält `WorkDay`-Objekte im Speicher. Für jede Aktion liest die UI einmal die lokale Uhr und ruft eine öffentliche `WorkDay`-Operation auf. Domain-Fehler werden im Fenster angezeigt. Das Fenster kann unfokussiert bleiben, während der Prozess läuft; bei Beenden gehen die Zeiten verloren.
- `frontend/terminal_ui.py` ist leer. Hintergrund-Tray, Autostart, automatische Aktivitätserkennung und Datenhaltung sind nicht implementiert.
- `tests/` enthält pytest-Tests für Perioden, Sessions, Work Days und die Desktop-Interaktion; siehe `testing.md`.

## Bestätigte Produkt- und Architektur-Richtung

Die Produkt-README und das Projektprofil geben folgende Richtung vor; diese Punkte sind Ziele, sofern nicht oben als implementiert beschrieben:

- Domänenverhalten unabhängig von Terminal-UI, Desktop-UI und Persistenz halten.
- Desktop mit Buttons zuerst; die frühere Terminal-first-Reihenfolge ist für dieses Projekt überholt.
- SQL-Persistenz (SQLite oder eine später bestimmte Alternative) erst nach stabilem In-Memory-Ablauf; Web- und Data-Science-Auswertung danach.
- Bei neuen Domänenverhalten zuerst die beobachtbare Regel und Zustandsänderung klären.

## Offene Entscheidungen

- Ob „im Hintergrund“ später Tray, OS-Autostart oder automatische Aktivitätserkennung umfasst, ist nicht entschieden; das erste MVP hält nur per Button ausgelöste Zeiten bei laufendem Prozess fest.
- Wie werden Sessions behandelt, die Mitternacht überschreiten?
- Welche öffentlichen Operationen soll `FlowManager` anbieten?
- Wie sollen SQLite-Datensätze später zu Work Days, Sessions und Perioden gehören?
- Anforderungen an Zeitzonen, echte Daten und Aufbewahrung sind nicht festgelegt.
