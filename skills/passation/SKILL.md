---
name: passation
description: End-of-session handover for any repository: measure the real state, log the decisions the owner made, update the state files, rewrite PASSATION.md, then propose the commit. Use when the user says passation, fin de séance, clôture la séance, or types /passation.
disable-model-invocation: true
---

Close the session so the next one starts from the truth, not from memory. Talk to the user in French, short, with numbers or bullets, no filler.

Find the files before touching any. List the repository root (`ls`) and match three files by name, ignoring case and treating `-` and `_` as the same: the handover (`PASSATION.md`), the state file (`ETAT-PROJET.md`, also `ETAT_PROJET.md`) and the decision log (`decision-log.md`, or another name like `DECISIONS-VITRINE.md`; the project complement names it when unsure). Write to the file that exists under its own name, never to a second spelling. Say in one line which of the three you found.

Read first, in this order, whatever exists: the repository's `CLAUDE.md` or `AGENTS.md`, `.claude/passation-projet.md` (the project complement: its steps, commands and limits apply on top of this skill, and win where they conflict; the template is `~/.claude/modeles-kit/passation-projet.modele.md`), then the three files above.

A file that does not exist is never created silently: say it is missing and ask once whether to create it (a handover is the usual yes; a state file or a decision log only if the owner wants one). A repository with none of the three still gets steps 1 and 6, and a decision-free session needs no decision log.

1. Measure, never assume. Rerun the commands that prove the state (the complement lists them; otherwise `git status --porcelain`, `git log --oneline -5` and the repository's test command). Never copy a number from a file into the handover.
2. Log decisions, only when the repository has a decision log. An entry is a decision the owner took in this session: today's date (and the next number if the log numbers its entries), the decision in one sentence, and what paid for it (a measure, a figure, a file). A proposal the owner did not validate is not a decision: it goes in the "not validated" part of the handover.
3. Update the state file (`ETAT-PROJET.md`) when the state moved, and always rewrite its "Départ" block (40 lines at most: level, date of the facts, where things stand, in progress, what waits for the owner, where the last stop is, where the priorities live). Fix the facts that became false, update the date and the journal number, keep the file under its own ceiling; what overflows goes to `docs/` or goes away. The levels of the method and their rules are in `references/niveaux.md`: read it when the repository's level is unclear or when a rule about plans, numbers or tests is in question.
4. Run the extra steps of the project complement, in its order, when there is one (acceptance book, backlog sync, and so on).
5. Rewrite `PASSATION.md` entirely: replacement, never an addition, never a dated file. In this order: the date, where the session stopped in one sentence, what was done, what was proposed and is not validated, what to do at the next start, what is urgent and does not depend on the owner. When it does not exist yet, follow the rule above: ask before creating it.
6. Propose the commit of this repository: show `git status --porcelain`, propose a short message saying what the session changed, and wait for the owner's OK. Never commit or push on your own.
7. Ask one thing only: the open question that unblocks the most. No list of questions.

End with a short report: what was measured, the decisions logged, and the commit waiting for the owner's OK.
