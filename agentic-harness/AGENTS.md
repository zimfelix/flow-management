# Agentic Harness – Projekteinstieg

> **Zuständigkeit:** Einstieg in den Harness dieses Projekts. Die Root-`AGENTS.md` verweist hierher; bestehende Projektanweisungen bleiben zusätzlich gültig.

> **Herkunft:** Aus dem Harness-Quellstand `3c936a1` übernommen. Bei der ersten Integration `b80b873` wurde ausschließlich Schritt 3 um Flow-Management-spezifische Lese- und Skill-Hinweise ergänzt; Schritte 1, 2, 4 und der Schlusshinweis stammen aus der Vorlage. In diesem Project-Init-Schritt wurde der Regeltext nicht geändert. Vergleich: `agentic-harness/harness/adoption-log.md`.

1. Lies `agentic-harness/harness/core.md` für den Ablauf und `agentic-harness/harness/project.md` für bestätigte Projektgrenzen.
2. Solange das Projektprofil `Pending Project Init` enthält, führe vor der ersten Produktimplementierung `agentic-harness/harness/init.md` durch.
3. Lade bei Bedarf die passende Projekt-Doku unter `agentic-harness/docs/`, Ideas-/Spec-Konventionen unter `agentic-harness/ideas/` und `agentic-harness/specs/` sowie die betroffenen Verification-Dateien unter `agentic-harness/harness/verification/`. Vor Architekturentscheidungen oder Struktur-Refactorings `agentic-harness/docs/architecture.md` lesen; vor Testplanung oder Teständerungen `agentic-harness/docs/testing.md`. Bei Clean-Code-Erklärungen, Code-Reviews und verhaltensgleichen Refactorings zusätzlich den globalen Skill `clean-code-coach` laden und die Heuristiken in `agentic-harness/docs/code.md` anwenden. Für eng begrenzte, fachfremde Fragen keine Detaildoku auf Vorrat laden.
4. `agentic-harness/` ist der gebündelte Harness. Anwendungscode und ausführbare Produkttests bleiben in den Projektordnern `src/` und `tests/` beziehungsweise ihrer bestehenden Struktur.

Nicht alle Dateien auf Vorrat laden. Bei Widersprüchen zwischen bestehenden Projektanweisungen, Auftrag und Harness vor riskanten Änderungen die Zuständigkeit klären; der Harness hebt Projektregeln nicht stillschweigend auf.
