"""
P3-SINF11BA1-A21

Johannes Edvard Radesey (nescapp sur Github) - 07042301
-> Arthur Backes (arthur backes sur Github) - 13512301
-> ... (à compléter)
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

BYPASS_GET_ID = False

class Device:
    def __init__(self, initial_channel, initial_group) -> None:
        self.__channel = initial_channel
        self.__group = initial_group
        self.set_key("kJg3ogEGePTKxPZnPByntA6SyYkSpLf2s7jDfy3v")

        if not BYPASS_GET_ID:
            self.id = self.get_id()
        else:
            self.id = 0

        if not BYPASS_GET_ID:
            display.show(str(self.id))
            sleep(500)
            display.clear()

        radio.on()
        radio.config(channel=self.__channel, group=self.__group)

    def set_channel(self, new_channel:int) -> None:
        self.__channel = new_channel
        radio.config(channel=self.__channel)

    def set_group(self, new_group:int) -> None:
        self.__group = new_group
        radio.config(group=self.__group)

    def set_key(self, new_key:str) -> None:
        self.__key = self.hashing(new_key)

    def hashing(self, string):
        """
        Hachage d'une chaîne de caractères fournie en paramètre.
        Le résultat est une chaîne de caractères.
        Attention : cette technique de hachage n'est pas suffisante (hachage dit cryptographique) pour une utilisation en dehors du cours.

        :param (str) string: la chaîne de caractères à hacher
        :return (str): le résultat du hachage
        """
        def to_32(value):
            """
            Fonction interne utilisée par hashing.
            Convertit une valeur en un entier signé de 32 bits.
            Si 'value' est un entier plus grand que 2 ** 31, il sera tronqué.

            :param (int) value: valeur du caractère transformé par la valeur de hachage de cette itération
            :return (int): entier signé de 32 bits représentant 'value'
            """
            value = value % (2 ** 32)
            if value >= 2**31:
                value = value - 2 ** 32
            value = int(value)
            return value

        if string:
            x = ord(string[0]) << 7
            m = 1000003
            for c in string:
                x = to_32((x*m) ^ ord(c))
            x ^= len(string)
            if x == -1:
                x = -2
            return str(x)
        return ""
        
    def vigenere(self, message:str, key:str, decryption:bool=False):
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

    def send_packet(self, key:str, type:str, content:str):
        """
        Envoi de données fournies en paramètres
        Cette fonction permet de construire, de chiffrer puis d'envoyer un paquet via l'interface radio du micro:bit

        :param (str) key:       Clé de chiffrement
            (str) type:      Type du paquet à envoyer
            (str) content:   Données à envoyer
        :return none
        """
        message = f"{type}|{len(content)}|{content}"
        message = self.vigenere(message, key)
        radio.send(message)

    def unpack_data(self, encrypted_packet:str, key:str):
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
        data = self.vigenere(encrypted_packet, key, True).split("|")
        try:
            type = data[0]
            try:
                lenght = int(data[1])
            except ValueError:
                lenght = None
            message = data[2]
            return type, lenght, message
        except IndexError:
            print(f"Mauvais packet reçu : {data}")
            return None, None, None

    def get_id(self):
        display.show(Image("00000:00000:90909:00000:00000"))
        self.send_packet(self.__key, "ID", "ASK") # est ce que je peux etre la m:b 1?
        while True:
            message = self.unpack_data(radio.receive(), self.__key)
            if message:
                if message[0] == "ID" and message[1] == "ASK": #est ce que je peux etre la m:b 1?
                    self.send_packet(self.__key, "ID", "CONF") # oui, tu peux! je vais etre la m:b 2 alors!
                    print("ID: 2")
                    return 2
                if message[0] == "ID" and message[1] == "CONF": # oui, tu peux! je vais etre la m:b 2 alors!
                    print("ID: 1")
                    return 1

class Parent(Device):
    def __init__(self) -> None:
        pass

class Child(Device):
    def __init__(self) -> None:
        self.statut = 0

    def main():
        self.send_packet(self.__key, "STATUT", self.statut)

this_device = Device(69, 42)
this_device.get_id()
