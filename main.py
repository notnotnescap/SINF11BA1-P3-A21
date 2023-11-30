# le code entier se trouve dans build/raw.py
Z='00000:00000:00000:00000:00000'
Y='test'
U='0'
T='9'
S=False
Q='b'
P='a'
M='P'
L=ord
J=str
F=True
D=print
from microbit import button_a as B,button_b as C,pin_logo as N,sleep as G,display as A,Image as E
import radio as H
V=F
W=Y
def a():
	G='CONF';C='ASK';A.show(E('00000:00000:90909:00000:00000'));K(W,'ID',C)
	while F:
		B=H.receive()
		if B:
			if B==C:K(W,'ID',G);D('ID: 2');return 2
			if B==G:D('ID: 1');return 1
def b(d):
	J='ROLE';E='E';A.show('?')
	while F:
		I=H.receive()
		if B.is_pressed()or I==E:K(d.key,J,E);A.show(M);G(1000);A.clear();D('Parent');return M
		if C.is_pressed()or I==M:K(d.key,J,M);A.show(E);G(1000);A.clear();D('Child');return E
def I(button):
	A=button
	if A.lower()==P:
		while B.is_pressed()and not C.is_pressed():0
		if C.is_pressed():return S
		return F
	if A.lower()==Q:
		while C.is_pressed()and not B.is_pressed():0
		if B.is_pressed():return S
		return F
	if A.lower()=='ab':
		while B.is_pressed()or C.is_pressed():0
def c(message,key,decryption=S):
	F=decryption;D='';G=len(key);E=[L(A)for A in key]
	for(H,A)in enumerate(J(message)):
		if A.isalpha():
			C=H%G
			if F:B=chr((L(A.upper())-E[C]+26)%26+L('A'))
			else:B=chr((L(A.upper())+E[C]-26)%26+L('A'))
			if A.islower():B=B.lower()
			D+=B
		elif A.isdigit():
			C=H%G
			if F:B=J((int(A)-E[C])%10)
			else:B=J((int(A)+E[C])%10)
			D+=B
		else:D+=A
	return D
def K(key,t,content):B=content;A='{}|{}|{}'.format(t,J(len(B)),B);A=c(A,key);H.send(A)
class R:
	def __init__(B):
		B.channel=69;B.group=42;B.key=Y;B.id=0
		if not V:A.show(J(B.id));G(500);A.clear()
		H.on();H.config(channel=B.channel,group=B.group)
class d(R):
	def __init__(B):A.show('i');super().__init__();B.quantite_de_lait=0;B.image_lait=Z;B.index_menu=0;B.menu_items=[('L',B.mode_compteur),('S',B.mode_status),('T',B.mode_temperature),('F',B.mode_find)];B.IMAGE_SLEEP_SEQUENCE=[E('00000:00000:99099:00000:09990'),E('00000:99990:00900:09000:99990'),E('09999:00090:00900:09999:00000')];B.menu()
	def menu(D):
		A.clear();G(100)
		while F:
			A.show(D.menu_items[D.index_menu][0])
			if B.is_pressed()and C.is_pressed():A.clear();G(100);D.menu_items[D.index_menu][1]()
			elif B.is_pressed():
				if I(P):
					D.index_menu-=1
					if D.index_menu<0:D.index_menu=3
			elif C.is_pressed():
				if I(Q):
					D.index_menu+=1
					if D.index_menu>3:D.index_menu=0
	def add_lait(B):
		B.image_lait=B.image_lait.replace(T,U,1);A.show(E(B.image_lait))
		if B.quantite_de_lait>0:B.quantite_de_lait-=1
		D(B.image_lait);D(B.quantite_de_lait)
	def remove_lait(B):
		C=B.image_lait.rfind(U)
		if C!=-1:B.image_lait=B.image_lait[:C]+T+B.image_lait[C+1:]
		A.show(E(B.image_lait))
		if B.quantite_de_lait<25:B.quantite_de_lait+=1
		D(B.quantite_de_lait);D(B.image_lait);D(B.quantite_de_lait)
	def mode_compteur(D):
		A.show(E(D.image_lait));I('ab')
		while F:
			if N.is_touched():D.menu()
			if B.is_pressed()and C.is_pressed():
				A.scroll(J(D.quantite_de_lait));A.show(E(D.image_lait));G(1000)
				if B.is_pressed()and C.is_pressed():D.image_lait=Z;D.quantite_de_lait=0;A.show(E(D.image_lait))
			elif B.is_pressed():
				if I(P):D.add_lait();I(P)
			elif C.is_pressed():
				if I(Q):D.remove_lait();I(Q)
	def mode_status(B):
		C=0;A.show(B.IMAGE_SLEEP_SEQUENCE[1])
		while F:
			if N.is_touched():B.menu()
			D=H.receive()
			if D=='STATUSr|6|ASLEEP':
				C+=1
				if C%5==0:A.show(B.IMAGE_SLEEP_SEQUENCE[0])
				elif C%2==0:A.show(B.IMAGE_SLEEP_SEQUENCE[2])
				else:A.show(B.IMAGE_SLEEP_SEQUENCE[1])
	def mode_temperature(B):
		while not N.is_touched():A.show('x')
		B.menu()
	def mode_find(C):
		while not N.is_touched():
			B=H.receive_full()
			if B:
				B=B[1];D(B)
				if B<-120:A.show(T)
				elif B>-40:A.show(U)
				else:A.show(abs(B)//10-2)
		C.menu()
class e(R):
	def __init__(A):super().__init__();A.statut=0;A.main()
	def main(A):
		while F:K(A.key,'STATUT',A.statut);G(1000)
O=R()
if not V:X=a()
else:X=0
O.id=X
if b(O)==M:O=d()
else:O=e()