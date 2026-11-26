# Règle d'écriture : marqueurs d'écriture IA

Fichier OPTIONNEL. Il se copie dans `~/.claude/rules/` ou s'ajoute au CLAUDE.md global. Sans lui, la méthode d'équipe fonctionne pareil.

Portée : tout texte produit (réponse, document, note, message de commit, mail, texte d'écran, description de PR).

Le motif : un modèle remplace le fait précis et rare par le générique valorisant. Le texte devient moins précis et plus emphatique. Chaque interdit ci-dessous est une forme de ce seul défaut.

## Niveau 1 : le fond (aucune exception)

1. Aucune phrase sur l'importance, l'héritage ou la tendance plus large : « joue un rôle clé », « témoigne de », « marque un tournant », « ouvre la voie à », « à l'ère de ».
2. Aucune analyse accrochée en fin de phrase par un participe : « …, permettant ainsi de… », « …, contribuant à… », « …, garantissant… ». Si la subordonnée en `-ant` n'ajoute aucun fait, on la supprime, on ne la réécrit pas.
3. Aucune attribution vague : « certains experts », « plusieurs sources », « des études montrent », « il est largement reconnu ». On nomme la source ou on ne l'invoque pas.
4. Aucun superlatif ni formule promotionnelle : « riche », « incontournable », « véritable », « révolutionnaire », « une expérience unique ».
5. Aucune conclusion en gabarit « défis et perspectives » (« Malgré ces défis… », « Perspectives d'avenir »). Le mot « défi » reste permis, c'est le gabarit qui est interdit.
6. Aucun parallélisme négatif : « non seulement X, mais aussi Y », « ce n'est pas X, c'est Y », « loin d'être un simple X ». Même sur une seule phrase.
7. Aucune règle de trois décorative. Trois éléments quand il y en a exactement trois, jamais pour faire ample.
8. `est`, `a`, `fait` plutôt que « constitue », « représente », « s'impose comme », « se positionne comme », « dispose de », « offre ». Le mot simple gagne.
9. Aucun lien vague (« associé à », « en lien avec »). On dit qui a fait quoi, quand.
10. Aucun reste de dialogue dans un livrable : « Bien sûr ! », « J'espère que cela vous aidera », « N'hésitez pas à… ». Un document livré ne parle pas à son commanditaire.
11. Aucun gabarit à trous livré comme fini : `[Nom]`, `[À compléter]`, `INSERT_URL`, `2026-XX-XX`. Un trou non rempli est un défaut de livraison.
12. Aucune clause de méconnaissance déguisée en prudence : « il convient de noter », « cela peut varier ». Si on ne sait pas, on le dit en une phrase et on nomme ce qui manque.
13. Peu de vocabulaire surexploité : « crucial », « robuste », « paysage », « tapestry », « leverage », « foster », « delve », « Additionally, » en tête de phrase. Le synonyme d'un mot surexploité ne l'est pas forcément : ne pas fuir un mot juste.

## Niveau 2 : la forme (subordonnée à la charte du document)

Par défaut : pas d'emoji en tête de titre ou de puce, pas de gras sur chaque terme d'un paragraphe, pas de listes `**En-tête :** texte` empilées là où une phrase suffit, pas de titres en Capitales À Chaque Mot, pas de `---` entre sections, pas de tableau de deux lignes qui serait une phrase, pas de titre qui ne contient que d'autres titres, pas de guillemets courbes mélangés aux droits.

Si le document édité a une charte explicite et contraire, la charte du document gagne. Le niveau 1 n'a jamais d'exception.

## Niveau 3 : ne pas surcorriger

Ne prouvent rien : une grammaire parfaite, une prose soutenue ou froide, un mélange de registres, un mot de liaison isolé, un tiret cadratin isolé, un texte sans source. Ne jamais dégrader un texte pour « avoir l'air humain » : pas de faute volontaire, pas de familiarité plaquée. La cible est la précision, pas le camouflage.

## Un texte gravé ne se réécrit jamais

Une clause juridique, une citation, un texte validé mot pour mot se recopie à l'identique. Aucune règle de style ne le modifie : un seul mot changé peut fabriquer un faux.

## Test avant d'envoyer (dix secondes)

« Si je retire de cette phrase tout ce qui n'est pas un fait vérifiable, que reste-t-il ? » Si la réponse est « rien », la phrase est du remplissage : on la supprime, on ne la réécrit pas.
