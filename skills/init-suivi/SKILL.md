---
name: init-suivi
description: Set up the follow-up files in a repository that has none (state with its Départ block, handover, decision log) at the right level, léger by default. Use when the user says init suivi, mets en place le suivi, initialise le workflow du projet, or types /init-suivi.
disable-model-invocation: true
---

Set up the follow-up method in the repository the owner is in. Talk to the owner in French, short. The method and its three levels are in `~/.claude/skills/passation/references/niveaux.md` (in this kit: `skills/passation/references/niveaux.md`): read it first.

List the repository root and match the three files by name, ignoring case and treating `-` and `_` as the same. Say in one line what exists. Never overwrite or rename a file that exists: where one exists, only offer to add the missing "Départ" block and the "Niveau de suivi" line after showing the exact text.

Pick the level: léger unless the owner asks for more, or the repository already has plans or an acceptance book (then moyen or complet). Say the level and why in one line, then ask one confirmation before creating anything.

Create only what is missing, only after that confirmation. Build every fact from commands you ran now (`git log`, `git status`, the manifest and README), never from memory, and write "à compléter avec le propriétaire" in the one place a fact cannot be found, rather than inventing it. A file with an unfilled placeholder is a defect: if a section would stay empty, leave the section out.

1. `ETAT-PROJET.md`: title, the "Départ" block (level, date of the facts, where things stand, in progress, waits for the owner, where the last stop is, where the priorities live), then a short "Ce qui tourne" table with the command that proves each line. Under 2000 words. The template is `~/.claude/modeles-kit/ETAT-PROJET.modele.md`.
2. `PASSATION.md`: only the six handover parts (date, where we stopped, done, not validated, next start, urgent), filled from this session. The template is `~/.claude/modeles-kit/PASSATION.modele.md`.
3. A decision log (`decision-log.md`) with its first entry only if the owner decided something this session; otherwise do not create it yet. The template is `~/.claude/modeles-kit/decision-log.modele.md`.

Finish with what was created and the commit waiting for the owner's OK; never commit or push on your own.
