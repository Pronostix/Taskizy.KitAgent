# Extrait de réglages

`settings-extrait.json` se FUSIONNE dans votre `~/.claude/settings.json`. Il ne le remplace pas : si le fichier existe, ajoutez ces clés à celles qui y sont déjà.

- `model` : `sonnet`. La séance principale tourne sur Sonnet, moins coûteux et assez fort pour coordonner. Le travail qui demande Opus part dans un sous-agent lancé avec ce modèle (voir la règle « La séance tourne sur Sonnet »).
- `hooks.PreToolUse` : avant chaque commande Bash ou PowerShell et chaque outil MCP, Claude Code lance `garde-suppression.py`. Le script refuse tout ce qui supprime (fichiers, branches, tables, conteneurs). Le matcher `Bash|PowerShell|mcp__.*` couvre ces trois familles d'outils.
- `hooks...command` : le chemin `~/.claude/hooks/garde-suppression.py` se remplace par le chemin absolu du script sur votre poste si votre système ne développe pas `~`.
- `permissions.deny` : refus fermes, sans question posée. `rm -rf`, `sudo`, `curl | bash` et `wget | bash` exécutent ou effacent sans relecture. `Read(./.env)` et `Read(./.env.*)` empêchent Claude de lire les fichiers de secrets du projet.

Après la fusion, relancez Claude Code. Le JSON doit rester valide : une virgule oubliée entre deux clés désactive tout le fichier.
