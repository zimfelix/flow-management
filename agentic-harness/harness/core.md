# Core – Auftrag bis Übergabe

**Zuständigkeit:** Ablauf, nicht Projektfakten, Testbefehle oder eine zweite Gate-Regel. Herkunft: `agentic-harness/harness/adoption-log.md`.

1. Lies `agentic-harness/harness/project.md`. Steht dort `Pending Project Init`, arbeite zuerst nach `agentic-harness/harness/init.md`.
2. Kläre beauftragtes Ziel und Umfang. Offene größere Vorhaben können als Idea geklärt werden; **bestätigtes und beauftragtes** neues/geändertes Nutzerverhalten braucht eine Spec unter `agentic-harness/specs/`. Ein verhaltensgleicher Refactor oder reine Dokuänderung braucht nicht automatisch eine Produktspec.
3. Lade die betroffene Doku nach `agentic-harness/AGENTS.md`. Bei Strukturaufträgen konkretisiere den vereinbarten Soll-Dateibaum, Imports, Paketinstallation und Testlayout **vor** dem Umbau; verkleinere den Auftrag nicht stillschweigend auf den leichtesten Teil. Kläre Berechtigungen und riskante Schreibaktionen vor Ausführung.
4. Setze die kleinste Änderung um, die den **ganzen vereinbarten Umfang** erfüllt. Gleiche bei neuem Umfang Projektgrenzen und betroffene Specs erneut ab.
5. Prüfe und berichte nach `agentic-harness/harness/verification/gate.md`. Bei Fehlschlag gilt `agentic-harness/harness/verification/fail.md`. `Implemented` nur mit Nachweis sämtlicher betroffener AK und bestandenem erforderlichem Gate; sonst `Modified` und Lücke benennen. Bei Änderungen ohne Produktspec den beauftragten Umfang und die betroffenen Verweise/Diffs prüfen, kein Produkt-Gate behaupten.

**Markdown-Pflege:** Eine Aussage hat einen Ort: Ablauf hier, Projektgrenzen/Befehle im Projektprofil, Architektur/Code/Tests in `docs/`, Soll-Verhalten in Specs. Bestätigtes von offenem trennen; Verweise statt Kopien. In diesem Harness-Test für geänderte Markdown-Dateien eine **kurze** Herkunftsreferenz und den Vergleich im `agentic-harness/harness/adoption-log.md` pflegen. Keine starre Zeilenbegrenzung, aber keine Historie in Pflichtkontext kopieren.
