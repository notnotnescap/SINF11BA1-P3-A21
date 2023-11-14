"""
P3-SINF11BA1-A21
"""

from microbit import *
import radio
import random

# initialisation
INITIAL_CHANNEL = 69
INITIAL_GROUP = 42

radio.on()
radio.config(channel=INITIAL_CHANNEL, group=INITIAL_GROUP)

def get_id() -> int:
    """
    Protocole MicroID™️ permettant d'attribuer un ID (1 ou 2) à chaque micro:bit
    """
    display.show(Image("00000:""00000:""90909:""00000:""00000"))
    while True:
        radio.send("ID|1|1") # can i be mb1?
        sleep(random.randint(0, 100))
        message = radio.receive()
        if message:
            if message == "ID|1|1": #can i be mb1?
                radio.send("ID|1|2") # yes you can, i'm mb2!
                print("ID: 2")
                return 2
            elif message == "ID|1|2": # yes you can, i'm mb2!
                print("ID: 1")
                return 1

    # confirmation (A FAIRE) parce que oui, il existen encore un micro possibilité que les deux micro:bit envoient en même temps le message "ID|1|1" 

def check_connection() -> bool:
    """
    Vérifie si la connexion est toujours active
    """
    # A FAIRE
    pass

def get_role() -> str:
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
            

ID = get_id()
# debug
# display.show(str(ID))
# sleep(3000)
display.clear()
ROLE = get_role()
