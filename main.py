"""
P3-SINF11BA1-A21
"""

from microbit import *
import radio
import random

# initialisation générale
INITIAL_CHANNEL = 69
INITIAL_GROUP = 42
DEV_BYPASS_GET_ID = True # True pour faire des tests avec qu'une seule m:b

radio.on()
radio.config(channel=INITIAL_CHANNEL, group=INITIAL_GROUP)

def get_id() -> int:
    """
    Protocole MicroID™️ permettant d'attribuer un ID (1 ou 2) à chaque micro:bit

    La microbit commence par demander si elle peut être la m:b 1. Puis, elle écoute si elle reçoit une réponse.
    Si elle reçoit la première le message d'une autre micro:bit, elle devient la m:b 2 et envoie une réponse autaurisant l'autre m:b à devenir la m:b 1.
    """
    display.show(Image("00000:""00000:""90909:""00000:""00000"))
    radio.send("ID|1|1") # est ce que je peux etre la m:b 1?
    while True:
        message = radio.receive()
        if message:
            if message == "ID|1|1": #est ce que je peux etre la m:b 1?
                radio.send("ID|1|2") # oui, tu peux! je vais etre la m:b 2 alors!
                print("ID: 2")
                return 2
            elif message == "ID|1|2": # oui, tu peux! je vais etre la m:b 2 alors!
                print("ID: 1")
                return 1

    # confirmation (A FAIRE) parce que oui, il existen encore un micro possibilité que les deux micro:bit envoient en même temps le message "ID|1|1" 
    # en vrai j'ai refais des tests et ça arrive pas mais bon, on sait jamais

def check_connection() -> bool:
    """
    Vérifie si la connexion est toujours active

    La m:b 1 commence par envoyer un message pour demander si la m:b 2 est toujours là.
    La m:b 2 répond seulement si elle reçoit le message de la m:b 1.
    """
    # A FAIRE
    pass

def get_role() -> str:
    """
    La m:b devient Parent si on appuie sur A ou Enfant si on appuie sur B, l'autre m:b s'addapte.
    """
    display.show("?")
    while True:
        message = radio.receive()
        if button_a.is_pressed() or message == "ROLE|1|E":
            radio.send("ROLE|1|P")
            display.show("P")
            sleep(1000)
            display.clear()
            print("Parent")
            return "P"
        elif button_b.is_pressed() or message == "ROLE|1|P":
            radio.send("ROLE|1|E")
            display.show("E")
            sleep(1000)
            display.clear()
            print("Child")
            return "E"

# initialisation de l'ID et du rôle            
if not DEV_BYPASS_GET_ID:
    ID = get_id()
else:
    ID = 1


# debug - - - - - - -
# display.show(str(ID))
# sleep(1000)
# display.clear()

ROLE = get_role()

# initialisation de la m:b Enfant
if ROLE == "E":
    # initialisation de la m:b Enfant
    class Enfant:
        def __init__(self) -> None:
            self.eveil = 0

    # tout le code de la m:b Enfant ici

# initialisation de la m:b Parent
elif ROLE == "P":
    # initialisation de la m:b Parent
    class Parent:
        def __init__(self) -> None:
            pass

    # tout le code de la m:b Parent ici