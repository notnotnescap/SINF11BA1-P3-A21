"""
P3-SINF11BA1-A21
"""

from microbit import *
import radio

# initialisation

INITIAL_CHANNEL = 69
INITIAL_GROUP = 42

radio.on()
radio.config(channel=INITIAL_CHANNEL, group=INITIAL_GROUP)

while True:
    if button_a.is_pressed():
        radio.send("1")
    message = radio.receive()
    if message == "1":
        display.show(Image.HAPPY)
        sleep(10)
    else:
        display.clear()
