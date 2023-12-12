# le code original se trouve dans src/source.py
q='TEMP'
p='GETTEMP'
o='CMD'
n='STATUT'
m='00ml'
l='00000:00000:00000:00000:00000'
k=reversed
f='SETQLAIT'
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
O=ord
L=False
F=True
E=print
C=str
from microbit import button_a as I,button_b as J,pin_logo as W,sleep as K,display as A,Image as D,accelerometer as c,microphone as r
import music as d,sys,radio as G,random as s
from microbit import temperature as g
t=L
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
G.on()
G.config(channel=69,group=42)
def u():
	K='CONF';J='ASK';I='ID';A.show(D(e));H(B,I,J)
	while F:
		C=N(G.receive(),B)
		if C:
			if C[0]==I and C[2]==J:H(B,I,K);E('ID: 2');return 2
			if C[0]==I and C[2]==K:E('ID: 1');return 1
def v():
	D='ROLE';A.show('?')
	while F:
		C=N(G.receive(),B)
		if I.is_pressed()or C and C[0]==D and C[2]==S:H(B,D,T);A.show(S);K(1000);A.clear();E('Parent');return S
		if J.is_pressed()or C and C[0]==D and C[2]==T:H(B,D,S);A.show(T);K(1000);A.clear();E('Child');return T
def P(string):
	B=string
	def D(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=R(A);return A
	if B:
		A=O(B[0])<<7;E=1000003
		for F in B:A=D(A*E^O(F))
		A^=X(B)
		if A==-1:A=-2
		return C(A)
	return''
def w():
	T='CHECK';S='superhash_of_a: {}';O='a: {}';L='SCE';global B
	if Q==1:
		J=s.randint(0,999999999);E(O.format(J));H(B,L,J);M=P(P(C(J)));E(S.format(M));A.show(D(e))
		while F:
			I=N(G.receive(),B)
			if I:
				if I[0]==L:
					if I[2]==M:B=B+P(C(J));K(500);H(B,L,T);A.show(D.YES);K(500);return
					A.show(D.NO);sys.exit()
	if Q==2:
		A.show(D(e))
		while F:
			I=N(G.receive(),B)
			if I:
				if I[0]==L:break
		J=R(I[2]);E(O.format(J));M=P(P(C(J)));E(S.format(M));H(B,L,M);B=B+P(C(J))
		while F:
			I=N(G.receive(),B)
			if I:
				if I[0]==L:
					if I[2]==T:A.show(D.YES);K(500);return
					A.show(D.NO);sys.exit()
def M(button):
	A=button
	if A.lower()==Z:
		while I.is_pressed()and not J.is_pressed():0
		if J.is_pressed():return L
		return F
	if A.lower()==U:
		while J.is_pressed()and not I.is_pressed():0
		if I.is_pressed():return L
		return F
	if A.lower()=='ab':
		while I.is_pressed()or J.is_pressed():0
def h(message,key,decryption=L):
	G=decryption;E='';H=X(key);F=[O(A)for A in key]
	for(I,A)in enumerate(C(message)):
		if A.isalpha():
			D=I%H
			if G:B=chr((O(A.upper())-F[D]+26)%26+O('A'))
			else:B=chr((O(A.upper())+F[D]-26)%26+O('A'))
			if A.islower():B=B.lower()
			E+=B
		elif A.isdigit():
			D=I%H
			if G:B=C((R(A)-F[D])%10)
			else:B=C((R(A)+F[D])%10)
			E+=B
		else:E+=A
	return E
def N(encrypted_packet,key):
	C=encrypted_packet;B=None
	if not C:return
	A=h(C,key,F).split('|')
	try:
		G=A[0]
		try:D=R(A[1])
		except ValueError:D=B
		H=A[2];return G,D,H
	except IndexError:E('Mauvais packet reçu : {}'.format(A));return B,B,B
def H(key,t,content):B=content;A='{}|{}|{}'.format(t,C(X(C(B))),C(B));A=h(A,key);G.send(A)
class i:
	def __init__(A,id):A.id=id
class x(i):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=l;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[D('00000:00000:99099:00000:09990'),D('00000:99990:00900:09000:99990'),D('09999:00090:00900:09999:00000')];A.menu()
	def menu(B):
		A.clear();K(100)
		while F:
			A.show(B.menu_items[B.index_menu][0])
			if I.is_pressed()and J.is_pressed():A.clear();K(100);B.menu_items[B.index_menu][1]()
			elif I.is_pressed():
				if M(Z):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif J.is_pressed():
				if M(U):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		J=B.image_lait.split(a);G=[];H=L
		for C in Y(J):
			if b in C and not H:
				I=C.rfind(b);G.append(C[:I]+V+C[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				H=F
			else:G.append(C)
		B.image_lait=a.join(Y(G));E(B.image_lait);E(B.quantite_de_lait);A.show(D(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(a);C=[];H=L
		for G in Y(k(I)):
			if V in G and not H:
				C.append(G.replace(V,b,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				H=F
			else:C.append(G)
		B.image_lait=a.join(Y(k(C)));E(B.image_lait);E(B.quantite_de_lait);A.show(D(B.image_lait))
	def mode_compteur(E):
		A.show(D(E.image_lait));M('ab')
		while not W.is_touched():
			if I.is_pressed()and J.is_pressed():
				if E.quantite_de_lait==0:A.scroll('0ml')
				else:A.scroll(C(E.quantite_de_lait)+m)
				A.show(D(E.image_lait));K(1000)
				if I.is_pressed()and J.is_pressed():E.image_lait=l;E.quantite_de_lait=0;A.show(D(E.image_lait))
			elif I.is_pressed():
				if M(Z):E.add_lait();H(B,f,C(E.quantite_de_lait));M(Z)
			elif J.is_pressed():
				if M(U):E.remove_lait();H(B,f,C(E.quantite_de_lait));M(U)
		E.menu()
	def mode_statut(E):
		while not W.is_touched():
			D=N(G.receive(),B)
			if D and D[0]==n:A.show(C(D[2]))
		E.menu()
	def mode_temperature(E):
		H(B,o,p)
		while not W.is_touched():
			D=N(G.receive(),B)
			if D:
				if D[0]==q:A.scroll(C(D[2]));break
		E.menu()
	def mode_find(C):
		while not W.is_touched():
			B=G.receive_full()
			if B:
				B=B[1];E(B)
				if B<-120:A.show(b)
				elif B>-40:A.show(V)
				else:A.show(abs(B)//10-2)
		C.menu()
class y(i):
	def __init__(A,id):super().__init__(id);A.statut=0;A.old_statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.playing_music=L;A.quantite_de_lait=0;A.main()
	def main(D):
		Q=0
		while F:
			for T in range(10000):
				O=N(G.receive(),B)
				if T%500==0:
					S=(c.get_x()+c.get_y()+c.get_z()+r.sound_level()*100)/4;W=abs((S-Q)/100);D.history.append(W);D.history.pop(0);P=sum(D.history)/X(D.history)
					if P<.8:D.statut=0;A.show(V)
					elif P<3.:D.statut=1;A.show('1')
					elif P<4.:D.statut=2;A.show('2')
					Q=S
				if D.statut!=D.old_statut:H(B,n,C(D.statut));D.old_statut=D.statut
				if J.is_pressed()and D.statut>0:
					if not D.playing_music:d.play(d.PYTHON,wait=L);D.playing_music=F
					else:d.stop();D.playing_music=L
					M(U)
				if I.is_pressed()and D.statut>0:A.scroll(C(D.quantite_de_lait)+m)
				if O:
					if O[0]==o and O[2]==p:K(100);H(B,q,C(g()));E('TEMP: {}'.format(g()))
					if O[0]==f:D.quantite_de_lait=R(O[2]);E('SETQLAIT: {}'.format(D.quantite_de_lait))
if not t:Q=u();A.show(C(Q));K(500);A.clear();w()
else:Q=0
j=v()
if j==S:z=x(Q)
elif j==T:z=y(Q)
else:A.scroll('ROLE ERROR')