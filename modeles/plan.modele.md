<!--
MODELE : un plan de chantier, à copier dans `docs/plans/<chantier>.md`.
Écrit par `team-tech-lead` (phases Analyser et Planifier de la méthode `apex`), avant tout travail d'un
développeur. Un plan par chantier qui dure plus d'une journée. Il se RÉÉCRIT, il ne s'empile pas :
une seule ligne de révision en tête (date et raison), l'historique reste dans `git log -p`, les
briefs des tâches terminées sont retirés. Plafond : 150 lignes ; un plan qui dépasse se coupe en
deux chantiers. Chaque développeur reçoit le chemin de ce fichier et le numéro de SA tâche, rien
d'autre. Supprimer les commentaires et remplacer les exemples à l'usage.
-->

# Plan : Export des commandes en PDF

Révision : 2026-01-15, tâche 3 ajoutée après la réponse du propriétaire sur le format (une page par client).

<!-- Ligne de révision : la date et la raison de la dernière réécriture, une seule ligne. -->

Objectif : le propriétaire exporte les commandes d'un client en un fichier PDF depuis l'écran des commandes.
Hors périmètre : l'envoi du PDF par courriel.

<!-- Objectif et hors périmètre : deux ou trois lignes. Le hors périmètre évite qu'un développeur ajoute une fonction non demandée. -->

## Constats

<!--
Ce que l'analyse a trouvé dans le dépôt, un fait par puce, avec le fichier ou la commande qui le montre.
Pas d'opinion ici. Ce qui n'a pas pu être vérifié se dit en une phrase, avec ce qui manque pour le savoir.
-->

- Les commandes sont lues par `src/commandes.ts` ; aucune fonction de mise en page n'existe (vérifié par `grep -rn "pdf" src`).
- Le format d'une facture est décrit dans `docs/format-facture.md`.
- La bibliothèque de génération de PDF n'est pas choisie : à trancher à la tâche 1.

## Choix

<!--
Un tableau par décision à prendre, jamais plus de trois options. La colonne « Recommandation » en
nomme une seule. Un inconvénient vide veut dire que l'option n'a pas été examinée.
Si le propriétaire doit trancher, écrire la question dans « Questions » plus bas.
-->

| # | Sujet | Recommandation | Écarté | Avantages | Risques | Effort |
|---|---|---|---|---|---|---|
| C1 | Génération du PDF | Bibliothèque libre déjà utilisée par le projet | Service en ligne payant | Aucun coût, fonctionne hors ligne | Mise en page à régler à la main | M |

## Tâches

<!--
Une ligne par tâche. « Rôle » : l'agent qui l'exécute (`team-dev-back`, `team-dev-front`, `team-designer`,
`team-qa`, `team-review`, `team-securite`). « Dépend de » : les numéros de tâches qui doivent être
finies avant, ou « aucune ». « Livrable vérifiable » : la commande ou le constat qui prouve que la tâche
est finie. Les tâches sans dépendance commune peuvent partir en parallèle ; le dire sous le tableau.
-->

| # | Titre | Rôle | Dépend de | Livrable vérifiable |
|---|---|---|---|---|
| 1 | Choix de la bibliothèque et gabarit d'une page | team-dev-back | aucune | `npm test -- pdf` vert ; un PDF d'une page produit |
| 2 | Maquette du bouton « Exporter » et de ses quatre états | team-designer | aucune | Maquette validée par le propriétaire |
| 3 | Export d'un client, une page par client | team-dev-back | 1 | Essais verts ; PDF de trois clients de 3 pages |
| 4 | Bouton « Exporter » sur l'écran des commandes | team-dev-front | 2, 3 | Parcours « cliquer, télécharger » joué dans le navigateur |
| 5 | QA du chantier | team-qa | 4 | Cas P1 à P3 de la recette ci-dessous |

Parallèles : 1 et 2. Relecture `team-review` sur le diff entier après la tâche 5.

## Briefs

<!--
Une section par tâche, titre exact « Brief pour <rôle> — tâche N ». Le brief dit : les fichiers à créer
ou modifier, le comportement attendu, les essais ciblés à écrire ou à rejouer (jamais la suite entière sauf
code partagé), ce qui est hors tâche. Il se suffit à lui-même : le développeur ne lit que son brief.
Un brief de tâche terminée se retire du plan.
-->

### Brief pour team-dev-back — tâche 1

Fichiers : `src/pdf/gabarit.ts` (une page à partir d'une liste de commandes), `src/pdf/gabarit.test.ts`.
Comportement : le gabarit reçoit les commandes d'un client et rend un PDF d'une page A4 avec le nom du client en titre.
Essais ciblés : une page pour 5 commandes ; deux pages pour 60 commandes ; client sans commande, page avec la mention « Aucune commande ».
Hors tâche : l'écran, l'envoi par courriel.

### Brief pour team-designer — tâche 2

Fichier : `maquettes/export.html`. Le bouton « Exporter » dans l'en-tête de la liste, avec les quatre états : nominal, chargement, erreur (génération en échec), vide (aucune commande à exporter).
Livrable : la maquette ouverte dans un navigateur, validée par le propriétaire avant la tâche 4.

### Brief pour team-dev-back — tâche 3

Fichiers : `src/pdf/export-client.ts`, `src/pdf/export-client.test.ts`.
Comportement : une page par client, dans l'ordre alphabétique des clients ; un client sans commande n'a pas de page.
Essais ciblés : trois clients, trois pages ; ordre alphabétique ; client vide ignoré.

### Brief pour team-dev-front — tâche 4

Fichiers : `web/commandes/BoutonExport.tsx` et son test.
Comportement : le bouton appelle l'export, affiche l'état de chargement, télécharge le fichier, affiche l'erreur en cas d'échec ; il est inactif quand la liste est vide.
Essais ciblés : les quatre états du composant.

### Brief pour team-qa — tâche 5

Rejouer les cas P1 à P3 ci-dessous sur le résultat final, plus l'écran voisin qui lit les mêmes commandes. Ne pas rejouer toute la recette du projet.

## Recette

<!-- Les cas que la QA rejoue, un par ligne : ce qu'on fait, ce qu'on doit voir. -->

- P1 : exporter un client de 5 commandes, ouvrir le PDF, compter les lignes : 5.
- P2 : exporter un client sans commande : le bouton est inactif, aucun fichier.
- P3 : couper le serveur, cliquer sur « Exporter » : message d'erreur lisible, rien n'est téléchargé.

## Questions

<!--
Ce que seul le propriétaire peut trancher, une question à la fois, avec la tâche qu'elle bloque.
Écrire « Aucune question ouverte. » s'il n'y en a pas.
-->

Aucune question ouverte.
