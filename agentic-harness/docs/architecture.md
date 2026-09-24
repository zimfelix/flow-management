# Architektur – tatsächlichen Produktaufbau erklären

**Zuständigkeit:** Tatsächliche Produktbausteine, Verantwortlichkeiten, Datenflüsse und offene Architekturentscheidungen. Geplante Teile bleiben klar vom Ist-Zustand getrennt.

> **Herkunft:** Vorlage `3c936a1`: Platzhalter; `b80b873`: Domänenbestand; `2bfac53`: Desktop-Prototyp. Danach ergänzt: vorgeschlagenes Zielbild und konkreter Ist-zu-Ziel-Abstand. Siehe `agentic-harness/harness/adoption-log.md`.

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

## Zielbild und Abstand – Vorschlag für die nächste Entscheidung

```text
Desktop-UI (Qt: Eingabe/Anzeige)
    → Anwendung/Koordination (aktive Session, Tagwahl, Uhr)
        → Domäne (WorkDay, WorkSession, Perioden; ohne Widgets/SQL)
        → später: Persistenz-Adapter (SQL-Datenbank)
    → später: Auswertung über eigene Web-/Analyse-Grenze
```

- **Bestätigte Richtung:** lokal bedienbare Desktop-Zeiterfassung zuerst, SQL-basierte Speicherung und Browser-/Data-Science-Auswertung später. Die Auswahl eines konkreten DB-, Web- oder Analyse-Frameworks ist **offen**; keine frühzeitige Abhängigkeit hinzufügen.
- **Ist-Abstand:** `frontend/desktop_ui.py` hält derzeit die `WorkDay`-Sammlung und aktive Session selbst, wählt den Tag und liest die Uhr. `backend/flow_manager.py` ist ein leerer Platzhalter ohne Nutzer. Damit ist App-weite Koordination bislang nicht unabhängig vom Widget test- und wiederverwendbar. Das allein beweist noch nicht, dass `FlowManager` die richtige neue Schnittstelle ist.
- **Erster Refactor-Kandidat (noch nicht beschlossen):** Zustands-/Uhr-Koordination vom Widget trennen und denselben Start–Pause–Fortsetzen–Ende-Ablauf ohne Qt durchspielen; Qt bleibt Eingabe/Anzeige. Aktuelles Verhalten und Tests erhalten, keine spekulative Datenbankabstraktion einführen. Danach prüfen, ob sich die Platzhalter `FlowManager` und `frontend/terminal_ui.py` begründet verwenden oder entfernen lassen.
- **Spätere Entscheidungspunkte:** Für Einzelplatz-/lokale Speicherung SQLite als naheliegender SQL-Kandidat, bei anderen Daten-/Mehrnutzeranforderungen Alternativen prüfen; Datenmodell/Migrationen erst nach fachlichen Regeln. Web-Technik und Analysewerkzeuge anhand eines konkreten Auswertungsablaufs wählen, nicht als Teil des heutigen Desktop-Cores.

## Offene Entscheidungen

- Ob „im Hintergrund“ später Tray, OS-Autostart oder automatische Aktivitätserkennung umfasst, ist nicht entschieden; der erste Prototyp hält nur per Button ausgelöste Zeiten bei laufendem Prozess fest.
- Wie werden Sessions behandelt, die Mitternacht überschreiten?
- Welche öffentlichen Operationen soll `FlowManager` anbieten?
- Wie sollen SQLite-Datensätze später zu Work Days, Sessions und Perioden gehören?
- Anforderungen an Zeitzonen, echte Daten und Aufbewahrung sind nicht festgelegt.
