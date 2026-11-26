<!--
MODELE : decision-log.md, le journal des décisions d'un dépôt.
Copier à la racine du dépôt sous le nom decision-log.md. Une ligne par décision que le propriétaire
a prise : une proposition non validée n'y entre pas. Le journal se CHERCHE (`grep -n "<sujet>"
decision-log.md`), il ne se lit pas en entier ; il l'emporte sur ETAT-PROJET.md et PASSATION.md
quand ils se contredisent. On n'efface jamais une ligne : une décision qui change s'écrit par une
nouvelle ligne datée qui dit ce qui a changé, et l'ancienne reçoit la mention « remplacée par
la ligne du <date> ». Choisir un ordre une fois pour toutes et le garder : plus récent EN HAUT (ci-dessous)
ou plus récent en bas. Supprimer les commentaires à l'usage.
-->

# Journal des décisions : Mon projet

Ce journal se cherche (`grep -n "<sujet>" decision-log.md`), il ne se lit pas en entier. Il l'emporte
sur `ETAT-PROJET.md` et `PASSATION.md` en cas de conflit.

<!--
Format d'une ligne : `- AAAA-MM-JJ <la décision en une phrase>. <Ce qui l'a payée : une mesure, un
chiffre, un fichier, ou la réponse exacte du propriétaire entre guillemets.>`
Le sujet est le premier mot important de la phrase, pour que le grep le retrouve.
-->

- 2026-01-15 Export PDF : une page par client (réponse du propriétaire : « une page par client »). Remplace la ligne du 2026-01-12 qui prévoyait une page unique.
- 2026-01-14 Arrondi : les totaux s'arrondissent au centime supérieur à partir de 5 (mesure : 10,005 affichait 10,00 dans la facture de test `F-0042`).
- 2026-01-12 (remplacée par la ligne du 2026-01-15) Export PDF : une seule page pour tous les clients (réponse du propriétaire : « une seule page »).
- 2026-01-10 Base de données : SQLite pour la première version, le moteur définitif se décide à la mise en ligne (réponse du propriétaire : « SQLite d'abord »).
