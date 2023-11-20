"""
P3-SINF11BA1-A21
"""

from microbit import *
import radio

# initialisation générale
INITIAL_CHANNEL = 69
INITIAL_GROUP = 42
DEV_BYPASS_GET_ID = True # True pour faire des tests avec qu'une seule m:b
MDP = "09999:00900:00000:00000:00000"
# pour tout ce qui est image il faut les initialiser après le choix du role pour utiliser moins de mémoire

# initialisation de la radio
radio.on()
radio.config(channel=INITIAL_CHANNEL, group=INITIAL_GROUP)

class ImageMdp():
    """Classe permettant de gérer une représentation visuelle du mot de passe sur l'écran de la m:b Parent"""
    def __init__(self) -> None:
        self.StrucMdpActu = "90000:00000:00000:00000:00000"
        self.StrucMdpFin = MDP
        self.imageMdp = Image(self.StrucMdpActu)
        self.placedPinMdp = "00000:00000:00000:00000:00000"
    
    def checkEntry(self) -> bool:
        """Vérifie si le mot de passe entré est correct"""
        if self.StrucMdpFin == self.StrucMdpActu:
            return True
        else:
            return False
        
    def changeImage(self, index:int, dir) -> None:
        """Change l'image du mot de passe"""
        n = 0
        if index in [5, 11, 17, 23]:
            return False
        for _ in range(self.StrucMdpActu):
            if n == index and self.StrucMdpActu[index] == "0":
                self.StrucMdpActu = self.StrucMdpActu[:index-1] + "9" + self.StrucMdpActu[index+1:]
            if n == index and self.StrucMdpActu[index] == "9":
                self.StrucMdpActu = self.StrucMdpActu[:index-1] + "0" + self.StrucMdpActu[index+1:]
    
    def changePosition(self, dir:str):
        """Change la position du curseur"""
        for i in range(len(self.StrucMdpActu)):
            if self.StrucMdpActu[i] == "9":
                if dir == "r":
                    if i == 28:
                        self.StrucMdpActu = "00000:00000:00000:00000:00009"
                        return True
                    
                    elif self.StrucMdpActu[i+1] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i] + "0:" + "9" + self.StrucMdpActu[i+3:]
                        return True
                    
                    else:
                        self.StrucMdpActu = self.StrucMdpActu[:i] + "0" + "9" + self.StrucMdpActu[i+2:]
                        return True

                elif dir == "l":
                    if self.StrucMdpActu[i-1] == ":":
                        self.StrucMdpActu = self.StrucMdpActu[:i-2] + "9:" + "0" + self.StrucMdpActu[i+1:]
                        return True
                    else:
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
                    
    def placePinMdp(self):
        for i in range(len(self.StrucMdpActu)):
            if self.StrucMdpActu[i] == "9":
                self.placedPinMdp = self.placedPinMdp[:i-1] + "9" + self.placedPinMdp[i+1:]
                return True
            
    def showImagePinPlaced(self):
        display.show(Image(self.placedPinMdp))
        sleep(3000)
    




def get_id() -> int:
    """
    Protocole MicroID™️ permettant d'attribuer un ID (1 ou 2) à chaque micro:bit

    La microbit commence par demander si elle peut être la m:b 1. Puis, elle écoute si elle reçoit une réponse.
    Si elle reçoit la première le message d'une autre micro:bit, elle devient la m:b 2 et envoie une réponse autaurisant l'autre m:b à devenir la m:b 1.
    """
    display.show(Image("00000:00000:90909:00000:00000"))
    send_message("IDa|1|1") # est ce que je peux etre la m:b 1?
    while True:
        message = radio.receive()
        if message:
            if message == "IDa|1|1": #est ce que je peux etre la m:b 1?
                send_message("IDc|1|2") # oui, tu peux! je vais etre la m:b 2 alors!
                print("ID: 2")
                return 2
            if message == "IDc|1|2": # oui, tu peux! je vais etre la m:b 2 alors!
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
    # A FAIRE (peut etre)

def get_role() -> str:
    """
    La m:b devient Parent si on appuie sur A ou Enfant si on appuie sur B, l'autre m:b s'addapte.
    """
    display.show("?")
    while True:
        message = radio.receive()
        if button_a.is_pressed() or message == "ROLEc|1|E":
            send_message("ROLEc|1|P")
            display.show("P")
            sleep(1000)
            display.clear()
            print("Parent")
            return "P"
        elif button_b.is_pressed() or message == "ROLEc|1|P":
            send_message("ROLEc|1|E")
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
    count = 0
    imageMdp = ImageMdp()
    while True:
        display.show(Image(imageMdp.StrucMdpActu))
        if button_b.is_pressed():
            imageMdp.changePosition(dir="r")
            wait_for_button_up_not_cenceled("b")
        if button_a.is_pressed():
            imageMdp.changePosition(dir="l")
            wait_for_button_up_not_cenceled("a")
        if button_a.is_pressed() and button_b.is_pressed():
            count += 1
            sleep(1000)
            imageMdp.placePinMdp()
        if count == 4:
            check = imageMdp.checkEntry()
            if check:
                imageMdp.showImagePinPlaced()
                return True
            else:
                imageMdp.showImagePinPlaced()
                display.scroll("Mauvais Mot de Passe, recommencer")
                count == 0

def send_message(message: str) -> None:
    """
    Envoie un message à l'autre m:b 
    (le but va etre de transformer cette fonction pour qu'elle soit encryptée plus tard comme ça on ne doit pas repasser partout dans le code)
    """
    radio.send(message)

# initialisation de l'ID et du rôle
if not DEV_BYPASS_GET_ID:
    ID = get_id()
else:
    ID = 1

# debug - - - - - - - (affiche l'ID de la m:b si il y en a deux)
if not DEV_BYPASS_GET_ID:
    display.show(str(ID))
    sleep(1000)
    display.clear()

# début du programme

ROLE = get_role()

if ROLE == "E":
    # initialisation de la m:b Enfant
    class Enfant:
        """Classe contenant les methodes et attributs de la m:b Enfant"""
        def __init__(self) -> None:
            self.eveil = 0

    # tout le code de la m:b Enfant ici
    while True:
        send_message("STATUSr|6|ASLEEP")
        sleep(1500)

elif ROLE == "P":
    # initialisation de la m:b Parent
    IMAGE_SLEEP_SEQUENCE = [Image("00000:00000:99099:00000:09990"),Image("00000:99990:00900:09000:99990"), Image("09999:00090:00900:09999:00000")]

    class Parent:
        """Classe contenant les methodes et attributs de la m:b Parent"""
        def __init__(self) -> None:
            self.quantite_de_lait = 0
            self.image_lait = "00000:00000:00000:00000:00000"
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
                    display.show("F") # Find my baby

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
                        self.mode_find()

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
            display.show(IMAGE_SLEEP_SEQUENCE[1])
            while True:
                if pin_logo.is_touched():
                    self.menu()
                message = radio.receive()
                if message == "STATUSr|6|ASLEEP":
                    animation_counter += 1
                    if animation_counter % 5 == 0:
                        display.show(IMAGE_SLEEP_SEQUENCE[0])
                    elif animation_counter % 2 == 0:
                        display.show(IMAGE_SLEEP_SEQUENCE[2])
                    else:
                        display.show(IMAGE_SLEEP_SEQUENCE[1])

        def mode_find(self):
            """permet de trouver la m:b Enfant"""
            # A FAIRE (feature bonus)
            # l'idée va être de faire un jeu de chaud/froid en utilisant la force du signal radio (c'est possible)

            while not pin_logo.is_touched():
                force_signal = radio.receive_full()
                if force_signal:
                    force_signal = force_signal[1]
                    print(force_signal)
                    if force_signal < -70:
                        display.show("3")
                    elif force_signal < -50:
                        display.show("2")
                    else:
                        display.show("1")
            self.menu()
    Parent().menu()

else:
    display.show(Image.SAD)
    sleep(1000)
    # si le rôle n'est pas "P" ou "E", il y a une erreur de rôle
    display.scroll("ROLE ERROR")

