
## Méthode d'équipe avec les sous-agents

Ce bloc s'AJOUTE à la fin de votre CLAUDE.md global. Il ne remplace rien.

## Décisions par grille (règle)

Quand un choix ou un arbitrage se présente, la réponse prend la forme d'une grille de décision, pas d'une explication technique. Colonnes utiles : avantages, inconvénients, complexité, effort (S/M/L ou heures/jours), risque, impact, gain rapide possible. Ajouter tout critère propre au cas (sécurité, performance, évolutivité).

Ce qui permet de trancher vite est la grille, pas le détail technique. Si on demande explicitement le code ou le mécanisme, on le montre.

## Délégation aux sous-agents pour l'exploration (règle)

Dès qu'une réponse demande de balayer plusieurs fichiers, de suivre un flux à travers plusieurs couches ou d'inventorier un dossier, on délègue à un sous-agent (`Explore`, `general-purpose`) et on ne remonte que la conclusion.

À ne PAS déléguer : lire un fichier déjà identifié, modifier du code, faire un choix d'architecture, produire une mesure dont dépend une décision. Cela reste dans le fil principal.

Raison : les résultats d'outils et les blocs de réflexion occupent l'essentiel du contexte. Un sous-agent qui lit vingt fichiers et rend trente lignes garde ces vingt fichiers hors de la fenêtre principale.

Mise en œuvre : un sous-agent par question indépendante, lancés dans le même message pour qu'ils tournent en parallèle, avec le modèle choisi par la grille plus bas.

## Pas de développeur sans plan du tech lead (règle)

Les agents développeurs (`team-dev-back`, `team-dev-front`) ne se lancent jamais sans un plan écrit par `team-tech-lead` pour le chantier.

- Le tech lead construit le plan avec la méthode `apex`, phases Analyser et Planifier seulement.
- Le plan est un fichier `docs/plans/<chantier>.md` dans le dépôt, avec une section « Brief pour <rôle> — tâche N » par tâche.
- Le brief donné au développeur cite le chemin de ce fichier et le numéro de sa tâche.
- Un brief détaillé écrit par le fil principal ne compte pas comme plan.

Raison : sans plan, un développeur part sur une interprétation de la demande que personne n'a relue.

Séquence : `team-product-owner` (cadrage, avec le questionnaire `grilling` / `/grill-me` sur tous les angles) → `team-tech-lead` (étape zéro : l'état réel des projets voisins ; plan, lots) → validation par vous si le plan pose des questions → `team-dev-*` sur un lot → QA et audit de sécurité en parallèle → corrections regroupées.

## L'effort d'équipe suit le risque (règle)

Le nombre de rôles lancés sur un lot dépend de ce que le code peut faire, pas de sa taille. Avant chaque lot, une question : ce code peut-il publier, envoyer, valider, payer ou toucher des données personnelles à la place du propriétaire ?

| Le lot… | Effort | Contenu |
|---|---|---|
| Peut publier, envoyer, valider, payer, gérer l'authentification, toucher des données personnelles, une étape de validation humaine ou une migration de base : OUI | Plein régime | plan du tech lead, développeur, puis QA et audit de sécurité lancés en parallèle, corrections regroupées en un seul passage du développeur |
| Écrans, textes, style | Léger | plan du tech lead, développeur, une seule relecture, pas de QA à part |
| Petite correction, documentation, suivi | Fil principal, seul | vérification directe, pas de sous-agent |

Un défaut mineur ne fait pas un lot : les mineurs sont regroupés avec les corrections du lot suivant ou traités par le fil principal. Les règles « pas de développeur sans plan du tech lead » et « tests ciblés » restent en vigueur à tous les niveaux. Un projet qui déclare un niveau plus strict dans son propre `CLAUDE.md` l'emporte.

Règles de processus associées :

- **Le product owner passe avant le tech lead.** Pour tout lot à risque ou toute feature encore à l'état d'intention, `team-product-owner` lance d'abord le questionnaire `grilling` (`/grill-me`) pour regarder tous les angles : produit, risques, exploitation, sécurité, usage au quotidien, ordre des étapes. Il rend au fil principal des tours de questions numérotées avec sa réponse recommandée ; le fil principal les pose, relance le product owner avec les réponses, jusqu'à ce qu'il n'en reste plus. Les décisions vont dans le journal des décisions du projet. Le plan ne s'écrit qu'après.
- **Étape zéro du tech lead :** avant de citer un projet comme modèle, relever l'état réel des projets voisins (moteur de base, authentification, hébergement, sauvegarde, noms), avec la preuve. Un modèle cité de mémoire est un défaut du plan.
- **QA et audit rendent leurs défauts au format brief de correction** (comportement attendu, fichiers, essai ciblé nommé, interdits) : le tech lead tranche seulement les vrais choix.
- **Une QA de tranche est limitée :** elle reprend les essais déjà écrits, ne couvre que les parcours entre tâches et les cas pas encore prouvés, 20 minutes au plus, et écrit son rapport au fur et à mesure.
- **Pipeline :** le développeur de la tâche suivante démarre pendant que la QA et l'audit de la précédente tournent, quand les fichiers touchés sont différents.

Raison : les QA et audits trouvent de vrais défauts de sécurité dans le code qui publie ou valide, mais un cycle complet par défaut mineur coûte beaucoup de temps pour peu de gain.

## La séance tourne sur Sonnet (règle)

Une séance démarre sur Sonnet, effort élevé (`"model": "sonnet"` dans le settings.json). Le travail qui demande un autre modèle part dans un sous-agent lancé avec ce modèle. Si la séance elle-même a besoin d'Opus (coordination d'une mise en ligne, opération sur une base de production, arbitrage dont dépend une décision), elle le dit avant de continuer, avec la raison en une phrase, et vous basculez par `/model opus`.

Chaque agent porte son `model` et son `effort` dans son en-tête et n'hérite de rien. Effort : `low` pour la recherche et le mécanique, `medium` pour l'exploration et la simplification, `high` pour le code, la conception et les documents de référence, `xhigh` pour la revue, la sécurité et le conseil.

Raison : une séance de coordination qui relaie des messages et compte des tests n'a pas besoin du modèle le plus coûteux.

## Choix du modèle par agent (règle)

Le modèle se choisit par agent, pas par chantier.

| Modèle | Quand |
|---|---|
| Haiku | Balayages mécaniques : inventaire, recherche massive, renommage |
| Sonnet | La spec existe, il s'agit de l'appliquer : porter des valeurs, générer des pages depuis un modèle validé, scaffolder une stack décidée, rédiger d'après des rapports déjà produits, réparer un défaut déjà identifié |
| Opus | Une conclusion fausse coûte cher : mesure dont dépend une décision, vérification adverse, document-contrat que les autres agents appliqueront, contrainte juridique |

Application :
1. Poser la question avant de lancer : « si cet agent se trompe avec assurance, que coûte l'erreur ? » Un chiffre faux dans un document de référence appliqué N fois coûte plus que l'économie du modèle. Un chercher-remplacer raté se voit.
2. Second levier : garder Opus et baisser `effort` (`low` ou `medium`) sur les étapes mécaniques d'un contexte piégeux.
3. Ne pas changer le modèle d'un workflow en cours : cela invalide le cache de reprise et fait perdre le travail déjà fait. La règle s'applique au workflow suivant.
4. Garder la vérification adverse sur Opus : elle pèse peu sur le total et c'est là qu'elle rapporte.

Un agent peut refuser son propre brief si la consigne contient une prémisse fausse. C'est la raison principale de payer Opus.

## Tests et recette ciblés sur la feature (règle)

On ne rejoue pas tout à chaque fois.

- Les essais se choisissent d'après ce que la feature change : tests du code modifié, tests qui lisent les mêmes tables, routes ou textes, parcours visible concerné.
- Suite entière seulement si le chantier touche du code partagé par tout le moteur (schéma, socle de stockage, authentification) que les essais ciblés ne couvrent pas, et même alors réduite aux fichiers concernés quand c'est possible.
- La recette rejoue les cas du cahier créés ou modifiés par la feature, plus les cas voisins qu'elle peut casser, pas tout le cahier.
- Le compte rendu dit quels essais ont été retenus et ce qui n'a pas été rejoué.

Le tech lead nomme les essais ciblés dans chaque brief. Raison : une suite complète de plusieurs heures repousse la mise en ligne pour un gain de couverture que les essais ciblés donnent déjà.

## Nettoyage en fin de chantier (règle)

Une copie de travail (`git worktree`) ou une branche ne survit pas au travail qui l'a créée.

- Fin d'une recette ou d'une relecture : la copie de l'agent se supprime dès que son rapport est rendu.
- Fusion d'une PR : la copie, la branche locale et la branche distante se suppriment le jour même.
- À chaque passation : inventaire (`git worktree list`, branches déjà fusionnées dans `origin/main`, fichiers non suivis de chaque copie) puis nettoyage de ce qui est terminé.

Le hook `garde-suppression.py` bloque `git worktree remove`, `git branch -d` et `git push --delete`, même avec votre accord. L'agent ne le contourne pas. Il vérifie chaque copie (fusionnée ? fichiers non committés ? un test en cours ?), écrit un script de nettoyage dans un dossier temporaire et vous donne la ligne `! bash <script>` à lancer. Ce qui n'est pas fusionné ou contient du travail non committé est listé à part, jamais supprimé d'office.

## Niveaux de suivi (règle)

Trois niveaux de suivi de chantier : léger, moyen, complet. Leur contenu et le moment où passer de l'un à l'autre sont décrits dans `~/.claude/skills/passation/references/niveaux.md`. Le niveau se choisit au démarrage du chantier, avec la même question de risque que pour l'effort d'équipe.
