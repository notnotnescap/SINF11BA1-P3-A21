"""
P3-SINF11BA1-A21
"""

import random
from microbit import *
import radio

# initialisation générale
INITIAL_CHANNEL = 69
INITIAL_GROUP = 42
DEV_BYPASS_GET_ID = True # True pour faire des tests avec qu'une seule m:b
MDP = "00900:00900:00900:00900:00900"
IMAGE_SLEEP_SEQUENCE = [Image("00000:""00000:""99099:""00000:""09990"),Image("00000:""99990:""00900:""09000:""99990"), Image("09999:""00090:""00900:""09999:""00000")]

radio.on()
radio.config(channel=INITIAL_CHANNEL, group=INITIAL_GROUP)

class ImageMdp():
    def __init__(self) -> None:
        self.StrucMdpActu = "90000:00000:00000:00000:00000"
        self.StrucMdpFin = MDP
        self.imageMdp = Image(self.StrucMdpActu)
    
    def checkEntry(self) -> bool:
        if self.StrucMdpFin == self.StrucMdpActu:
            return True
        else:
            return False
        
    def changeImage(self, index:int, dir) -> None:
        n = 0
        if index in [5, 11, 17, 23]:
            return False
        for i in range(self.StrucMdpActu):
            if n == index and self.StrucMdpActu[index] == "0":
                self.StrucMdpActu = self.StrucMdpActu[:index-1] + "9" + self.StrucMdpActu[index+1:]
            if n == index and self.StrucMdpActu[index] == "9":
                self.StrucMdpActu = self.StrucMdpActu[:index-1] + "0" + self.StrucMdpActu[index+1:]
    
    def changePosition(self, dir:str):
        for i in range(len(self.StrucMdpActu)):
            if self.StrucMdpActu[i] == "9":
                print(i)
                if dir == "r":
                    if i == 28:
                        self.StrucMdpActu = "00000:00000:00000:00000:00009"
                        print(self.StrucMdpActu)
                        return True
                    
                    elif self.StrucMdpActu[i+1] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i] + "0:" + "9" + self.StrucMdpActu[i+3:]
                        print(self.StrucMdpActu)
                        return True
                    
                    else:
                        self.StrucMdpActu = self.StrucMdpActu[:i] + "0" + "9" + self.StrucMdpActu[i+2:]
                        print(self.StrucMdpActu)
                        return True

                elif dir == "l":
                    if self.StrucMdpActu[i-1] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i-2] + "9:" + "0" + self.StrucMdpActu[i+1:]
                        print(self.StrucMdpActu)
                        return True
                    else:
                        if self.StrucMdpActu[i-2] == ":":
                            self.StrucMdpActu = self.StrucMdpActu[:i-2] + ":9" + "0" + self.StrucMdpActu[i+1:]
                        elif i == 1:
                            self.StrucMdpActu = "90000:00000:00000:00000:00000"
                            print(self.StrucMdpActu)
                            return True
                        elif i == 0:
                            self.StrucMdpActu = "90000:00000:00000:00000:00000"
                            print(self.StrucMdpActu)
                            return True
                        else:
                            self.StrucMdpActu = self.StrucMdpActu[:i-2] + "09" + "0" + self.StrucMdpActu[i+1:]
                        print(self.StrucMdpActu)
                        return True
                    
    

        



class ImageCompteurLait():
    """Classe permettant de gérer une représentation visuelle de la quantité de lait sur l'écran de la m:b Parent"""
    def __init__(self) -> None:
        self.imageStruc = "00000:""00000:""00000:""00000:""00000"
        self.image = Image(self.imageStruc)

    def showImage(self):
        """Retourne l'image de la quantité de lait"""
        return Image(self.imageStruc)

    def checkStruc(self):
        """Retourne l'index du premier 0 dans la structure de l'image"""
        n = 0
        for i in self.imageStruc:
            if str(i).isdigit():
                if i == "0":
                    return n
            n+=1
        return n
    
    def addPin(self) -> None:
        """Ajoute un point à la représentation visuelle de la quantité de lait"""
        n = self.checkStruc()
        if n > 28:
            pass
        else:
            print("OUI") # on peut retirer ?
            self.imageStruc = self.imageStruc[:n] + "9" + self.imageStruc[n + 1:]
        self.image = Image(self.imageStruc)
        print("[INFO] STRUCTURE IMAGE", self.imageStruc)

    def removePin(self) -> None:
        """Retire un point à la représentation visuelle de la quantité de lait"""
        n = self.checkStruc()
        print(n)
        if n > 28:
            self.imageStruc = "99999:""99999:""99999:""99999:""99990"
        elif n == 0:
            pass
        else:
            if n in [6, 12, 18, 24]:
                self.imageStruc = self.imageStruc[:n-2] + "0:" + self.imageStruc[n:]
            else:
                self.imageStruc = self.imageStruc[:n-1] + "0" + self.imageStruc[n:]
        self.image = Image(self.imageStruc)
        print("[INFO] STRUCTURE IMAGE", self.imageStruc)


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
        else:
            return True
    elif button.lower() == "b":
        while button_b.is_pressed() and not button_a.is_pressed():
            pass
        if button_a.is_pressed():
            return False
        else:
            return True
    elif button.lower() == "ab":
        while button_a.is_pressed() or button_b.is_pressed():
            pass
def check_mdp():
    imageMdp = ImageMdp()
    while True:
        display.show(Image(imageMdp.StrucMdpActu))
        if button_b.is_pressed():
            imageMdp.changePosition(dir="r")
            wait_for_button_up_not_cenceled("b")
        if button_a.is_pressed():
            imageMdp.changePosition(dir="l")
            wait_for_button_up_not_cenceled("a")
        check = imageMdp.checkEntry()
        if check:
            return True

# initialisation de l'ID et du rôle

if not DEV_BYPASS_GET_ID:
    ID = get_id()
else:
    ID = 1


# debug - - - - - - -
if not DEV_BYPASS_GET_ID:
    display.show(str(ID))
    sleep(1000)
    display.clear()

ROLE = get_role()

# initialisation de la m:b Enfant
if ROLE == "E":
    # initialisation de la m:b Enfant
    class Enfant:
        """Classe contenant les methodes et attributs de la m:b Enfant"""
        def __init__(self) -> None:
            self.eveil = 0

    # tout le code de la m:b Enfant ici
    while True:
        radio.send("STATUS|6|ASLEEP")
        sleep(1500)

# initialisation de la m:b Parent
elif ROLE == "P":
    # initialisation de la m:b Parent
    class Parent:
        """Classe contenant les methodes et attributs de la m:b Parent"""
        def __init__(self) -> None:
            self.quantite_de_lait = 0
            self.index_menu = 0

        def menu(self):
            """permet de choisir le mode"""
            # l'idéal serait d'utiliser un dictionnaire
            # Pour l'instant il y a 4 modes: A,B,C,D (pour les tests)
            # ils auront des noms plus tard

            # le pin_logo agit comme un bouton d'accueil (pour revenir au menu)
            check_mdp()
            display.clear()
            sleep(500)

            while True:
                if self.index_menu == 0:
                    display.show("L") # Lait
                elif self.index_menu == 1:
                    display.show("S") # Statut
                elif self.index_menu == 2:
                    display.show("T") # Température
                elif self.index_menu == 3:
                    display.show("R") # Recherche

                if button_a.is_pressed() and button_b.is_pressed():
                    # pour sélectionner le mode il faut appuyer sur A et B en même temps
                    display.clear()
                    # sleep(1000)
                    # display.show(self.index_menu) # affiche le mode sélectionné (dans le futur, affichera le nom du mode)
                    # sleep(1000)

                    # et ici le programme devra lancer le mode selon l'index du menu sélectionné
                    # pour l'instant, peu importe l'index, il lance le mode compteur (qui n'est pas encore fait et affiche juste un "?")

                    # self.mode_compteur()
                    display.clear()
                    sleep(500)
                    if self.index_menu == 1:
                        self.mode_status()
                    if self.index_menu == 0:
                        self.mode_compteur()
                    if self.index_menu == 3:
                        self.mode_recherche()

                elif button_a.is_pressed():
                    if wait_for_button_up_not_cenceled("a"):
                        # cette fonction attend juste que le bouton soit relaché et s'assure qu'on a pas essayé d'appuyer sur A et B en même temps
                        # sinon il faut timer parfaitement l'appui sur les deux boutons et c'est horrible
                        self.index_menu -= 1
                        if self.index_menu < 0:
                            self.index_menu = 3 # ici dans le futur il faudra mettre la longueur du dictionnaire du menu

                elif button_b.is_pressed():
                    if wait_for_button_up_not_cenceled("b"):
                        self.index_menu += 1
                        if self.index_menu > 3:
                            self.index_menu = 0

        def mode_compteur(self):
            """permet de compter la quantité de lait"""
            # le pin_logo agit comme un bouton d'accueil (pour revenir au menu)
            imageLait = ImageCompteurLait()

            # moyen idéal est de tout gérer dans une seule fonction
            for x in range(self.quantite_de_lait):
                display.show(Image(imageLait.imageStruc))
                imageLait.addPin()
                sleep(20)

            while True:
                display.show(Image(imageLait.imageStruc))
                if button_b.is_pressed():
                    display.show(Image(imageLait.imageStruc))
                    imageLait.addPin()
                    if self.quantite_de_lait < 25:
                        self.quantite_de_lait += 1
                    wait_for_button_up_not_cenceled("b")

                if button_a.is_pressed():
                    display.show(Image(imageLait.imageStruc))
                    imageLait.removePin()
                    if self.quantite_de_lait > 0:
                        self.quantite_de_lait -= 1
                    wait_for_button_up_not_cenceled("a")

                if pin_logo.is_touched():
                    self.menu()



        def mode_status(self):
            """permet de voir l'état de l'Enfant"""
            # NOT DEBUGGED YET
            animation_counter = 0
            display.show(IMAGE_SLEEP_SEQUENCE[1])
            while True:
                if pin_logo.is_touched():
                    self.menu()
                message = radio.receive()
                if message == "STATUS|6|ASLEEP":
                    animation_counter += 1
                    if animation_counter % 5 == 0:
                        display.show(IMAGE_SLEEP_SEQUENCE[0])
                    elif animation_counter % 2 == 0:
                        display.show(IMAGE_SLEEP_SEQUENCE[2])
                    else:
                        display.show(IMAGE_SLEEP_SEQUENCE[1])

        def mode_recherche(self):
            """permet de trouver la m:b Enfant"""
            # A FAIRE (feature bonus)
            # l'idée va être de faire un jeu de chaud/froid en utilisant la force du signal radio (c'est possible)
            while not pin_logo.is_touched():
                if radio.receive_full():
                    force_signal = radio.receive_full()
                    print(force_signal)
                # if force_signal > -50:
                #     display.show("3")
                # elif force_signal > -100:
                #     display.show("2")
                # else:
                #     display.show("1")
            self.menu()
    Parent().menu()
