# le code original se trouve dans src/source.py
o='TEMP'
n='GETTEMP'
m='CMD'
l='STATUT'
k='00000:00000:00000:00000:00000'
j=reversed
e='00000:00000:90909:00000:00000'
b='9'
a=':'
Z='a'
Y=list
X=len
V='0'
U='b'
T='E'
S='P'
R=int
O=False
N=ord
G=True
E=print
C=str
from microbit import button_a as H,button_b as I,pin_logo as W,sleep as J,display as A,Image as D,accelerometer as c,microphone as p
import music as d,sys,radio as F,random as q
from microbit import temperature as f
r=O
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
F.on()
F.config(channel=69,group=42)
def s():
	J='CONF';I='ASK';H='ID';A.show(D(e));K(B,H,I)
	while G:
		C=M(F.receive(),B)
		if C:
			if C[0]==H and C[2]==I:K(B,H,J);E('ID: 2');return 2
			if C[0]==H and C[2]==J:E('ID: 1');return 1
def t():
	D='ROLE';A.show('?')
	while G:
		C=M(F.receive(),B)
		if H.is_pressed()or C and C[0]==D and C[2]==S:K(B,D,T);A.show(S);J(1000);A.clear();E('Parent');return S
		if I.is_pressed()or C and C[0]==D and C[2]==T:K(B,D,S);A.show(T);J(1000);A.clear();E('Child');return T
def P(string):
	B=string
	def D(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=R(A);return A
	if B:
		A=N(B[0])<<7;E=1000003
		for F in B:A=D(A*E^N(F))
		A^=X(B)
		if A==-1:A=-2
		return C(A)
	return''
def u():
	T='CHECK';S='superhash_of_a: {}';O='a: {}';L='SCE';global B
	if Q==1:
		I=q.randint(0,999999999);E(O.format(I));K(B,L,I);N=P(P(C(I)));E(S.format(N));A.show(D(e))
		while G:
			H=M(F.receive(),B)
			if H:
				if H[0]==L:
					if H[2]==N:B=B+P(C(I));J(500);K(B,L,T);A.show(D.YES);J(500);return
					A.show(D.NO);sys.exit()
	if Q==2:
		A.show(D(e))
		while G:
			H=M(F.receive(),B)
			if H:
				if H[0]==L:break
		I=R(H[2]);E(O.format(I));N=P(P(C(I)));E(S.format(N));K(B,L,N);B=B+P(C(I))
		while G:
			H=M(F.receive(),B)
			if H:
				if H[0]==L:
					if H[2]==T:A.show(D.YES);J(500);return
					A.show(D.NO);sys.exit()
def L(button):
	A=button
	if A.lower()==Z:
		while H.is_pressed()and not I.is_pressed():0
		if I.is_pressed():return O
		return G
	if A.lower()==U:
		while I.is_pressed()and not H.is_pressed():0
		if H.is_pressed():return O
		return G
	if A.lower()=='ab':
		while H.is_pressed()or I.is_pressed():0
def g(message,key,decryption=O):
	G=decryption;E='';H=X(key);F=[N(A)for A in key]
	for(I,A)in enumerate(C(message)):
		if A.isalpha():
			D=I%H
			if G:B=chr((N(A.upper())-F[D]+26)%26+N('A'))
			else:B=chr((N(A.upper())+F[D]-26)%26+N('A'))
			if A.islower():B=B.lower()
			E+=B
		elif A.isdigit():
			D=I%H
			if G:B=C((R(A)-F[D])%10)
			else:B=C((R(A)+F[D])%10)
			E+=B
		else:E+=A
	return E
def M(encrypted_packet,key):
	C=encrypted_packet;B=None
	if not C:return
	A=g(C,key,G).split('|')
	try:
		F=A[0]
		try:D=R(A[1])
		except ValueError:D=B
		H=A[2];return F,D,H
	except IndexError:E('Mauvais packet reçu : {}'.format(A));return B,B,B
def K(key,t,content):B=content;A='{}|{}|{}'.format(t,C(X(C(B))),C(B));A=g(A,key);F.send(A)
class h:
	def __init__(A,id):A.id=id
class v(h):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=k;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[D('00000:00000:99099:00000:09990'),D('00000:99990:00900:09000:99990'),D('09999:00090:00900:09999:00000')];A.menu()
	def menu(B):
		A.clear();J(100)
		while G:
			A.show(B.menu_items[B.index_menu][0])
			if H.is_pressed()and I.is_pressed():A.clear();J(100);B.menu_items[B.index_menu][1]()
			elif H.is_pressed():
				if L(Z):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif I.is_pressed():
				if L(U):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		J=B.image_lait.split(a);F=[];H=O
		for C in Y(J):
			if b in C and not H:
				I=C.rfind(b);F.append(C[:I]+V+C[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				H=G
			else:F.append(C)
		B.image_lait=a.join(Y(F));E(B.image_lait);E(B.quantite_de_lait);A.show(D(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(a);C=[];H=O
		for F in Y(j(I)):
			if V in F and not H:
				C.append(F.replace(V,b,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				H=G
			else:C.append(F)
		B.image_lait=a.join(Y(j(C)));E(B.image_lait);E(B.quantite_de_lait);A.show(D(B.image_lait))
	def mode_compteur(B):
		A.show(D(B.image_lait));L('ab')
		while not W.is_touched():
			if H.is_pressed()and I.is_pressed():
				if B.quantite_de_lait==0:A.scroll('0ml')
				else:A.scroll(C(B.quantite_de_lait)+'00ml')
				A.show(D(B.image_lait));J(1000)
				if H.is_pressed()and I.is_pressed():B.image_lait=k;B.quantite_de_lait=0;A.show(D(B.image_lait))
			elif H.is_pressed():
				if L(Z):B.add_lait();L(Z)
			elif I.is_pressed():
				if L(U):B.remove_lait();L(U)
		B.menu()
	def mode_statut(E):
		while not W.is_touched():
			D=M(F.receive(),B)
			if D and D[0]==l:A.show(C(D[2]))
		E.menu()
	def mode_temperature(E):
		K(B,m,n)
		while not W.is_touched():
			D=M(F.receive(),B)
			if D:
				if D[0]==o:A.scroll(C(D[2]));break
		E.menu()
	def mode_find(C):
		while not W.is_touched():
			B=F.receive_full()
			if B:
				B=B[1];E(B)
				if B<-120:A.show(b)
				elif B>-40:A.show(V)
				else:A.show(abs(B)//10-2)
		C.menu()
class w(h):
	def __init__(A,id):super().__init__(id);A.statut=0;A.old_statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.main()
	def main(D):
		Q=0
		while G:
			for S in range(10000):
				N=M(F.receive(),B)
				if S%500==0:
					R=(c.get_x()+c.get_y()+c.get_z()+p.sound_level()*100)/4;T=abs((R-Q)/100);D.history.append(T);D.history.pop(0);P=sum(D.history)/X(D.history)
					if P<.8:D.statut=0;A.show(V)
					elif P<3.:D.statut=1;A.show('1')
					elif P<4.:D.statut=2;A.show('2')
					Q=R
				if D.statut!=D.old_statut:K(B,l,C(D.statut));D.old_statut=D.statut
				if I.is_pressed()and D.statut>0:d.play(d.PYTHON,wait=O);L(U)
				if H.is_pressed()and D.statut>0:d.stop()
				if N:
					if N[0]==m and N[2]==n:J(100);K(B,o,C(f()));E('TEMP: {}'.format(f()))
if not r:Q=s();A.show(C(Q));J(500);A.clear();u()
else:Q=0
i=t()
if i==S:x=v(Q)
elif i==T:x=w(Q)
else:A.scroll('ROLE ERROR')