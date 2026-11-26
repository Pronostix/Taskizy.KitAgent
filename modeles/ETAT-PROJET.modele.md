<!--
MODELE : ETAT-PROJET.md, le fichier de départ unique d'un dépôt.
Copier ce fichier à la racine du dépôt sous le nom ETAT-PROJET.md, remplacer les exemples
(« Mon projet ») par les faits relevés par commande, puis supprimer tous les commentaires
comme celui-ci. Plafond : 2000 mots (`wc -w ETAT-PROJET.md`). Ce qui déborde va dans `docs/`.
Ce fichier ne fait foi sur rien contre le journal des décisions. Il est réécrit par /passation.
-->

# État du projet : Mon projet

> Ce fichier dit ce qui est vrai à la date indiquée dans « Départ ». Aucun chiffre d'ici ne se
> recopie sans refaire sa commande.

## Départ

<!--
Le bloc « Départ » est la seule chose qu'une séance lit en premier. 40 lignes au plus.
/passation le réécrit entièrement à chaque fin de séance. Chaque ligne ci-dessous
explique son champ en une phrase, entre parenthèses ; supprimer ces parenthèses à l'usage.
-->

- Niveau de suivi : léger
  (une des trois valeurs `léger`, `moyen`, `complet` ; voir `skills/passation/references/niveaux.md`)
- Faits relevés le : 2026-01-15
  (date où les commandes de « Ce qui tourne » ont été rejouées ; si elle est ancienne, tout ce qui suit est à revérifier)
- Où on en est : l'écran de connexion et la liste des commandes fonctionnent ; l'export en PDF n'existe pas encore.
  (deux ou trois phrases sur l'état réel, sans numéro de tâche seul)
- En cours : export des commandes en PDF ; correction de l'arrondi des totaux.
  (ce qui est commencé et pas fini, titres de tâches)
- Attend le propriétaire : choix du format du PDF (une page ou une page par client) ; accord pour la mise en ligne.
  (décisions, validations ou gestes que seul le propriétaire peut faire)
- Dernier arrêt : voir `PASSATION.md`.
  (renvoi vers le fichier de passation, qui détaille la dernière séance)
- Priorités : `docs/plans/export-pdf.md` en premier, puis l'écran de recherche.
  (où vit l'ordre des priorités : un plan, une feuille de route, un fichier nommé)
- Décisions : se cherchent par `grep -n "<sujet>" decision-log.md`.
  (le journal des décisions n'est jamais lu en entier)

## Ce que fait le projet

<!--
Quelques lignes : à qui il sert, ce qu'il fait, où il tourne. Un lecteur qui arrive sans contexte
doit comprendre de quoi il s'agit sans ouvrir le code.
-->

Mon projet est une application web qui permet à une petite équipe de suivre ses commandes clients.
Elle tourne en local pour le moment ; aucune mise en ligne n'a eu lieu.

## Ce qui tourne

<!--
Un tableau, une ligne par chose qui fonctionne. La troisième colonne est une commande que
n'importe qui peut rejouer pour le prouver. Pas de commande, pas de ligne : une affirmation
sans commande va dans « Pas testé ».
-->

| Quoi | État | La commande qui le prouve |
|---|---|---|
| Le code compile sans erreur de type | propre au 2026-01-15 | `npm run typecheck` |
| Les essais passent | 42 essais verts au 2026-01-15 | `npm test` |
| Le serveur local répond | répond « ok » | `curl http://localhost:3000/sante` |
| Le dépôt est propre | aucun fichier non suivi | `git status --porcelain` |

## Pas testé

<!--
Ce qui existe mais n'a pas été vérifié, avec la raison. Supprimer la section si tout est vérifié.
-->

- L'envoi réel des courriels : seul un faux serveur de courriel a servi aux essais.

## Ce qui n'existe pas encore

<!--
La liste courte de ce qui est prévu et absent, pour qu'une séance ne cherche pas du code qui n'a pas été écrit.
-->

- L'export en PDF.
- L'écran de recherche.
