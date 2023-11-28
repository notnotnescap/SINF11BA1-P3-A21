'\nP3-SINF11BA1-A21\n\nJohannes Edvard Radesey (nescapp sur Github) - 07042301\n-> ... (à compléter)\n-> ... (à compléter)\n-> ... (à compléter)\n'
_G='STATUSr|6|ASLEEP'
_F=False
_E='00000:00000:00000:00000:00000'
_D='90000:00000:00000:00000:00000'
_C='0'
_B='9'
_A=True
from microbit import button_a,button_b,pin_logo,sleep,display,Image
import radio
INITIAL_CHANNEL=69
INITIAL_GROUP=42
DEV_BYPASS_GET_ID=_A
MDP='09999:00900:00000:00000:00000'
radio.on()
radio.config(channel=INITIAL_CHANNEL,group=INITIAL_GROUP)
class ImageMdp:
	"Classe permettant de gérer une représentation visuelle du mot de passe sur l'écran de la m:b Parent"
	def __init__(A):A.StrucMdpActu=_D;A.StrucMdpFin=MDP;A.imageMdp=Image(A.StrucMdpActu);A.placedPinMdp=_E
	def check_entry(A):'Vérifie si le mot de passe entré est correct';return A.StrucMdpFin==A.StrucMdpActu
	def change_image(A,index,dir):
		"Change l'image du mot de passe";B=index;C=0
		if B in[5,11,17,23]:return _F
		for D in range(A.StrucMdpActu):
			if C==B and A.StrucMdpActu[B]==_C:A.StrucMdpActu=A.StrucMdpActu[:B-1]+_B+A.StrucMdpActu[B+1:]
			if C==B and A.StrucMdpActu[B]==_B:A.StrucMdpActu=A.StrucMdpActu[:B-1]+_C+A.StrucMdpActu[B+1:]
	def change_position(A,dir):
		'Change la position du curseur';C=':'
		for(B,D)in enumerate(A.StrucMdpActu):
			if D==_B:
				if dir=='r':
					if B==28:A.StrucMdpActu='00000:00000:00000:00000:00009';return _A
					if A.StrucMdpActu[B+1]==C:A.StrucMdpActu=A.StrucMdpActu[:B]+'0:'+_B+A.StrucMdpActu[B+3:];return _A
					A.StrucMdpActu=A.StrucMdpActu[:B]+_C+_B+A.StrucMdpActu[B+2:];return _A
				if dir=='l':
					if A.StrucMdpActu[B-1]==C:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'9:'+_C+A.StrucMdpActu[B+1:];return _A
					if A.StrucMdpActu[B-2]==C:A.StrucMdpActu=A.StrucMdpActu[:B-2]+':9'+_C+A.StrucMdpActu[B+1:]
					elif B==1:A.StrucMdpActu=_D;return _A
					elif B==0:A.StrucMdpActu=_D;return _A
					else:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'09'+_C+A.StrucMdpActu[B+1:]
					return _A
	def place_pin_mdp(A):
		'Place un pin dans le mot de passe'
		for(B,C)in enumerate(A.StrucMdpActu):
			if C==_B:A.placedPinMdp=A.placedPinMdp[:B-1]+_B+A.placedPinMdp[B+1:];return _A
	def show_image_pin_placed(A):"Affiche l'image du mot de passe avec le pin placé";display.show(Image(A.placedPinMdp));sleep(3000)
def get_id():
	"\n    Protocole MicroID™️ permettant d'attribuer un ID (1 ou 2) à chaque micro:bit\n\n    La microbit commence par demander si elle peut être la m:b 1. Puis, elle écoute si elle reçoit une réponse.\n    Si elle reçoit la première le message d'une autre micro:bit, elle devient la m:b 2 et envoie une réponse autaurisant l'autre m:b à devenir la m:b 1.\n    ";C='IDc|1|2';B='IDa|1|1';display.show(Image('00000:00000:90909:00000:00000'));send_message(B)
	while _A:
		A=radio.receive()
		if A:
			if A==B:send_message(C);print('ID: 2');return 2
			if A==C:print('ID: 1');return 1
def check_connection():'\n    Vérifie si la connexion est toujours active\n\n    La m:b 1 commence par envoyer un message pour demander si la m:b 2 est toujours là.\n    La m:b 2 répond seulement si elle reçoit le message de la m:b 1.\n    '
def get_role():
	"\n    La m:b devient Parent si on appuie sur A ou Enfant si on appuie sur B, l'autre m:b s'addapte.\n    ";C='ROLEc|1|P';B='ROLEc|1|E';display.show('?')
	while _A:
		A=radio.receive()
		if button_a.is_pressed()or A==B:send_message(C);display.show('P');sleep(1000);display.clear();print('Parent');return'P'
		elif button_b.is_pressed()or A==C:send_message(B);display.show('E');sleep(1000);display.clear();print('Child');return'E'
def wait_for_button_up_not_cenceled(button):
	'\n    prend en paramètre le bouton à attendre (a, b ou ab)\n    Attend que le bouton soit relaché\n    ';A=button
	if A.lower()=='a':
		while button_a.is_pressed()and not button_b.is_pressed():0
		if button_b.is_pressed():return _F
		else:return _A
	elif A.lower()=='b':
		while button_b.is_pressed()and not button_a.is_pressed():0
		if button_a.is_pressed():return _F
		else:return _A
	elif A.lower()=='ab':
		while button_a.is_pressed()or button_b.is_pressed():0
def check_mdp():
	'Vérifie si le mot de passe entré est correct';B=0;A=ImageMdp()
	while _A:
		display.show(Image(A.StrucMdpActu))
		if button_b.is_pressed():A.change_position(dir='r');wait_for_button_up_not_cenceled('b')
		if button_a.is_pressed():A.change_position(dir='l');wait_for_button_up_not_cenceled('a')
		if button_a.is_pressed()and button_b.is_pressed():B+=1;sleep(1000);A.place_pin_mdp()
		if B==4:
			C=A.check_entry()
			if C:A.show_image_pin_placed();return _A
			A.show_image_pin_placed();display.scroll('Mauvais Mot de Passe, recommencer');B=0
def send_message(message):"\n    Envoie un message à l'autre m:b \n    (le but va etre de transformer cette fonction pour qu'elle soit encryptée plus tard comme ça on ne doit pas repasser partout dans le code)\n    ";radio.send(message)
if not DEV_BYPASS_GET_ID:ID=get_id()
else:ID=1
if not DEV_BYPASS_GET_ID:display.show(str(ID));sleep(500);display.clear()
ROLE=get_role()
if ROLE=='E':
	class Enfant:
		'Classe contenant les methodes et attributs de la m:b Enfant'
		def __init__(A):A.eveil=0
	while _A:send_message(_G);sleep(1500)
elif ROLE=='P':
	IMAGE_SLEEP_SEQUENCE=[Image('00000:00000:99099:00000:09990'),Image('00000:99990:00900:09000:99990'),Image('09999:00090:00900:09999:00000')]
	class Parent:
		'Classe contenant les methodes et attributs de la m:b Parent'
		def __init__(A):A.quantite_de_lait=0;A.image_lait=_E;A.index_menu=0;A.menu_items=[('L',A.mode_compteur),('S',A.mode_status),('T',A.mode_temperature),('F',A.mode_find)]
		def menu(A):
			'permet de choisir le mode';display.clear();sleep(100)
			while _A:
				display.show(A.menu_items[A.index_menu][0])
				if button_a.is_pressed()and button_b.is_pressed():display.clear();display.clear();sleep(100);A.menu_items[A.index_menu][1]()
				elif button_a.is_pressed():
					if wait_for_button_up_not_cenceled('a'):
						A.index_menu-=1
						if A.index_menu<0:A.index_menu=3
				elif button_b.is_pressed():
					if wait_for_button_up_not_cenceled('b'):
						A.index_menu+=1
						if A.index_menu>3:A.index_menu=0
		def add_lait(A):
			'Ajoute 1 unité de lait';A.image_lait=A.image_lait.replace(_B,_C,1);display.show(Image(A.image_lait))
			if A.quantite_de_lait>0:A.quantite_de_lait-=1
			print(A.image_lait);print(A.quantite_de_lait)
		def remove_lait(A):
			'Retire 1 unité de lait';B=A.image_lait.rfind(_C)
			if B!=-1:A.image_lait=A.image_lait[:B]+_B+A.image_lait[B+1:]
			display.show(Image(A.image_lait))
			if A.quantite_de_lait<25:A.quantite_de_lait+=1
			print(A.quantite_de_lait);print(A.image_lait);print(A.quantite_de_lait)
		def mode_compteur(A):
			'permet de compter la quantité de lait';display.show(Image(A.image_lait));wait_for_button_up_not_cenceled('ab')
			while _A:
				if pin_logo.is_touched():A.menu()
				if button_a.is_pressed()and button_b.is_pressed():
					display.scroll(str(A.quantite_de_lait));display.show(Image(A.image_lait));sleep(1000)
					if button_a.is_pressed()and button_b.is_pressed():A.image_lait=_E;A.quantite_de_lait=0;display.show(Image(A.image_lait))
				elif button_a.is_pressed():
					if wait_for_button_up_not_cenceled('a'):A.add_lait();wait_for_button_up_not_cenceled('a')
				elif button_b.is_pressed():
					if wait_for_button_up_not_cenceled('b'):A.remove_lait();wait_for_button_up_not_cenceled('b')
		def mode_status(B):
			"permet de voir l'état de l'Enfant";A=0;display.show(IMAGE_SLEEP_SEQUENCE[1])
			while _A:
				if pin_logo.is_touched():B.menu()
				C=radio.receive()
				if C==_G:
					A+=1
					if A%5==0:display.show(IMAGE_SLEEP_SEQUENCE[0])
					elif A%2==0:display.show(IMAGE_SLEEP_SEQUENCE[2])
					else:display.show(IMAGE_SLEEP_SEQUENCE[1])
		def mode_temperature(A):
			while not pin_logo.is_touched():display.show('x')
			A.menu()
		def mode_find(B):
			'permet de trouver la m:b Enfant'
			while not pin_logo.is_touched():
				A=radio.receive_full()
				if A:
					A=A[1];print(A)
					if A<-120:display.show(_B)
					elif A>-40:display.show(_C)
					else:display.show(abs(A)//10-2)
			B.menu()
	Parent().menu()
else:display.show(Image.SAD);sleep(1000);display.scroll('ROLE ERROR')