# Projet 3 : le be:bi

Cette repo contient le code source du projet 3

# Manuel d'utilisation de l'utilisateur

Note : Si `BYPASS_CONNECT` est `True` (Elle l'est par défaut), la m:b ne se connectera pas à une autre m:b et vous permettra de tester les fonctionnalités de la m:b sans avoir besoin d'une autre m:b.

1. (cette étape est sautée si `BYPASS_CONNECT` est `True`) Affiche ・・・ et attend qu'une autre m:b s'annonce, affiche l'id (1 ou 2) de la m:b, affiche ・・・ et attend l'établissement de la connexion secure. Finalement, affiche 'v' ou 'x' selon si la connexion secure est établie ou non.
2. La m:b affiche "?", il faut alors appuier sur `A` pour le mode Parent ou `B` pour le mode Enfant. (Si une deuximème microbit est connectée, elle s'adaptera automatiquement) Finalement, la m:b affiche "P" ou "E" selon le mode choisi pendent une seconde.

## Mode Enfant

Le mode enfant affiche '0' si l'enfant dort, '1' si l'enfant est agité et '2' si l'enfant est très agité. Si vous appuiez sur `A`, l'enfant sera calmé avec une musique. Appuiyer sur `B` pour afficher la quantité de lait.

## Mode Parent

Insérez le mot de passe avec les boutons `A` et `B`. Appuiez sur A et B en même temps pour valider le choix d'une case.
```
0xxxx
00000
00000
00000
00000
```

Vous accederez ensuite au menu parent que vous naviguez avec `A` et `B`. Appuiez sur A et B en même temps pour valider votre choix.

Dès que vous etes dans un des modes, vous pouvez appuier sur le logo microbit pour revenir au menu parent.

### Mode 'C' : Compteur de lait

- Pour ajouter une certaine quantité de lait, appuyez sur le bouton `B`. Chaque unité (un point lumineux), correspont à une valeur standart de 10mL de lait.
- Pour retirer une quantité de lait, appuyez sur le bouton `A`.
- Pour afficher la quantité de lait, appuyez sur les deux boutons `A` et `B` en même temps.
- Pour réinitialiser la quantité de lait, restez appuyé sur les deux boutons `A` et `B` en même temps.

### Mode 'S' : Statut de l'enfant

Affiche l'état de l'enfant.

### Mode 'T : Température

(pas encore implémenté)

### Mode 'F' : Recherche

Affiche un chiffre de 0 à 9 correspondant à la distance entre la m:b et la m:b enfant.

# Manuel d'utilisation du développeur

Le code source se trouve dans `src/source.py`. Pour le minimifier, utilisez `src/minifier.py`. Le résutat est automatiquement écrit dans `main.py`. Les fichiers `ref_...` sont juste des fichiers de référence.
