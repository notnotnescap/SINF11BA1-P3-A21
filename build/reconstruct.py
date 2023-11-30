"""
P3-SINF11BA1-A21

Johannes Edvard Radesey (nescapp sur Github) - 07042301
Arthur Backes (arthur backes sur Github) - 13512301
Hugo Restiau (HugoRst sur Github) - 46242300
-> ... (à compléter)
"""
# Basics

from microbit import button_a
from microbit import button_b
from microbit import pin_logo
from microbit import sleep
from microbit import display
from microbit import Image
# from microbit import accelerometer
# from microbit import compass

# from microbit import i2c
# from microbit import microphone
# from microbit import power
# from microbit import speaker
# from microbit import spi
# from microbit import uart

# Extended

# import audio
# import machine
# import music
# import neopixel
# import os
import radio
# import random
# import speech

BYPASS_GET_ID = True
defaultkey = "test"

radio.on()
radio.config(channel=69, group=42)

def get_id() -> int:
    display.show(Image("00000:00000:90909:00000:00000"))
    send_packet(defaultkey, "ID", "ASK") # est ce que je peux etre la m:b 1?
    while True:
        message = unpack_data(radio.receive(), defaultkey)
        print(message)
        # message = radio.receive()
        if message:
            if message[0] == "ID" and message[2] == "ASK": #est ce que je peux etre la m:b 1?
            # if message == "ASK":
                send_packet(defaultkey, "ID", "CONF") # oui, tu peux! je vais etre la m:b 2 alors!
                print("ID: 2")
                return 2
            if message[0] == "ID" and message[2] == "CONF": # oui, tu peux! je vais etre la m:b 2 alors!
            # if message == "CONF":
                print("ID: 1")
                return 1

def get_role(d:'Device') -> str:
    """
    La m:b devient Parent si on appuie sur A ou Enfant si on appuie sur B, l'autre m:b s'addapte.
    """
    display.show("?")
    while True:
        message = radio.receive()
        if button_a.is_pressed() or message == "E":
            send_packet(d.key, "ROLE", "E")
            display.show("P")
            sleep(1000)
            display.clear()
            print("Parent")
            return "P"
        if button_b.is_pressed() or message == "P":
            send_packet(d.key, "ROLE", "P")
            display.show("E")
            sleep(1000)
            display.clear()
            print("Child")
            return "E"

def wait_for_button_up_not_cenceled(button: str) -> bool:
    """
    prend en paramètre le bouton à attendre (a, b ou ab)
    Attend que le bouton soit relaché
    """
    if button.lower() == "a":
        while button_a.is_pressed() and not button_b.is_pressed():
            pass
        if button_b.is_pressed():
            return False
        return True
    if button.lower() == "b":
        while button_b.is_pressed() and not button_a.is_pressed():
            pass
        if button_a.is_pressed():
            return False
        return True
    if button.lower() == "ab":
        while button_a.is_pressed() or button_b.is_pressed():
            pass

def vigenere(message:str, key:str, decryption:bool=False):
    text = ""
    key_length = len(key)
    key_as_int = [ord(k) for k in key]

    for i, char in enumerate(str(message)):
        #Letters encryption/decryption
        if char.isalpha():
            key_index = i % key_length
            if decryption:
                modified_char = chr((ord(char.upper()) - key_as_int[key_index] + 26) % 26 + ord('A'))
            else : 
                modified_char = chr((ord(char.upper()) + key_as_int[key_index] - 26) % 26 + ord('A'))
            #Put back in lower case if it was
            if char.islower():
                modified_char = modified_char.lower()
            text += modified_char
        #Digits encryption/decryption
        elif char.isdigit():
            key_index = i % key_length
            if decryption:
                modified_char = str((int(char) - key_as_int[key_index]) % 10)
            else:  
                modified_char = str((int(char) + key_as_int[key_index]) % 10)
            text += modified_char
        else:
            text += char
    return text

def unpack_data(encrypted_packet:str, key:str):
    """
    Déballe et déchiffre les paquets reçus via l'interface radio du micro:bit
    Cette fonction renvoit les différents champs du message passé en paramètre

    :param (str) encrypted_packet: Paquet reçu
        (str) key:              Clé de chiffrement
    :return (srt)type:             Type de paquet
            (int)length:           Longueur de la donnée en caractères
            (str) message:         Données reçue
    """
    if not encrypted_packet:
        return None
    data = vigenere(encrypted_packet, key, True).split("|")
    try:
        t = data[0]
        try:
            lenght = int(data[1])
        except ValueError:
            lenght = None
        message = data[2]
        return t, lenght, message
    except IndexError:
        print("Mauvais packet reçu : {}".format(data))
        return None, None, None

def send_packet(key:str, t:str, content:str):
    """
    Envoi de données fournies en paramètres
    Cette fonction permet de construire, de chiffrer puis d'envoyer un paquet via l'interface radio du micro:bit

    :param (str) key:       Clé de chiffrement
        (str) type:      Type du paquet à envoyer
        (str) content:   Données à envoyer
    :return none
    """
    message = "{}|{}|{}".format(t, str(len(content)), content)
    message = vigenere(message, key)
    radio.send(message)

class Device:
    def __init__(self) -> None:
        # self.channel = 69
        # self.group = 42
        self.key = "test"
        self.id = 0

        if not BYPASS_GET_ID:
            display.show(str(self.id))
            sleep(500)
            display.clear()



    # def set_key(self, new_key:str) -> None:
    #     self.key = self.hashing(new_key)

    # def hashing(self, string):
    #     """
    #     Hachage d'une chaîne de caractères fournie en paramètre.
    #     Le résultat est une chaîne de caractères.
    #     Attention : cette technique de hachage n'est pas suffisante (hachage dit cryptographique) pour une utilisation en dehors du cours.

    #     :param (str) string: la chaîne de caractères à hacher
    #     :return (str): le résultat du hachage
    #     """
    #     def to_32(value):
    #         """
    #         Fonction interne utilisée par hashing.
    #         Convertit une valeur en un entier signé de 32 bits.
    #         Si 'value' est un entier plus grand que 2 ** 31, il sera tronqué.

    #         :param (int) value: valeur du caractère transformé par la valeur de hachage de cette itération
    #         :return (int): entier signé de 32 bits représentant 'value'
    #         """
    #         value = value % (2 ** 32)
    #         if value >= 2**31:
    #             value = value - 2 ** 32
    #         value = int(value)
    #         return value

    #     if string:
    #         x = ord(string[0]) << 7
    #         m = 1000003
    #         for c in string:
    #             x = to_32((x*m) ^ ord(c))
    #         x ^= len(string)
    #         if x == -1:
    #             x = -2
    #         return str(x)
    #     return ""

class Parent(Device):
    def __init__(self) -> None:
        display.show("i")
        super().__init__()
        self.quantite_de_lait = 0
        self.image_lait = "00000:00000:00000:00000:00000"
        self.index_menu = 0
        self.menu_items = [("L", self.mode_compteur), # Lait
                        ("S", self.mode_status), # Status
                        ("T", self.mode_temperature), # Temperature
                        ("F", self.mode_find)] # Find
        self.IMAGE_SLEEP_SEQUENCE = [Image("00000:00000:99099:00000:09990"),
                                     Image("00000:99990:00900:09000:99990"), 
                                     Image("09999:00090:00900:09999:00000")]
        self.menu()

    def menu(self):
        display.clear()
        sleep(100)

        while True:
            display.show(self.menu_items[self.index_menu][0])

            if button_a.is_pressed() and button_b.is_pressed():
                # pour sélectionner le mode il faut appuyer sur A et B en même temps
                display.clear()
                sleep(100)
                self.menu_items[self.index_menu][1]()

            elif button_a.is_pressed():
                if wait_for_button_up_not_cenceled("a"):
                    self.index_menu -= 1
                    if self.index_menu < 0:
                        self.index_menu = 3 # ici dans le futur il faudra mettre la longueur du dictionnaire du menu

            elif button_b.is_pressed():
                if wait_for_button_up_not_cenceled("b"):
                    self.index_menu += 1
                    if self.index_menu > 3:
                        self.index_menu = 0

    def add_lait(self) -> None:
        """Ajoute 1 unité de lait"""
        self.image_lait = self.image_lait.replace("9", "0", 1)
        display.show(Image(self.image_lait))
        if self.quantite_de_lait > 0:
            self.quantite_de_lait -= 1
        print(self.image_lait)
        print(self.quantite_de_lait)

    def remove_lait(self) -> None:
        """Retire 1 unité de lait"""
        last_zero_index = self.image_lait.rfind("0")
        if last_zero_index != -1:
            self.image_lait = self.image_lait[:last_zero_index] + "9" + self.image_lait[last_zero_index+1:]
        display.show(Image(self.image_lait))
        if self.quantite_de_lait < 25:
            self.quantite_de_lait += 1
        print(self.quantite_de_lait)
        print(self.image_lait)
        print(self.quantite_de_lait)

    def mode_compteur(self):
        """permet de compter la quantité de lait"""
        display.show(Image(self.image_lait))
        wait_for_button_up_not_cenceled("ab")
        while True:
            if pin_logo.is_touched():
                self.menu()
            if button_a.is_pressed() and button_b.is_pressed():
                display.scroll(str(self.quantite_de_lait))
                display.show(Image(self.image_lait))
                sleep(1000)
                if button_a.is_pressed() and button_b.is_pressed():
                    self.image_lait = "00000:00000:00000:00000:00000"
                    self.quantite_de_lait = 0
                    display.show(Image(self.image_lait))
            elif button_a.is_pressed():
                if wait_for_button_up_not_cenceled("a"):
                    self.add_lait()
                    wait_for_button_up_not_cenceled("a")
            elif button_b.is_pressed():
                if wait_for_button_up_not_cenceled("b"):
                    self.remove_lait()
                    wait_for_button_up_not_cenceled("b")

    def mode_status(self):
        """permet de voir l'état de l'Enfant"""

        animation_counter = 0
        display.show(self.IMAGE_SLEEP_SEQUENCE[1])
        while True:
            if pin_logo.is_touched():
                self.menu()
            message = radio.receive()
            if message == "STATUSr|6|ASLEEP":
                animation_counter += 1
                if animation_counter % 5 == 0:
                    display.show(self.IMAGE_SLEEP_SEQUENCE[0])
                elif animation_counter % 2 == 0:
                    display.show(self.IMAGE_SLEEP_SEQUENCE[2])
                else:
                    display.show(self.IMAGE_SLEEP_SEQUENCE[1])

    def mode_temperature(self):
        while not pin_logo.is_touched():
            display.show("x")
        self.menu()

    def mode_find(self):
        """permet de trouver la m:b Enfant"""
        while not pin_logo.is_touched():
            force_signal = radio.receive_full()
            if force_signal:
                force_signal = force_signal[1]
                print(force_signal)

                if force_signal < -120:
                    display.show("9")
                elif force_signal > -40:
                    display.show("0")
                else:
                    display.show(abs(force_signal)//10-2)

        self.menu()

class Child(Device):
    def __init__(self) -> None:
        super().__init__()
        self.statut = 0
        self.main()

    def main(self):
        while True:
            send_packet(self.key, "STATUT", self.statut)
            sleep(1000)


device = Device()
if not BYPASS_GET_ID:
    ID = get_id()
else:
    ID = 0
device.id = ID
# get_role(device)


if get_role(device) == "P":
    device = Parent()
else:
    device = Child()
