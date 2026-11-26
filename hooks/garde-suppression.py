# Crochet PreToolUse de Claude Code : refuse les commandes Bash/PowerShell et les outils MCP qui suppriment.
# Sortie 2 + message sur stderr = l'outil est bloqué ; sortie 0 = la commande passe.
# Installation : copier ce fichier dans ~/.claude/hooks/ (Python 3.10 ou plus requis).
# Puis fusionner reglages/settings-extrait.json dans ~/.claude/settings.json, avec le chemin absolu du script.
# Vérification : relancer Claude Code et lui demander de supprimer un fichier de test ; l'outil doit être refusé.
"""Crochet PreToolUse : refuse toute commande qui supprime quelque chose.

Fait pour tourner en mode bypassPermissions. Il lit le texte ENTIER de la
commande (y compris ce qui est passé à ssh, bash -c, python -c), là où une
règle `deny` de Claude Code ne regarde que le début.

Sortie 2 + message sur stderr = l'outil est bloqué, Claude lit le motif.
Sortie 0 = rien à dire, la commande passe.

Limite connue : un script écrit puis lancé, ou une commande encodée, échappe
au filtre. Un fichier écrasé par l'outil Write n'est pas une commande.
"""
import json
import re
import sys

# (motif, libellé affiché) — insensible à la casse
MOTIFS = [
    # Fichiers
    (r"(?<![\w-])rm(?![\w-])", "rm"),
    (r"(?<![\w-])rmdir(?![\w-])", "rmdir"),
    (r"(?<![\w-])(unlink|shred)(?![\w-])", "unlink / shred"),
    (r"\bRemove-Item\b", "Remove-Item"),
    (r"(?<![\w-])(del|erase|rd)(?=\s+[/\w\"'.~$%\\])", "del / erase / rd"),
    (r"\bfind\b[^|;&]*\s-delete\b", "find -delete"),
    (r"\b(rmtree|os\.remove|os\.unlink|\.unlink\s*\()", "suppression par Python"),
    # Git
    (r"\bgit\s+(-C\s+\S+\s+)?clean\b", "git clean"),
    (r"\bgit\s+(-C\s+\S+\s+)?reset\s+[^|;&]*--hard\b", "git reset --hard"),
    (r"\bgit\s+(-C\s+\S+\s+)?push\b[^|;&]*(\s--force\b|\s-f\b|\s--force-with-lease\b|\s\+\S|\s--delete\b|\s-d\b)", "git push forcé ou suppression de branche distante"),
    (r"\bgit\s+(-C\s+\S+\s+)?branch\b[^|;&]*\s(-D|-d|--delete)\b", "git branch -d / -D"),
    (r"\bgit\s+(-C\s+\S+\s+)?worktree\s+(remove|prune)\b", "git worktree remove / prune"),
    (r"\bgit\s+(-C\s+\S+\s+)?stash\s+(drop|clear)\b", "git stash drop / clear"),
    (r"\bgit\s+(-C\s+\S+\s+)?checkout\s+[^|;&]*--\s+\.", "git checkout -- ."),
    (r"\bgit\s+(-C\s+\S+\s+)?restore\b(?![^|;&]*--staged)", "git restore"),
    (r"\bgit\s+(-C\s+\S+\s+)?rm\b", "git rm"),
    # Base de données
    (r"\bDROP\s+(TABLE|SCHEMA|DATABASE|INDEX|VIEW|ROLE|USER)\b", "DROP"),
    (r"\bTRUNCATE\b", "TRUNCATE"),
    (r"\bDELETE\s+FROM\b", "DELETE FROM"),
    (r"\bdropdb\b", "dropdb"),
    (r"\bpg_restore\b[^|;&]*(\s--clean\b|\s-c\b)", "pg_restore --clean"),
    # Docker
    (r"\bdocker(-compose|\s+compose)?\b[^|;&]*\bdown\b[^|;&]*(\s-v\b|\s--volumes\b|\s--rmi\b)", "docker compose down -v"),
    (r"\bdocker\s+(volume|image|container|network|builder|system)\s+(rm|prune)\b", "docker … rm / prune"),
    (r"\bdocker\s+(rm|rmi)\b", "docker rm / rmi"),
    # Disques
    (r"\bmkfs(\.\w+)?\b", "mkfs"),
    (r"\bdd\b[^|;&]*\bof=", "dd of="),
    (r"\bwipefs\b", "wipefs"),
]

# Outils MCP dont le nom annonce une suppression ou un retour arrière
MCP_DESTRUCTIF = re.compile(r"(delete|remove|purge|recreate|restore|reset)", re.I)


def verdict(nom_outil: str, entree: dict) -> str | None:
    """Rend le libellé du motif trouvé, ou None si la commande passe."""
    if nom_outil.startswith("mcp__"):
        m = MCP_DESTRUCTIF.search(nom_outil.split("__")[-1])
        return f"outil {nom_outil}" if m else None
    commande = entree.get("command") or ""
    for motif, libelle in MOTIFS:
        if re.search(motif, commande, re.I):
            return libelle
    return None


def main() -> int:
    # Sous Windows, stdin et stderr sont en cp1252 par défaut : on lit et on
    # écrit en UTF-8 pour ne pas rater une commande accentuée.
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        donnees = json.loads(sys.stdin.buffer.read().decode("utf-8", errors="replace"))
    except (json.JSONDecodeError, ValueError):
        return 0  # entrée illisible : on ne bloque pas le travail pour ça
    trouve = verdict(donnees.get("tool_name", ""), donnees.get("tool_input") or {})
    if trouve is None:
        return 0
    print(
        f"Bloqué par le crochet anti-suppression ({trouve}). "
        "Ne cherchez pas de détour : demandez au propriétaire de lancer "
        "la commande lui-même, ou de l'autoriser explicitement.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
