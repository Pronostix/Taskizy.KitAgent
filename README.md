# Kit d'équipe pour Claude Code

Une façon de travailler avec Claude Code sur des projets de développement : une équipe de 14 agents spécialisés, un suivi de projet en trois fichiers, des règles de méthode, et un garde-fou qui bloque les suppressions. Tout est en français.

## Installer

Dans Claude Code, colle ceci en remplaçant le lien :

> Installe ce kit : `https://github.com/Pronostix/Taskizy.KitAgent`. Clone-le, lis `INSTALL.md` et suis-le.

Claude clone le dépôt, te montre ce qu'il va faire, te demande ton accord, puis installe. Sans Claude : `python installer.py --essai` pour voir, `python installer.py` pour installer.

Prérequis : `git`, Python 3.10 ou plus. Node.js pour les skills d'autres auteurs. Bun seulement pour gstack.

## Ce que contient le kit

| Dossier ou fichier | Contenu |
|---|---|
| `agents/` | Les 14 rôles : product owner, tech lead, CTO, architecte, designer, développeur back, développeur front, QA, relecteur, sécurité, performance, conseil, marketing, communication. Chacun porte son modèle et son niveau d'effort. |
| `skills/` | Skills de suivi (`init-suivi`, `passation`, `point`) et skills appelés par les agents dont l'origine n'a pas de dépôt public (`apex`, `llm-council`, `clean-code`, `caveman`, etc.). |
| `skills-externes.json` | Skills appelés par les agents et publiés par d'autres auteurs. Récupérés à la source, jamais recopiés ici. |
| `hooks/` | `garde-suppression.py` : bloque `rm`, `git reset --hard`, suppression de branche, etc. |
| `regles/` | `CLAUDE-methode.md` (ajouté à ton `CLAUDE.md`), `ecriture.md` (optionnel), `context7.md`. |
| `reglages/` | Extrait de `settings.json` : modèle `sonnet`, interdictions, branchement du garde-fou. |
| `modeles/` | Modèles de fichiers de suivi, de plan, de passation. Installés dans `~/.claude/modeles-kit/`. |
| `docs/` | `methode.md` (comment tout s'enchaîne), `skills-appeles.md` (quel agent appelle quel skill). |
| `installer.py` | L'installateur, sûr et rejouable. |

## Ce qui est laissé de côté

Rien de personnel : pas de profil, pas de projets, pas de coffre de notes, pas de clés, pas de plugins ni de réglages d'affichage. Le kit ne modifie ni ne supprime aucun fichier existant : un fichier différent reste en place et la version du kit s'écrit à côté en `.kit`.

## Licences des skills d'autres auteurs

Ils ne sont pas recopiés : l'installateur les récupère chez leurs auteurs, sous leur licence. La liste est dans `skills-externes.json`.
