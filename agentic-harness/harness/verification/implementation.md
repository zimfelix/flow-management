# Implementierung – Änderung und Verhalten nachweisen

> **Zuständigkeit:** Für jedes betroffene AK beobachtbare Evidenz einholen; kein zweites `agentic-harness/docs/testing.md`. Herkunft: `agentic-harness/harness/adoption-log.md`.

- Prüfe den Diff (Code, Tests, Konfiguration, Dokumentation) gegen Auftrag und Spec auf fehlende Schritte und unerwartete Nebenwirkungen. Existiert ein Aufgabenplan, gleiche ihn zusätzlich mit der tatsächlichen Umsetzung ab; kläre Abweichungen, statt den Plan über Auftrag oder Spec zu stellen. Ohne Plan ist kein eigenes Plandokument nötig.
- Beachte geltende Konventionen in `agentic-harness/docs/code.md` und `agentic-harness/docs/testing.md`. Führe relevante Tests aus `tests/` und die eingerichteten Befehle aus `agentic-harness/harness/project.md` tatsächlich aus; prüfe passende Fehlerfälle.
- Bei beauftragter Strukturmigration Soll-Dateibaum gegen **tatsächliche Dateien** prüfen; Paketinstallation, Imports und Testentdeckung auch außerhalb des Repo-Roots ausführen. Fehlende Moves oder nicht installierbare Pakete als offen melden, selbst wenn bestehende Tests grün sind.
- Ein grüner Build belegt nicht automatisch funktionierendes Nutzerverhalten. Verifiziere den wichtigsten Ablauf über die passende Grenze (z. B. API, Datenbank oder UI), wenn die Spec das verlangt; schütze echte Daten.
- Halte für jedes AK Test oder begründete manuelle Prüfung, beobachtetes Ergebnis und Grenzen des Nachweises fest. Fehlende, leere oder nicht ausführbare Checks sind **nicht verifiziert**, nicht `PASS`.

Hier wird Evidenz für die Änderung beurteilt. Teststrategie steht in `agentic-harness/docs/testing.md`, ausführbare Tests in `tests/`, Abschlussentscheidung in `gate.md`.
