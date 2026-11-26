The one follow-up method, in three levels. A repository declares its level on one line of `ETAT-PROJET.md`: `Niveau de suivi : léger`, `moyen` or `complet`. Without that line, infer it from the files present and say which level you assumed. A level goes up only after an incident that the lighter level could not have caught, never in advance.

Levels

- léger: `ETAT-PROJET.md` (with its "Départ" block), `PASSATION.md`, a decision log. No plans, no acceptance book. Open tasks live in the "Départ" block. For a small or young repository.
- moyen: léger, plus one plan per job that lasts more than a day, in `docs/plans/<job>.md`, and one branch per job (`chantier/<subject>`).
- complet: moyen, plus the acceptance book, defects handled in batches, the `team-*` roles, and a project complement in `.claude/passation-projet.md`. For a project at real risk: real sends, payments, personal data.

The three files

- `ETAT-PROJET.md` is the single start file. It opens with a "Départ" block of 40 lines at most: level, date of the facts, where things stand, what is in progress, what waits for the owner, where the last session stopped, where the priorities live. The whole file stays under 2000 words; what overflows goes to `docs/`.
- `PASSATION.md` holds the detail of the last stop. Read on demand, replaced at each handover, never stacked, never dated files.
- The decision log is searched, never read whole: `grep -n "<subject>" <log>`. It wins over the other two when they conflict.

A start file must fit one read. The "Départ" block is the only thing a session must read first.

Plans (moyen and complet)

A plan is rewritten, not stacked: one revision line at the top (date and reason), history in `git log -p`, briefs of finished tasks removed, 150 lines at most. A plan that grows past that splits into two jobs.

Numbers

Numbers (`D12`, `R3`, and so on) are for agents and for citations inside files. In anything said to the owner, the title comes first and the number, if kept, sits in brackets and never alone.

Tests (any level)

Run only the tests that the change touches, named in the task. A full suite runs out of delivery time (night, calm machine) and blocks a delivery only for code shared by the whole system. One QA pass and one review per job, on the whole diff.
