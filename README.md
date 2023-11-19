# Projet 3 : le be:bi

Cette repo contient le code source du projet 3

# Manuel d'utilisation de l'utilisateur

Note : Si `DEV_BYPASS_GET_ID` est `True` (Elle l'est par défaut) la m:b va bypass la fonction `get_id()` vous permettant de tester le code sans avoir à utiliser deux m:bs.

1. La m:b affiche "?", il faut alors appuier sur A pour le mode Parent ou B pour le mode Enfant. (Si une deuximème microbit est connectée, elle s'adaptera automatiquement)
2. La m:b affiche "P" ou "E" selon le mode choisi pendent une seconde.

## Mode Enfant

Si vous avez choisi le mode Enfant, rien ne se passera vu qu'il n'est pas encore implémenté. 😂

## Mode Parent

Si vous avez choisi le mode Parent, vous accederez au menu parent que vous naviguez avec A et B. Appuiez sur A et B en même temps pour valider votre choix.

Vous pouvez alors appuier sur le logo microbit pour revenir au menu parent.

### Mode 1 : Quantité de lait

1. Appuyer sur les deux boutons (a et b) sur le microbit parents à l'affichage de la lettre L dans le menu global
2. Pour ajouter une certaine quantité de lait, appuyez sur le boutons a. Chaque unité (un point lumineux), correspont à une valeur standart de 100mL de lait.
3. Pour corriger et retirer une quantité de lait, appuyez sur le bouton b.
4. Pour revenir en arrière il suffit d'appuyer sur le bouton tactile au-dessus du display

### Mode 2 : Statut de l'enfant

1. Appuyer sur les deux boutons (a et b) sur le microbit parents à l'affichage de la lettre S dans le menu global
2. Une animation indique l'état de l'endant

### Mode 3 : Température

1. Appuyer sur les deux boutons (a et b) sur le microbit parents à l'affichage de la lettre T dans le menu global

(pas encore implémenté)

### Mode 4 : Recherche

1. Appuyer sur les deux boutons (a et b) sur le microbit parents à l'affichage de la lettre R dans le menu global

(pas encore implémenté)

# Manuel développeur

## Types de messages

les messages sont formatés de manière T|L|C où T est le type de message, L est la longueur du message et C est le contenu du message. Voici une liste des types de messages :

`IDa` *(ID ask)* - Demande d'ID
`IDc` *(ID confirm)* - Confirmation d'ID
`ROLEc` *(ROLE confirm)* - Confirmation de rôle
`STATUSa` *(STATUS ask)* - Demande de status
`STATUSr` *(STATUS response)* - Mise à jour sur le status de la m:b
`CMD` - Envoie d'une commande\

Note : il faudrait peut-être repenser le format des messages pour qu'ils soient plus faciles à comprendre (c'est pas grave si ils sont plus longs)

# Types de commandes

Note : Les commandes vont exclusivement de la m:b parent à la m:b enfant

`START_SEARCH` - Début de la recherche d'une m:b enfant\
