# Architektur – tatsächlichen Produktaufbau erklären

**Zuständigkeit:** Tatsächliche Produktbausteine, Verantwortlichkeiten, Datenflüsse und offene Architekturentscheidungen. Geplante Teile bleiben klar vom Ist-Zustand getrennt.

## Produkt und aktueller Stand

Flow Management ist laut Produkt-README als lokale Anwendung zur Erfassung von Arbeitszeit gedacht. Der bisherige Code bildet ausschließlich Domänenlogik ab; eine ausführbare Oberfläche oder Persistenz ist noch nicht vorhanden.

```text
backend.exceptions
└── Domänenfehler und ihre Meldungen

backend.work_day
└── WorkDay
    └── WorkSession
        ├── WorkPeriod
        └── BreakPeriod

backend.flow_manager
└── FlowManager (derzeit nur Platzhalter)
```

- `backend.time_period` definiert `Period` mit Startzeit und optionaler Endzeit sowie die Unterklassen `WorkPeriod` und `BreakPeriod`. Eine Periode kann nicht zweimal beendet oder vor ihrer Startzeit beendet werden.
- `WorkSession` besitzt ihre Arbeits- und Pausenperioden und verwaltet den aktiven Zeitraum. `start_break()` und `resume_work()` beenden den bisherigen Zeitraum, erzeugen und speichern den nächsten und setzen ihn als aktiv. `set_end()` beendet den aktiven Zeitraum und die Session.
- `WorkDay` speichert ein Datum und seine Sessions. Es kann eine Session starten, beenden, pausieren und fortsetzen. Es verhindert mehr als eine aktive Session und delegiert Session-Übergänge an `WorkSession`.
- `FlowManager` enthält derzeit lediglich eine Liste von `WorkDay`-Objekten; Koordinationsverhalten ist nicht implementiert.
- `frontend/terminal_ui.py`, `frontend/desktop_ui.py` und `main.py` sind derzeit leer. UI-Verhalten und ein ausführbarer Anwendungsablauf sind noch nicht vorhanden.
- `tests/` enthält pytest-Tests für Perioden, Sessions und Work Days; siehe `testing.md`.

## Bestätigte Produkt- und Architektur-Richtung

Die Produkt-README und `AGENTS.md` geben folgende Richtung vor; diese Punkte sind Ziele, keine Aussage über bereits implementierte Funktionen:

- Domänenverhalten unabhängig von Terminal-UI, Desktop-UI und Persistenz halten.
- Zuerst die Terminal-Oberfläche aufbauen, die Desktop-Oberfläche später.
- SQLite erst hinzufügen, wenn der In-Memory-Domänenablauf stabil ist.
- Bei neuen Domänenverhalten zuerst die beobachtbare Regel und Zustandsänderung klären.

## Offene Entscheidungen

- Erster Nutzerablauf, MVP und Nicht-Ziele sind noch nicht geklärt.
- Wie werden Sessions behandelt, die Mitternacht überschreiten?
- Welche öffentlichen Operationen soll `FlowManager` anbieten?
- Wie sollen SQLite-Datensätze später zu Work Days, Sessions und Perioden gehören?
- Anforderungen an Zeitzonen, echte Daten und Aufbewahrung sind nicht festgelegt.
