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
    display.show(Image("00000:"
                    "00000:"
                    "90909:"
                    "00000:"
                    "00000"))
    while True:
        radio.send("ID|1|1") # can i be mb1?
        sleep(random.randint(0, 100))
        message = radio.receive()
        if message:
            if message == "ID|1|1": #can i be mb1?
                radio.send("ID|1|2") # yes you can, i'm mb2!
                return 2
            elif message == "ID|1|2": # yes you can, i'm mb2!
                return 1

    # confirmation (A FAIRE)

def check_connection() -> bool:
    """
    Vérifie si la connexion est toujours active
    """
    # A FAIRE
    pass

ID = get_id()