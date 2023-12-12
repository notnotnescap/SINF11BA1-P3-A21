"""
P3-SINF11BA1-A21

Auteurs:
Johannes Edvard Radesey (nescapp sur Github) - 07042301
Arthur Backes (arthur backes sur Github) - 13512301
Hugo Restiau (HugoRst sur Github) - 46242300
Omari Johnson (243-FIREMAN) - 56542200
"""

import sys
import random
import music
import radio
# import audio
# import machine
# import speech

from microbit import button_a
from microbit import button_b
from microbit import pin_logo
from microbit import sleep
from microbit import display
from microbit import Image
from microbit import accelerometer
from microbit import temperature
# from microbit import compass

from microbit import microphone
# from microbit import i2c
# from microbit import power
# from microbit import speaker
# from microbit import spi
# from microbit import uart

BYPASS_CONNECT = False
SILENT = False
MDP = "09999:00000:00000:00000:00000"
KEY = "9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7"

radio.on()
radio.config(channel=69, group=42)

def get_role() -> str:
    """La m:b devient Parent si on appuie sur A ou Enfant si on appuie sur B, l'autre m:b s'addapte."""
    

def hashing(string):
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

def establish_secure_connection():
    """Etablit une connexion chiffrée entre les deux m:b"""
    global KEY
    if ID == 1:
        if not SILENT: music.play('g5:1')

        a = random.randint(0, 999999999) # génère un nombre aléatoire entre 0 et 999999999
        print("a: {}".format(a))

        send_packet(KEY, "SCE", a) # envoie le nombre aléatoire à la m:b 2
        superhash_of_a = hashing(hashing(str(a))) # hache le nombre aléatoire 2 fois
        print("superhash_of_a: {}".format(superhash_of_a))

        display.show(Image("00000:00000:90909:00000:00000"))

        while True: # attend la réponse de la m:b 2
            message = unpack_data(radio.receive(), KEY)
            if message and message[0] == "SCE":
                if message[2] == superhash_of_a: # si les deux nombres aléatoires hachés sont identiques, la connexion est sécurisée
                    KEY = KEY + hashing(str(a)) # crée une clé de chiffrement unique pour les deux m:b
                    sleep(500)
                    send_packet(KEY, "SCE", "CHECK") # envoie un message de confirmation à la m:b 2
                    if not SILENT: music.play('c6:1')
                    # de ce coté, la connexion est sécurisée
                    display.show(Image.YES)
                    sleep(500)
                    return
                display.show(Image.NO)
                if not SILENT: music.play('c#:1')
                sys.exit()

    if ID == 2:
        if not SILENT: music.play('e5:1')
        display.show(Image("00000:00000:90909:00000:00000"))

        while True: # attend le nombre aléatoire de la m:b 1
            message = unpack_data(radio.receive(), KEY)
            if message and message[0] == "SCE":
                break
        a = int(message[2])
        print("a: {}".format(a))

        superhash_of_a = hashing(hashing(str(a))) # hache le nombre aléatoire 2 fois
        print("superhash_of_a: {}".format(superhash_of_a))

        send_packet(KEY, "SCE", superhash_of_a) # envoie le nombre aléatoire haché à la m:b 1 pour confirmation
        KEY = KEY + hashing(str(a)) # crée une clé de chiffrement unique pour les deux m:b

        while True: # attend la confirmation de la m:b 1
            message = unpack_data(radio.receive(), KEY)
            if message and message[0] == "SCE":
                if message[2] == "CHECK": # si la m:b 1 confirme, la connexion est sécurisée
                    if not SILENT: music.play('c5:1')
                    display.show(Image.YES)
                    sleep(500)
                    return
                display.show(Image.NO)
                if not SILENT: music.play('bb:1')
                sys.exit()

def wait_for_button_up_not_cenceled(button: str) -> bool:
    """
    prend en paramètre le bouton à attendre ('a', 'b' ou 'ab')
    Attend que le bouton soit relaché et retourne True si l'autre bouton n'est pas appuyé
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
    """Encrypte ou décrypte un message avec la méthode de Vigenère)"""
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
    message = "{}|{}|{}".format(t, str(len(str(content))), str(content))
    message = vigenere(message, key)
    radio.send(message)

class ImageMdp():
    """Classe permettant de gérer une représentation visuelle du mot de passe sur l'écran de la m:b Parent"""
    def __init__(self) -> None:
        self.StrucMdpActu = "90000:00000:00000:00000:00000"
        self.StrucMdpFin = MDP
        self.imageMdp = Image(self.StrucMdpActu)
        self.placedPinMdp = "00000:00000:00000:00000:00000"

    def check_entered_password(self) -> bool:
        """Vérifie si le mot de passe entré est correct"""
        rep = False
        if self.StrucMdpFin == self.placedPinMdp:
            rep = True
        self.placedPinMdp = "00000:00000:00000:00000:00000"
        return rep

    def cursor_change_position(self, direction:str):
        """Change la position du curseur"""
        for i, digit in enumerate(self.StrucMdpActu):
            if digit == "9":
                if direction == "r":
                    if i == 28:
                        self.StrucMdpActu = "00000:00000:00000:00000:00009"
                        return True

                    if self.StrucMdpActu[i+1] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i] + "0:" + "9" + self.StrucMdpActu[i+3:]
                        return True

                    self.StrucMdpActu = self.StrucMdpActu[:i] + "0" + "9" + self.StrucMdpActu[i+2:]
                    return True

                if direction == "l":
                    if self.StrucMdpActu[i-1] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i-2] + "9:" + "0" + self.StrucMdpActu[i+1:]
                        return True

                    if self.StrucMdpActu[i-2] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i-2] + ":9" + "0" + self.StrucMdpActu[i+1:]
                    elif i == 1:
                        self.StrucMdpActu = "90000:00000:00000:00000:00000"
                        return True
                    elif i == 0:
                        self.StrucMdpActu = "90000:00000:00000:00000:00000"
                        return True
                    else:
                        self.StrucMdpActu = self.StrucMdpActu[:i-2] + "09" + "0" + self.StrucMdpActu[i+1:]
                    return True

    def place_pin_for_password(self):
        """Place un pin dans le mot de passe"""
        for i, digit in enumerate(self.StrucMdpActu):
            if digit == "9":
                if i == 0:
                    self.placedPinMdp = "9" + self.placedPinMdp[1:]
                elif i == 29:
                    self.placedPinMdp = self.placedPinMdp[0:-1] + "9"
                else:
                    if self.placedPinMdp[i-1] == ":":
                        self.placedPinMdp = self.placedPinMdp[0:i-1] + ":9" + self.placedPinMdp[i+1:]
                    else:
                        self.placedPinMdp = self.placedPinMdp[0:i] + "9" + self.placedPinMdp[i+1:]
                print(i, "index")
                print(self.placedPinMdp)
                return True

    def show_image_placed_pins(self):
        """Affiche l'image du mot de passe avec le pin placé"""
        display.show(Image(self.placedPinMdp))
        print(self.placedPinMdp)
        sleep(500)

def check_password():
    """Vérifie si le mot de passe entré est correct"""
    count = 0
    imageMdp = ImageMdp()
    while True:
        display.show(Image(imageMdp.StrucMdpActu))

        if button_a.is_pressed() and button_b.is_pressed():
            if not SILENT:
                if count > 2:
                    music.play(['c3:1'])
                else:
                    music.play(['g4:1'])
            count += 1
            imageMdp.place_pin_for_password()
            wait_for_button_up_not_cenceled("ab")

        if button_a.is_pressed():
            if wait_for_button_up_not_cenceled("a"):
                imageMdp.cursor_change_position(direction="l")
                wait_for_button_up_not_cenceled("a")

        if button_b.is_pressed():
            if wait_for_button_up_not_cenceled("b"):
                imageMdp.cursor_change_position(direction="r")
                wait_for_button_up_not_cenceled("b")

        if count == 4:
            if imageMdp.check_entered_password():
                imageMdp.show_image_placed_pins()
                display.show(Image.YES)
                sleep(500)
                display.clear()
                return True

            imageMdp.show_image_placed_pins()
            display.show(Image.NO)
            sleep(500)
            display.clear()
            count = 0

class Device:
    """Classe parente des classes Parent et Child"""
    def __init__(self, id:int) -> None:
        """Initialise la m:b (Parent ou Enfant)"""
        self.id = id # 1 ou 2

class Parent(Device):
    """Classe permettant de gérer la m:b Parent"""
    def __init__(self,id) -> None:
        """Initialise la m:b Parent"""
        super().__init__(id)
        self.quantite_de_lait = 0
        self.image_lait = "00000:00000:00000:00000:00000"
        self.index_menu = 0
        self.light = False
        self.menu_items = [("C", self.mode_compteur), # Compteur (quantité de lait)
                           ("S", self.mode_statut), # Status
                           ("T", self.mode_temperature), # Temperature
                           ("F", self.mode_find), # Find
                           ("L", self.mode_light)] # Light
        self.IMAGE_SLEEP_SEQUENCE = [Image("00000:00000:99099:00000:09990"),
                                     Image("00000:99990:00900:09000:99990"), 
                                     Image("09999:00090:00900:09999:00000")]
        check_password()
        self.menu() # Toujour mettre en dernier!

    def menu(self):
        """Affiche le menu parent"""
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
                        self.index_menu = len(self.menu_items)-1

            elif button_b.is_pressed():
                if wait_for_button_up_not_cenceled("b"):
                    self.index_menu += 1
                    if self.index_menu > len(self.menu_items)-1:
                        self.index_menu = 0

    def add_lait(self) -> None:
        """Ajoute 10ml de lait"""
        # self.image_lait = self.image_lait.replace("9", "0", 1)
        # display.show(Image(self.image_lait))
        # if self.quantite_de_lait > 0:
        #     self.quantite_de_lait -= 1
        # print(self.image_lait)
        # print(self.quantite_de_lait)

        split = self.image_lait.split(":")
        output = []
        done = False

        for i in list(split):
            if "9" in i and not done:
                last_9_index = i.rfind("9")
                output.append(i[:last_9_index] + "0" + i[last_9_index+1:])

                if self.quantite_de_lait > 0:
                    self.quantite_de_lait -= 1
                done = True
            else:
                output.append(i)

        self.image_lait = ":".join(list(output))

        print(self.image_lait)
        print(self.quantite_de_lait)
        display.show(Image(self.image_lait))

    def remove_lait(self) -> None:
        """Retire 10ml de lait"""
        split = self.image_lait.split(":")
        output = []
        done = False
        for i in list(reversed(split)):
            if "0" in i and not done:
                output.append(i.replace("0", "9", 1))
                if self.quantite_de_lait < 25:
                    self.quantite_de_lait += 1
                done = True
            else:
                output.append(i)

        self.image_lait = ":".join(list(reversed(output)))

        print(self.image_lait)
        print(self.quantite_de_lait)
        display.show(Image(self.image_lait))

    def mode_compteur(self):
        """permet de compter la quantité de lait"""
        display.show(Image(self.image_lait))
        wait_for_button_up_not_cenceled("ab")
        while not pin_logo.is_touched():
            if button_a.is_pressed() and button_b.is_pressed():
                if self.quantite_de_lait == 0:
                    display.scroll("0ml")
                else:
                    display.scroll(str(self.quantite_de_lait)+"0ml")
                display.show(Image(self.image_lait))
                sleep(1000)
                if button_a.is_pressed() and button_b.is_pressed():
                    self.image_lait = "00000:00000:00000:00000:00000"
                    self.quantite_de_lait = 0
                    send_packet(KEY, "SETQLAIT", str(self.quantite_de_lait))
                    display.show(Image(self.image_lait))
            elif button_a.is_pressed():
                if wait_for_button_up_not_cenceled("a"):
                    self.add_lait()
                    send_packet(KEY, "SETQLAIT", str(self.quantite_de_lait))
                    wait_for_button_up_not_cenceled("a")
            elif button_b.is_pressed():
                if wait_for_button_up_not_cenceled("b"):
                    self.remove_lait()
                    send_packet(KEY, "SETQLAIT", str(self.quantite_de_lait))
                    wait_for_button_up_not_cenceled("b")
        self.menu()

    def mode_statut(self):
        """permet de voir l'état de l'Enfant"""

        # animation_counter = 0
        # display.show(self.IMAGE_SLEEP_SEQUENCE[1])
        display.show("0")
        while not pin_logo.is_touched():
            message = unpack_data(radio.receive(), KEY)
            if message and message[0] == "STATUT":
                display.show(str(message[2]))
                if not SILENT:
                    if message[2] == "0":
                        music.play(['c4:1'])
                    elif message[2] == "1":
                        music.play(['e4:1'])
                    else:
                        music.play(['e5:4'])

            # if message[0] == "STATUT" and message[2] == "0":
                # animation_counter += 1
                # if animation_counter % 5 == 0:
                #     display.show(self.IMAGE_SLEEP_SEQUENCE[0])
                # elif animation_counter % 2 == 0:
                #     display.show(self.IMAGE_SLEEP_SEQUENCE[2])
                # else:
                #     display.show(self.IMAGE_SLEEP_SEQUENCE[1])
            
        self.menu()

    def mode_temperature(self):
        """Affiche la température de l'Enfant"""
        send_packet(KEY, "CMD", "GETTEMP")
        while not pin_logo.is_touched():
            message = unpack_data(radio.receive(), KEY)
            if message:
                if message[0] == "TEMP":
                    display.scroll(str(message[2]))
                    break
        self.menu()

    def mode_find(self):
        """permet de trouver la m:b Enfant"""
        send_packet(KEY, "CMD", "STARTFIND")
        while not pin_logo.is_touched():
            force_signal = radio.receive_full()
            if force_signal:
                force_signal = force_signal[1]
                print(force_signal)

                if force_signal < -120:
                    display.show("9")
                elif force_signal > -30:
                    display.show("0")
                else:
                    display.show(abs(force_signal)//10-2)

        send_packet(KEY, "CMD", "STOPFIND")
        self.menu()

    def mode_light(self):
        """permet de mettre la m:b Enfant en mode veilleuse"""
        if self.light:
            send_packet(KEY, "CMD", "STOPLIGHT")
            display.show(Image.NO)
            sleep(1000)
            display.clear()
            self.light = False
        else:
            send_packet(KEY, "CMD", "STARTLIGHT")
            display.show(Image.YES)
            sleep(1000)
            display.clear()
            self.light = True
        self.menu()

class Child(Device):
    """Classe permettant de gérer la m:b Enfant"""
    def __init__(self, id):
        """Initialise la m:b Enfant"""
        super().__init__(id)
        self.statut = 0
        self.old_statut = 0
        self.history = [0,0,0,0,0,0,0,0,0,0]
        self.playing_music = False
        self.quantite_de_lait = 0
        self.findmode = False
        self.show_statut = True
        self.main() # lance la boucle principale

    def main(self):
        """Boucle principale de la m:b Enfant"""
        previous = 0
        while True:
            for i in range(10000): # oui, c'est un peu sale, mais il n'y a pas moyen d'exécuter du code en parallèle
                message = unpack_data(radio.receive(), KEY)
                if i % 500 == 0:
                    if self.findmode: # envoyer un signal radio pour aider la m:b Parent à trouver la m:b Enfant
                        send_packet(KEY, "PING", "PING")

                    avg = (accelerometer.get_x()+accelerometer.get_y()+accelerometer.get_z()+microphone.sound_level()*100)/4
                    speed = abs((avg - previous) / 100)

                    self.history.append(speed)
                    self.history.pop(0)

                    # print("\033c")
                    agitation = sum(self.history)/len(self.history)
                    # print(agitation)
                    # print(history)

                    if agitation < 0.8:
                        self.statut = 0
                        if self.show_statut: display.show("0")
                    elif agitation < 3.0:
                        self.statut = 1
                        if self.show_statut: display.show("1")
                    elif agitation < 4.0:
                        self.statut = 2
                        if self.show_statut: display.show("2")

                    previous = avg

                if self.statut != self.old_statut:
                    send_packet(KEY, "STATUT", str(self.statut))
                    self.old_statut = self.statut

                if button_b.is_pressed() and self.statut > 0:
                    if not self.playing_music:
                        music.play(music.PYTHON, wait=False)
                        self.playing_music = True
                    else:
                        music.stop()
                        self.playing_music = False
                    wait_for_button_up_not_cenceled("b")
                if button_a.is_pressed():
                    if self.quantite_de_lait == 0:
                        display.scroll("0ml")
                    else:
                        display.scroll(str(self.quantite_de_lait)+"0ml")

                    if not self.show_statut:
                        display.show(Image("99999:99999:99999:99999:99999"))

                if message:
                    if message[0] == "CMD":
                        if message[2] == "GETTEMP":
                            sleep(100)
                            send_packet(KEY, "TEMP", str(temperature()))
                            print("TEMP: {}".format(temperature()))
                        elif message[2] == "STARTFIND":
                            self.findmode = True
                        elif message[2] == "STOPFIND":
                            self.findmode = False
                        elif message[2] == "STARTLIGHT":
                            display.show(Image("99999:99999:99999:99999:99999"))
                            self.show_statut = False
                        elif message[2] == "STOPLIGHT":
                            display.clear()
                            self.show_statut = True
                    elif message[0] == "SETQLAIT":
                        self.quantite_de_lait = int(message[2])
                        print("SETQLAIT: {}".format(self.quantite_de_lait))

if not SILENT: music.play('c6:1')

if not BYPASS_CONNECT:
    # identification de la m:b 1 et 2
    display.show(Image("00000:00000:90909:00000:00000"))
    send_packet(KEY, "ID", "ASK") # est ce que je peux etre la m:b 1?
    while True:
        message = unpack_data(radio.receive(), KEY)
        if message:
            if message[0] == "ID" and message[2] == "ASK": #est ce que je peux etre la m:b 1?
                send_packet(KEY, "ID", "CONF") # oui, tu peux! je vais etre la m:b 2 alors!
                print("ID: 2")
                if not SILENT: music.play('c6:1')
                ID = 2
                break
            if message[0] == "ID" and message[2] == "CONF": # oui, tu peux! je vais etre la m:b 2 alors!
                print("ID: 1")
                if not SILENT: music.play('c5:1')
                ID = 1
                break
    display.show(str(ID))
    sleep(500)
    display.clear()
    establish_secure_connection()
else:
    ID = 0

# choix du rôle de la m:b

display.show("?")
while True:
    message = unpack_data(radio.receive(), KEY)
    if button_a.is_pressed() or message and message[0] == "ROLE" and message[2] == "P":
        send_packet(KEY, "ROLE", "E")
        display.show("P")
        sleep(1000)
        display.clear()
        print("Parent")
        if not SILENT: music.play('g5:1')
        device = Parent(ID)
        break
    if button_b.is_pressed() or message and message[0] == "ROLE" and message[2] == "E":
        send_packet(KEY, "ROLE", "P")
        display.show("E")
        sleep(1000)
        display.clear()
        print("Child")
        if not SILENT: music.play('e5:1')
        device = Child(ID)
        break
