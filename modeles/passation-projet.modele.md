<!--
MODELE : `.claude/passation-projet.md`, le complément d'un dépôt à la commande /passation.
Copier dans `.claude/passation-projet.md` du dépôt. Le skill `/passation` donne le tronc commun
(mesurer, journal des décisions, état, passation, commit) ; ce fichier dit seulement ce qui est propre au
dépôt : les commandes qui mesurent, les étapes en plus, les limites. Il s'applique PAR-DESSUS le skill et
l'emporte en cas de conflit. Chaque section porte le numéro de l'étape du skill qu'elle complète ou
qu'elle ajoute. Une section qui ne sert pas se supprime. Supprimer les commentaires à l'usage.
-->

# Passation de Mon projet : ce qui s'ajoute au skill `/passation`

Le skill `/passation` donne le tronc commun. Ce fichier dit ce qui est propre à ce dépôt : il s'applique en plus, et l'emporte en cas de conflit.

## Étape 1 : les commandes qui mesurent

<!--
La liste exacte des commandes à rejouer à chaque fin de séance, avec ce que chacune prouve. Aucun
chiffre ne se recopie d'un fichier : on refait la commande. Indiquer quels essais rejouer (ciblés sur
ce que la séance a touché) et dans quel cas la suite entière est nécessaire.
-->

- `npm run typecheck` : le code compile sans erreur de type.
- `npm test -- <fichier touché>` : les essais du code modifié par la séance ; la suite entière (`npm test`) seulement si la séance a touché du code partagé par tout le projet.
- `git status --porcelain | wc -l` : le nombre de fichiers non commités.
- `git log --oneline | head -5` : où en est l'historique.

## Étape 2 : le journal des décisions

<!-- Le nom du journal, son ordre (récent en haut ou en bas) et la forme d'une ligne, si le dépôt a une règle de plus que le modèle. -->

Le journal est `decision-log.md`, plus récent en haut. Une ligne par décision que le propriétaire a tranchée, avec ce qui l'a payée (une mesure, un fichier, sa réponse exacte). Une proposition qu'il n'a pas validée va dans la partie « Pas validé » de la passation.

## Étape 3 : `ETAT-PROJET.md`

<!-- Les plafonds et les réflexes propres au dépôt : taille maximale, fichier de débordement, ligne à mettre à jour (version, numéro de journal). -->

Corriger les faits devenus faux, réécrire le bloc « Départ » (40 lignes au plus), mettre à jour la date. Plafond 2000 mots (`wc -w ETAT-PROJET.md`) ; ce qui déborde part dans `docs/`.

## Étape 4 : étapes locales

<!--
Les étapes que seul ce dépôt a : synchroniser un cahier de recette, mettre à jour une liste d'anomalies,
publier une page, regénérer un fichier. Chaque étape dit quand elle s'applique (« si la séance a changé
un écran »), la commande à lancer et ce qu'on ne touche jamais. Supprimer la section s'il n'y en a pas.
-->

Si la séance a changé un parcours visible (écran, message, règle), mettre à jour les cas concernés dans `docs/recette/cas.md` : cas ajoutés, modifiés ou retirés. Ne jamais modifier les verdicts que le propriétaire a saisis.

## Étape 5 : `PASSATION.md`

Remplacement, pas ajout. Aucun fichier daté, aucun dossier. Ordre : la date, où on s'est arrêté en une phrase, ce qui a été fait, ce qui a été proposé et n'est pas validé, ce qu'il faut faire au prochain démarrage, ce qui est urgent et ne dépend pas du propriétaire.

## Étapes 6 et 7 : commit et question

Montrer `git status --porcelain`, proposer un message court, attendre l'accord : jamais de commit de ta propre initiative. Puis une seule question, celle qui débloque le plus.
