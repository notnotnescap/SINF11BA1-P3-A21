"""
P3-SINF11BA1-A21

Johannes Edvard Radesey (nescapp sur Github) - 07042301
-> Arthur Backes (arthur backes sur Github) - 13512301
-> ... (à compléter)
-> ... (à compléter)
"""
# Basics

# from microbit import button_a
# from microbit import button_b
# from microbit import pin_logo
# from microbit import sleep
# from microbit import display
# from microbit import Image
# # from microbit import accelerometer
# # from microbit import compass

# # from microbit import i2c
# # from microbit import microphone
# # from microbit import power
# # from microbit import speaker
# # from microbit import spi
# # from microbit import uart

# # Extended

# # import audio
# # import machine
# # import music
# # import neopixel
# # import os
# import radio
# # import random
# # import speech

class Device:
    def __init__(self, initial_channel, initial_group) -> None:
        self.channel = initial_channel
        self.group = initial_group
        # radio.on()
        # radio.config(channel=self.channel, group=self.group)

    def change_channel(self, new_channel):
        self.channel = new_channel
        radio.config(channel=self.channel)

    def change_group(self, new_group):
        self.group = new_group
        radio.config(group=self.group)

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

    def receive_packet(self, packet_received, key):
        """
        Traite les paquets reçus via l'interface radio du micro:bit
        Cette fonction utilise la fonction unpack_data pour renvoyer les différents champs du message passé en paramètre
        Si une erreur survient, les 3 champs sont retournés vides

        :param (str) packet_received: Paquet reçue
            (str) key:              Clé de chiffrement
        :return (srt)type:             Type de paquet
                (int)lenght:           Longueur de la donnée en caractère
                (str) message:         Données reçue
        """
        type, lenght, message = self.unpack_data(packet_received, key)
        return None
    

    def get_id(self):
        display.show(Image("00000:00000:90909:00000:00000"))
        self.send_packet("DEFAULT", "ID", "ASK") # est ce que je peux etre la m:b 1?
        while True:
            message = radio.receive()
            if message:
                if message == "IDa|1|1": #est ce que je peux etre la m:b 1?
                    self.send_packet("IDc|1|2") # oui, tu peux! je vais etre la m:b 2 alors!
                    print("ID: 2")
                    return 2
                if message == "IDc|1|2": # oui, tu peux! je vais etre la m:b 2 alors!
                    print("ID: 1")
                    return 1

class Parent(Device):
    def __init__(self) -> None:
        pass

class Child(Device):
    def __init__(self) -> None:
        pass

test = Device(1,1)
print(test.unpack_data("LH|8|LLN", "DEFAULT"))