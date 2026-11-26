#!/usr/bin/env python3
"""Installateur du kit d'équipe pour Claude Code.

Usage :
  python installer.py --essai            montre ce qui serait fait, ne change rien
  python installer.py                    installe agents, skills, garde-fou, règles, réglages
  python installer.py --externes         installe aussi les skills publiés par d'autres auteurs
  python installer.py --verifier         contrôle seulement : chaque skill appelé par un agent existe-t-il ?

Règles de sûreté :
  - un fichier existant et différent n'est jamais écrasé : il est signalé, le kit est écrit à côté en `.kit` ;
  - CLAUDE.md et settings.json sont sauvegardés en `.avant-kit` avant toute modification ;
  - CLAUDE.md : le kit n'ajoute qu'un bloc entre deux repères, remplaçable à chaque relance ;
  - settings.json : le kit fusionne (garde-fou de suppression, interdictions), il ne supprime rien
    et ne change pas un `model` déjà choisi.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
MAISON = Path.home() / ".claude"
REPERE_DEBUT = "<!-- kit-equipe:debut -->"
REPERE_FIN = "<!-- kit-equipe:fin -->"


def dire(msg: str) -> None:
    print(msg, flush=True)


def copier_arbre(source: Path, cible: Path, essai: bool, rapport: dict) -> None:
    """Copie un dossier sans jamais écraser un fichier différent."""
    for chemin in sorted(source.rglob("*")):
        if chemin.is_dir() or "__pycache__" in chemin.parts:
            continue
        rel = chemin.relative_to(source)
        dest = cible / rel
        if dest.exists():
            if dest.read_bytes() == chemin.read_bytes():
                rapport["identiques"] += 1
                continue
            rapport["differents"].append(str(dest))
            if not essai:
                dest.with_name(dest.name + ".kit").write_bytes(chemin.read_bytes())
            continue
        rapport["nouveaux"] += 1
        if not essai:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(chemin, dest)


def installer_dossier(nom_kit: str, nom_cible: str, essai: bool) -> None:
    source = KIT / nom_kit
    if not source.is_dir():
        return
    rapport = {"nouveaux": 0, "identiques": 0, "differents": []}
    copier_arbre(source, MAISON / nom_cible, essai, rapport)
    dire(f"  {nom_cible}: {rapport['nouveaux']} nouveau(x), {rapport['identiques']} déjà à jour")
    for d in rapport["differents"]:
        dire(f"    ⚠ existe déjà et diffère : {d} (version du kit écrite à côté en .kit)")


def sauvegarder(fichier: Path, essai: bool) -> None:
    sauvegarde = fichier.with_name(fichier.name + ".avant-kit")
    if fichier.exists() and not sauvegarde.exists() and not essai:
        shutil.copy2(fichier, sauvegarde)


def bloc_claude_md(essai: bool) -> None:
    source = KIT / "regles" / "CLAUDE-methode.md"
    if not source.exists():
        return
    cible = MAISON / "CLAUDE.md"
    contenu = cible.read_text(encoding="utf-8") if cible.exists() else ""
    bloc = f"{REPERE_DEBUT}\n{source.read_text(encoding='utf-8').rstrip()}\n{REPERE_FIN}\n"
    motif = re.compile(re.escape(REPERE_DEBUT) + r".*?" + re.escape(REPERE_FIN) + r"\n?", re.S)
    if motif.search(contenu):
        nouveau = motif.sub(lambda _m: bloc, contenu)
        action = "bloc du kit mis à jour"
    else:
        nouveau = (contenu.rstrip() + "\n\n" if contenu.strip() else "") + bloc
        action = "bloc du kit ajouté à la fin"
    if nouveau == contenu:
        dire("  CLAUDE.md: déjà à jour")
        return
    dire(f"  CLAUDE.md: {action}")
    if not essai:
        sauvegarder(cible, essai)
        MAISON.mkdir(parents=True, exist_ok=True)
        cible.write_text(nouveau, encoding="utf-8")


def fusionner_reglages(essai: bool) -> None:
    source = KIT / "reglages" / "settings-extrait.json"
    if not source.exists():
        return
    extrait = json.loads(source.read_text(encoding="utf-8"))
    cible = MAISON / "settings.json"
    actuel = json.loads(cible.read_text(encoding="utf-8")) if cible.exists() else {}
    change = False

    # Modèle : ne change jamais un choix existant.
    if "model" in extrait:
        if "model" not in actuel:
            actuel["model"] = extrait["model"]
            change = True
            dire(f"  settings.json: model = {extrait['model']}")
        elif actuel["model"] != extrait["model"]:
            dire(f"  ⚠ settings.json: model vaut déjà « {actuel['model']} », laissé tel quel. "
                 f"La méthode du kit suppose « {extrait['model']} » : /model {extrait['model']} dans la séance.")

    # Interdictions : union.
    deny_kit = extrait.get("permissions", {}).get("deny", [])
    if deny_kit:
        perms = actuel.setdefault("permissions", {})
        deny = perms.setdefault("deny", [])
        ajouts = [d for d in deny_kit if d not in deny]
        if ajouts:
            deny.extend(ajouts)
            change = True
            dire(f"  settings.json: {len(ajouts)} interdiction(s) ajoutée(s)")

    # Garde-fou de suppression : chemin absolu et bon interpréteur.
    hooks_kit = extrait.get("hooks", {}).get("PreToolUse", [])
    script = (MAISON / "hooks" / "garde-suppression.py").as_posix()
    python = "python" if sys.platform == "win32" else "python3"
    for entree in hooks_kit:
        nouvelle = json.loads(json.dumps(entree).replace("~/.claude/hooks/garde-suppression.py", script))
        for h in nouvelle.get("hooks", []):
            if "command" in h:
                h["command"] = re.sub(r"^python3?\b", python, h["command"])
        liste = actuel.setdefault("hooks", {}).setdefault("PreToolUse", [])
        deja = any("garde-suppression.py" in json.dumps(e) for e in liste)
        if not deja:
            liste.append(nouvelle)
            change = True
            dire("  settings.json: garde-fou de suppression branché")
        else:
            dire("  settings.json: garde-fou de suppression déjà branché")

    if change and not essai:
        sauvegarder(cible, essai)
        MAISON.mkdir(parents=True, exist_ok=True)
        cible.write_text(json.dumps(actuel, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def installer_externes(essai: bool) -> None:
    donnees = json.loads((KIT / "skills-externes.json").read_text(encoding="utf-8"))
    for s in donnees["sources"]:
        if s["mode"] == "skills":
            for nom in s["skills"]:
                cmd = ["npx", "--yes", "skills", "add", s["source"], "-g", "-s", nom]
                dire(f"  {' '.join(cmd)}")
                if not essai:
                    resultat = subprocess.run(cmd, shell=(sys.platform == "win32"))
                    if resultat.returncode != 0:
                        dire(f"    ⚠ échec pour {nom} (code {resultat.returncode}) : à installer à la main")
        elif s["mode"] == "gstack":
            cible = MAISON / "skills" / "gstack"
            if cible.exists():
                dire("  gstack: déjà présent")
                continue
            dire(f"  gstack: {s['commande']}  (exige : {s['exigence']})")
            if not essai:
                resultat = subprocess.run(["git", "clone", "--single-branch", "--depth", "1", s["source"], str(cible)])
                if resultat.returncode == 0:
                    dire("    Dépôt récupéré. Lancez ensuite « ./setup » dans ce dossier (Bun requis).")
                else:
                    dire("    ⚠ échec du clonage de gstack : à faire à la main")


def skills_appeles() -> dict[str, list[str]]:
    """Noms de skills cités entre accents graves dans les tableaux des agents, par agent."""
    connus = json.loads((KIT / "skills-externes.json").read_text(encoding="utf-8"))
    noms = set()
    for s in connus["sources"]:
        noms.update(s["skills"])
    noms.update(p.name for p in (KIT / "skills").iterdir() if p.is_dir())
    noms.update(connus.get("integres-a-claude-code", []))
    appeles: dict[str, list[str]] = {}
    for agent in sorted((KIT / "agents").glob("*.md")):
        texte = agent.read_text(encoding="utf-8")
        for m in re.findall(r"`([a-z0-9][a-z0-9-]+)`", texte):
            if m in noms:
                appeles.setdefault(m, []).append(agent.stem)
    return appeles


def verifier() -> int:
    dossiers = [MAISON / "skills", Path.home() / ".agents" / "skills"]
    appeles = skills_appeles()
    integres = set(json.loads((KIT / "skills-externes.json").read_text(encoding="utf-8")).get("integres-a-claude-code", []))
    manquants = []
    for nom, agents in sorted(appeles.items()):
        if nom in integres:
            continue
        if not any((d / nom).is_dir() for d in dossiers):
            manquants.append((nom, agents))
    dire(f"Skills appelés par les agents : {len(appeles)}")
    if not manquants:
        dire("Tous les skills appelés sont installés.")
        return 0
    dire(f"Manquants : {len(manquants)}")
    for nom, agents in manquants:
        dire(f"  - {nom} (appelé par {', '.join(sorted(set(agents)))})")
    dire("Relancez avec --externes, ou installez-les à la main (voir skills-externes.json).")
    return 1


def main() -> int:
    # Les consoles Windows en cp1252 ne savent pas écrire les accents composés ni les symboles.
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            flux.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="Installateur du kit d'équipe pour Claude Code")
    p.add_argument("--essai", action="store_true", help="ne change rien, montre ce qui serait fait")
    p.add_argument("--externes", action="store_true", help="installe aussi les skills d'autres auteurs")
    p.add_argument("--verifier", action="store_true", help="contrôle seulement les skills appelés")
    a = p.parse_args()

    if a.verifier:
        return verifier()

    dire(f"Kit : {KIT}")
    dire(f"Cible : {MAISON}" + ("  (essai, rien n'est modifié)" if a.essai else ""))
    dire("Agents, skills, garde-fou, règles :")
    installer_dossier("agents", "agents", a.essai)
    installer_dossier("skills", "skills", a.essai)
    installer_dossier("hooks", "hooks", a.essai)
    installer_dossier("modeles", "modeles-kit", a.essai)
    for nom in ("context7.md",):
        src = KIT / "regles" / nom
        if src.exists():
            dest = MAISON / "rules" / nom
            if not dest.exists():
                dire(f"  rules/{nom}: nouveau")
                if not a.essai:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest)
            elif dest.read_bytes() != src.read_bytes():
                dire(f"    ⚠ rules/{nom} existe déjà et diffère (laissé tel quel)")
    dire("Instructions et réglages :")
    bloc_claude_md(a.essai)
    fusionner_reglages(a.essai)
    if a.externes:
        dire("Skills d'autres auteurs :")
        installer_externes(a.essai)
    else:
        dire("Skills d'autres auteurs : non installés (ajoutez --externes).")
    dire("Contrôle :")
    if a.essai:
        dire("  (contrôle ignoré en essai)")
        return 0
    return verifier()


if __name__ == "__main__":
    sys.exit(main())
