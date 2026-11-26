---
name: point
description: One-page status of the current repository: state, what is in progress, what waits for the owner, the next tasks in order. Read-only. Use when the user says point, fais le point, où en est le projet, état du projet, ce qu'il reste à faire, or types /point.
---

Give the owner the state of the repository they are in, on one page, in French, with short bullets. Change nothing: no file, no commit.

Find the files first: list the repository root and match `ETAT-PROJET.md` (also `ETAT_PROJET.md`), `PASSATION.md` and the decision log, ignoring case and treating `-` and `_` as the same. Read the "Départ" block of the state file (its first 40 lines) and, when it exists, the "Niveau de suivi" line; the three levels are described in `~/.claude/skills/passation/references/niveaux.md` (in this kit: `skills/passation/references/niveaux.md`). Open `PASSATION.md` only to answer "where did we stop". Search the decision log with `grep -n`, never read it whole. If the repository has plans (`docs/plans/`), list those whose tasks are not all done by reading only their headings and status tables.

Then check what you are about to say: rerun the cheap commands that prove it (`git status --porcelain`, `git log --oneline -5`, the branch). A fact taken from a file carries its date; if the file is older than the last commit, say so. Never quote a number from a file without its command or its date.

Report in this order, at most 25 lines: the state in two or three lines; in progress (titles, not numbers); what waits for the owner; the next tasks in priority order, most valuable first; risks that the files themselves name. Finish by saying which file is missing or stale, if any, and stop. Offer `/passation` only when the working tree has uncommitted changes.
