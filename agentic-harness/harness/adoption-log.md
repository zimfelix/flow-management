# Harness-Übernahme – Herkunft der Markdown-Inhalte

**Zuständigkeit:** Herkunfts- und Änderungsnachweis für das Harness-Lernprojekt; keine zweite Kopie der Produktregeln. Vergleiche drei Stände: **Vorlage** `FelixZimmermannDev/agentic-harness-v3` bei Commit `3c936a1f7e6b663f2751b725853d19f142bf01c5` (Quellordner `agentic-harness/`) → **erste Flow-Management-Integration** `b80b873` → **erster Project-Init-/Prototyp-Schritt** `2bfac53` → **Präzisierung nach `2bfac53`** auf `test/harness-v3`. Der Quell-Commit ist gepinnt, da sich GitHub-`main` ändern kann. Die zwei Vergleiche, nicht die heutige Vorlage auf `main`, bestimmen die Herkunft.

Die Angaben in den bearbeiteten Markdown-Dateien sind kurze Wegweiser; der genaue Wortlaut ist über Git-Diffs prüfbar. Unveränderte Vorlagendateien werden nur hier gelistet, um sie nicht allein für einen Herkunftshinweis zu verändern. Dateien außerhalb von `agentic-harness/` stammen nicht aus der kopierten Harness-Vorlage.

## Bereits bei erster Integration aus der Vorlage übernommen

**Unverändert in `b80b873`, `2bfac53` und der anschließenden Präzisierung:**

- `agentic-harness/README.md`, `agentic-harness/docs/README.md`
- `agentic-harness/harness/templates/idea.md`, `agentic-harness/harness/templates/spec.md`
- `agentic-harness/harness/verification/fail.md`, `gate.md`, `implementation.md`, `requirements.md`
- `agentic-harness/ideas/README.md`, `agentic-harness/specs/README.md`

**Unverändert aus der Vorlage in `b80b873`, in `2bfac53` erstmals ergänzt:**

| Datei | Neu in `2bfac53` |
| --- | --- |
| `agentic-harness/harness/core.md` | Provenienz-Hinweis und letzte Regel unter „Markdown-Dateien pflegen“; bestehender Ablauf blieb erhalten. |
| `agentic-harness/harness/init.md` | Provenienz-Hinweis, Bündelung der Rückfragen in Schritt 1 und letzter Absatz zur Herkunftspflege; übrige Schritte stammen aus der Vorlage. |

## Bereits im ersten Integrations-Commit `b80b873` angepasst

| Datei | Aus der Vorlage | Änderung schon in `b80b873` | Neu in `2bfac53` |
| --- | --- | --- | --- |
| `agentic-harness/AGENTS.md` | Einstieg und Schritte 1–4 | Zusatz zu Schritt 3: projektspezifische Lese- und Skill-Hinweise | Nur Herkunftshinweis; Regeltext unverändert |
| `agentic-harness/docs/architecture.md` | Titel und leerer Architektur-Platzhalter | Projektbezogene Beschreibung der vorhandenen Domäne statt Platzhalter | Desktop-Datenfluss, Zustand und geänderte UI-Reihenfolge |
| `agentic-harness/docs/code.md` | Titel und leerer Code-Platzhalter | Domänen-Heuristiken aus bisherigen Projektregeln statt Platzhalter | PySide6-/Desktop-Adapter-Konvention |
| `agentic-harness/docs/testing.md` | leerer Testing-Platzhalter | Bisheriges projektbezogenes `docs/testing.md` übertragen und für den Harness angepasst | Desktop-Widget-Testniveau und offscreen-Ausführung |
| `agentic-harness/harness/project.md` | leeres Profil mit `Pending Project Init` | bekannte Domänenfakten und Lernmodus eingetragen, Init-Status offen gelassen | Nutzer, erster Desktop-Ablauf, Grenzen, Stack und geprüfter Gate-Befehl |

Die vorhandenen Produkt-Docs `docs/architecture.md` und `docs/testing.md` wurden in `b80b873` entfernt beziehungsweise in die Harness-Dokumentation übertragen; siehe Commit-Diff. Root-`AGENTS.md` war eine **Flow-Management-Datei**, nicht die Root-`AGENTS.md` des Quell-Repos: `b80b873` ersetzte ihre bisherigen Detailregeln durch den Verweis auf `agentic-harness/AGENTS.md`. Die Produkt-`README.md` bestand bereits vor `b80b873` und wurde in `2bfac53` um Desktop-first, spätere Ziele und Startbefehle aktualisiert.

## Neu in `2bfac53`

| Datei | Herkunft |
| --- | --- |
| `agentic-harness/specs/desktop-workflow.md` | Neue Produktspec aus Felix' Auftrag, im Format der bestehenden Harness-Vorlage. |
| `agentic-harness/harness/adoption-log.md` | Dieses Herkunftsprotokoll für das Lernprojekt. |

**Sonstige in `2bfac53` unveränderte Projekt-Markdown-Datei:** `AGENTS.md`. Die unveränderten Harness-Dateien stehen oben.

## Präzisierung nach `2bfac53`

Auslöser: Der erste Durchlauf dokumentierte den Anfänger-Ist-Zustand und ergänzte eine UI, ohne Vision, Zielarchitektur, Qualitätswerkzeuge und Modernisierungsbedarf vorab ausreichend gegeneinander zu prüfen. Ausführliche, teils noch offene Erkenntnisse: `learning-state.md` (nur lokal in Flow Management; die externe Harness-Vorlage wird nicht geändert).

| Datei | Änderung gegenüber `2bfac53` |
| --- | --- |
| `learning-state.md` | Neu: bestätigte Schwächen, präzisierte Init-Reihenfolge, Testhypothesen für das nächste Projekt. |
| `agentic-harness/AGENTS.md` | Bei Harness-Aufgaben den lokalen Lernstand lesen; Vorlage bleibt unberührt. |
| `agentic-harness/harness/init.md` | Verbindlicher Ist-zu-Ziel-Abgleich samt Werkzeugauswahl und Modernisierungsgrenze auch für bestehende Projekte. |
| `agentic-harness/harness/project.md` | `Pending Project Init` für ausstehenden Architektur-Abgleich, getrennt vom bereits bestandenen pytest-Gate. |
| `agentic-harness/docs/architecture.md` | Ist, vorgeschlagenes Zielbild, konkrete Lücke und erster Refactor-Kandidat getrennt. |
| `agentic-harness/docs/code.md` | Tatsächlich aktive Qualitätspraxis gegenüber Werkzeugkandidaten abgegrenzt. |
| `agentic-harness/docs/testing.md` | Testpraxis verdichtet; Test-Gate von noch nicht eingerichteten Checks getrennt. |
| `agentic-harness/harness/adoption-log.md` | Diese zweite Änderungsetappe ergänzt und veraltetes „laufend“-Etikett für `2bfac53` korrigiert. |

**Bei der Präzisierung unverändert:** übrige Markdown-Dateien einschließlich `agentic-harness/harness/core.md`, `AGENTS.md`, `README.md` und `agentic-harness/specs/desktop-workflow.md`; keine Änderung an Produktcode oder der separaten Vorlage `../agentic-harness-v3/`.

**Prüfung:** Ein Checkout der Vorlage bei `3c936a1f7e6b663f2751b725853d19f142bf01c5` ermöglicht den Vergleich mit `git show b80b873:agentic-harness/<datei>`. Spätere Etappen anhand `git diff b80b873..2bfac53 -- <datei>` und `git diff 2bfac53 -- <datei>` vergleichen (für neue Dateien `git status --short`). Ein Dateivergleich ist präziser als die Kurzübersicht hier.
