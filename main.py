b='00000:00000:00000:00000:00000'
a='test'
W='0'
V='9'
U=int
R='b'
Q='a'
P=False
M='P'
L=ord
J=str
F=True
B=print
from microbit import button_a as C,button_b as D,pin_logo as N,sleep as G,display as A,Image as E
import radio as H
X=P
S=a
H.on()
H.config(channel=69,group=42)
def c():
	I='CONF';G='ASK';D='ID';A.show(E('00000:00000:90909:00000:00000'));K(S,D,G)
	while F:
		C=e(H.receive(),S);B(C)
		if C:
			if C[0]==D and C[2]==G:K(S,D,I);B('ID: 2');return 2
			if C[0]==D and C[2]==I:B('ID: 1');return 1
def d(d):
	J='ROLE';E='E';A.show('?')
	while F:
		I=H.receive()
		if C.is_pressed()or I==E:K(d.key,J,E);A.show(M);G(1000);A.clear();B('Parent');return M
		if D.is_pressed()or I==M:K(d.key,J,M);A.show(E);G(1000);A.clear();B('Child');return E
def I(button):
	A=button
	if A.lower()==Q:
		while C.is_pressed()and not D.is_pressed():0
		if D.is_pressed():return P
		return F
	if A.lower()==R:
		while D.is_pressed()and not C.is_pressed():0
		if C.is_pressed():return P
		return F
	if A.lower()=='ab':
		while C.is_pressed()or D.is_pressed():0
def Y(message,key,decryption=P):
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
			if F:B=J((U(A)-E[C])%10)
			else:B=J((U(A)+E[C])%10)
			D+=B
		else:D+=A
	return D
def e(encrypted_packet,key):
	D=encrypted_packet;C=None
	if not D:return
	A=Y(D,key,F).split('|')
	try:
		G=A[0]
		try:E=U(A[1])
		except ValueError:E=C
		H=A[2];return G,E,H
	except IndexError:B('Mauvais packet reçu : {}'.format(A));return C,C,C
def K(key,t,content):B=content;A='{}|{}|{}'.format(t,J(len(B)),B);A=Y(A,key);H.send(A)
class T:
	def __init__(B):
		B.key=a;B.id=0
		if not X:A.show(J(B.id));G(500);A.clear()
class f(T):
	def __init__(B):A.show('i');super().__init__();B.quantite_de_lait=0;B.image_lait=b;B.index_menu=0;B.menu_items=[('L',B.mode_compteur),('S',B.mode_status),('T',B.mode_temperature),('F',B.mode_find)];B.IMAGE_SLEEP_SEQUENCE=[E('00000:00000:99099:00000:09990'),E('00000:99990:00900:09000:99990'),E('09999:00090:00900:09999:00000')];B.menu()
	def menu(B):
		A.clear();G(100)
		while F:
			A.show(B.menu_items[B.index_menu][0])
			if C.is_pressed()and D.is_pressed():A.clear();G(100);B.menu_items[B.index_menu][1]()
			elif C.is_pressed():
				if I(Q):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif D.is_pressed():
				if I(R):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(C):
		C.image_lait=C.image_lait.replace(V,W,1);A.show(E(C.image_lait))
		if C.quantite_de_lait>0:C.quantite_de_lait-=1
		B(C.image_lait);B(C.quantite_de_lait)
	def remove_lait(C):
		D=C.image_lait.rfind(W)
		if D!=-1:C.image_lait=C.image_lait[:D]+V+C.image_lait[D+1:]
		A.show(E(C.image_lait))
		if C.quantite_de_lait<25:C.quantite_de_lait+=1
		B(C.quantite_de_lait);B(C.image_lait);B(C.quantite_de_lait)
	def mode_compteur(B):
		A.show(E(B.image_lait));I('ab')
		while F:
			if N.is_touched():B.menu()
			if C.is_pressed()and D.is_pressed():
				A.scroll(J(B.quantite_de_lait));A.show(E(B.image_lait));G(1000)
				if C.is_pressed()and D.is_pressed():B.image_lait=b;B.quantite_de_lait=0;A.show(E(B.image_lait))
			elif C.is_pressed():
				if I(Q):B.add_lait();I(Q)
			elif D.is_pressed():
				if I(R):B.remove_lait();I(R)
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
	def mode_find(D):
		while not N.is_touched():
			C=H.receive_full()
			if C:
				C=C[1];B(C)
				if C<-120:A.show(V)
				elif C>-40:A.show(W)
				else:A.show(abs(C)//10-2)
		D.menu()
class g(T):
	def __init__(A):super().__init__();A.statut=0;A.main()
	def main(A):
		while F:K(A.key,'STATUT',A.statut);G(1000)
O=T()
if not X:Z=c()
else:Z=0
O.id=Z
if d(O)==M:O=f()
else:O=g()