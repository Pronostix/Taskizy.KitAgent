<!--
MODELE : AGENTS.md, les consignes courtes d'un dépôt pour les agents.
Copier à la racine du dépôt sous le nom AGENTS.md (ou dans CLAUDE.md si le dépôt n'a que celui-là).
Le fichier tient sur un écran : une phrase qui dit ce qu'est le dépôt, où trouver le suivi, puis les
règles qui valent pour tout agent. Les règles ci-dessous sont le socle ; en ajouter une seulement
si une erreur réelle l'a rendue nécessaire. Remplacer « Mon projet » et les chemins, puis supprimer
les commentaires.
-->

# Mon projet : consignes pour les agents

Application web de suivi de commandes pour une petite équipe. Le suivi du projet est dans `ETAT-PROJET.md` (bloc « Départ » en premier), le détail du dernier arrêt dans `PASSATION.md`, les décisions dans `decision-log.md` et les plans de chantier dans `docs/plans/`.

<!-- Première ligne : ce qu'est le dépôt et où se trouve le suivi. Pas d'historique ici. -->

- Rien ne part vers l'extérieur sans la validation du propriétaire : aucun envoi de courriel ou de message, aucune publication, aucun paiement, aucune écriture sur un serveur de production. Un élément passe de brouillon à validé par le propriétaire avant toute action réelle.
- Aucun développeur (`team-dev-back`, `team-dev-front`) ne démarre sans un plan écrit par `team-tech-lead` dans `docs/plans/`, avec une section « Brief pour <rôle> — tâche N » par tâche. Un brief rédigé dans la conversation ne remplace pas ce plan.
- Ne jamais lire, afficher ni copier un fichier `.env`, une clé d'API ou un jeton. Les secrets vivent dans l'environnement du service sur le serveur, jamais dans le dépôt.
- Commit seulement à la demande du propriétaire. Jamais de poussée (`push`) ni de suppression de branche de ta propre initiative.
- Les essais se choisissent d'après ce que le changement touche ; la suite entière ne tourne que pour du code partagé par tout le projet.

<!-- Règles du socle : validation humaine, plan du tech lead, secrets, commit à la demande, essais ciblés. -->
