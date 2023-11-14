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

# Protocole MicroID™️
display.show(Image("00000:"
                   "00000:"
                   "90909:"
                   "00000:"
                   "00000"))
while True:
    radio.send("can i be mb1?")
    sleep(random.randint(0, 100))
    message = radio.receive()
    if message:
        if message == "can i be mb1?":
            ID =2
            radio.send("yes you can, i'm mb2!")
            # for x in range(10):
            #     sleep(random.randint(0, 10))
            #     radio.send("yes you can, i'm mb2!")
            break
        elif message == "yes you can, i'm mb2!":
            ID = 1
            break

# confirmation (A FAIRE)

display.show(str(ID))