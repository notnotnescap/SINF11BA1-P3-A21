# Projet 3 : le be:bi

Cette repo contient le code source du projet 3

# Description du fonctionnement

Si `DEV_BYPASS_GET_ID` est `True` (Elle l'est par défaut) la m:b va bypass la fonction `get_id()` vous permettant de tester le code sans avoir à utiliser deux m:bs.

1. La m:b affiche "?", il faut alors appuier sur A pour le mode Parent ou B pour le mode Enfant. (Si une deuximème microbit est connectée, elle s'adaptera automatiquement)
2. La m:b affiche "P" ou "E" selon le mode choisi pendent une seconde.
3. Si vous avez choisi le mode Enfant, rien ne se passera vu qu'il n'est pas encore implémenté. 😂
4. Si vous avez choisi le mode Parent, vous accederez au menu parent que vous naviguez avec A et B. Appuiez sur A et B en même temps pour valider votre choix. (Cependant, la m:b va juste afficher "?" car aucun mode n'est implémenté pour le moment)
5. Vous pouvez alors appuier sur le logo microbit pour revenir au menu parent.

Petit conseil : Si vous essayez de lire et comprendre le code, ne le lisez pas dans l'ordre mais plutôt en suivant le chemin de l'execution du code.

# Menu Parent 1 : Quantité de lait

Pour utiliser le menu:

1. Appuyer sur les deux boutons (a et b) sur le microbit parents à l'affichage de la lettre L dans le menu global
2. Pour ajouter une certaine quantité de lait, appuyez sur le boutons a. Chaque unité (un point lumineux), correspont à une valeur standart de 100mL de lait.
3. Pour corriger et retirer une quantité de lait, appuyez sur le bouton b.
4. Pour revenir en arrière il suffit d'appuyer sur le bouton tactile au-dessus du display
