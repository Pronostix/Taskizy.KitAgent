# La méthode en une page

## L'équipe

Chaque rôle est un agent défini dans `agents/`. Ils travaillent dans cet ordre quand la demande est une intention, pas une tâche :

1. **`team-product-owner`** cadre : il passe d'abord la demande au questionnaire `grilling` (`/grill-me`) pour regarder tous les angles, par tours de questions numérotées avec sa réponse recommandée, que le fil principal pose à la personne. Puis il écrit le problème, le périmètre minimal, les critères d'acceptation et ce qui est renvoyé à plus tard.
2. **`team-cto`**, **`team-architecte`** et **`team-conseil`** interviennent quand un choix structurant coûte cher à rater.
3. **`team-tech-lead`** commence par relever l'état réel des projets voisins (moteur de base, authentification, hébergement, sauvegarde), avec la preuve, puis découpe en tâches et écrit le plan `docs/plans/<chantier>.md`, avec une section « Brief pour <rôle> — tâche N » par tâche.
4. **`team-designer`** conçoit l'écran avant tout code.
5. **`team-dev-back`** et **`team-dev-front`** codent, un lot à la fois. Ils s'arrêtent si le brief ne cite pas le plan.
6. **`team-qa`** et **`team-securite`** vérifient et auditent en parallèle, et rendent leurs défauts au format brief de correction (comportement attendu, fichiers, essai ciblé, interdits). **`team-review`** relit à la fin d'une tranche, pas après chaque lot. Une QA de tranche reprend les essais déjà écrits et ne couvre que les parcours entre tâches, en 20 minutes au plus.
7. **`team-performance`**, **`team-marketing`** et **`team-communication`** servent à la demande.

## L'effort suit le risque

- Plein régime pour tout ce qui peut publier, envoyer, valider, payer ou toucher des données personnelles : plan, développeur, puis QA et audit de sécurité en parallèle, corrections regroupées en un seul passage.
- Léger pour les écrans et les textes : plan, développeur, une relecture.
- Le fil principal fait seul, avec vérification, les petites corrections, la documentation et le suivi.
- Un défaut mineur ne fait pas un lot.
- Le développeur de la tâche suivante démarre pendant la QA et l'audit de la précédente, quand les fichiers touchés sont différents.

## Le suivi de projet

Trois fichiers par dépôt, dont le niveau (léger, moyen, complet) est écrit en une ligne dans `ETAT-PROJET.md` :

- `ETAT-PROJET.md` : le fichier de départ, avec un bloc « Départ » de 40 lignes au plus.
- `PASSATION.md` : le détail du dernier arrêt, remplacé à chaque passation.
- `decision-log.md` : une ligne datée par décision, cherché par `grep`, jamais lu en entier. Il l'emporte sur les deux autres en cas de conflit.

Commandes : `/init-suivi` crée les fichiers, `/passation` clôt une séance, `/point` donne l'état en une page. Les niveaux sont définis dans `skills/passation/references/niveaux.md`.

## Les garde-fous

- Pas de développeur sans plan écrit par le tech lead.
- Tests et recette ciblés sur la feature, suite entière seulement pour du code partagé.
- Le garde-fou de suppression bloque les commandes destructrices ; en cas de besoin, l'agent écrit un script de nettoyage et la personne le lance.
- Séance sur Sonnet, effort élevé ; le modèle de chaque agent est écrit dans son en-tête.
