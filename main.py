k='STATUT'
j='00000:00000:00000:00000:00000'
i=reversed
e='00000:00000:90909:00000:00000'
b='9'
a=':'
Z='a'
Y=list
X=len
V='0'
U='b'
T='P'
S='E'
R=int
P=False
M=ord
F=True
D=str
C=print
from microbit import button_a as G,button_b as H,pin_logo as W,sleep as J,display as A,Image as E,accelerometer as c,microphone as l
import music as d,sys,radio as I,random as m
n=F
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
I.on()
I.config(channel=69,group=42)
def o():
	J='CONF';H='ASK';G='ID';A.show(E(e));L(B,G,H)
	while F:
		D=Q(I.receive(),B)
		if D:
			if D[0]==G and D[2]==H:L(B,G,J);C('ID: 2');return 2
			if D[0]==G and D[2]==J:C('ID: 1');return 1
def p():
	E='ROLE';A.show('?')
	while F:
		D=I.receive()
		if G.is_pressed()or D==S:L(B,E,S);A.show(T);J(1000);A.clear();C('Parent');return T
		if H.is_pressed()or D==T:L(B,E,T);A.show(S);J(1000);A.clear();C('Child');return S
def N(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=R(A);return A
	if B:
		A=M(B[0])<<7;E=1000003
		for F in B:A=C(A*E^M(F))
		A^=X(B)
		if A==-1:A=-2
		return D(A)
	return''
def q():
	S='superhash_of_a: {}';P='a: {}';M='SCE';global B
	if O==1:
		H=m.randint(0,999999999);C(P.format(H));L(B,M,H);K=N(N(D(H)));C(S.format(K));A.show(E(e))
		while F:
			G=Q(I.receive(),B)
			if G:
				if G[0]==M:
					if G[2]==K:B=B+N(D(H));A.show(E.YES);J(500);A.scroll(G,delay=80);return
					A.show(E.NO);sys.exit()
	if O==2:
		A.show(E(e))
		while F:
			G=Q(I.receive(),B)
			if G:
				if G[0]==M:break
		H=R(G[2]);C(P.format(H));K=N(N(D(H)));C(S.format(K));L(B,M,K);B=B+N(D(H));A.show(E.YES);J(500);A.scroll(G,delay=80)
def K(button):
	A=button
	if A.lower()==Z:
		while G.is_pressed()and not H.is_pressed():0
		if H.is_pressed():return P
		return F
	if A.lower()==U:
		while H.is_pressed()and not G.is_pressed():0
		if G.is_pressed():return P
		return F
	if A.lower()=='ab':
		while G.is_pressed()or H.is_pressed():0
def f(message,key,decryption=P):
	G=decryption;E='';H=X(key);F=[M(A)for A in key]
	for(I,A)in enumerate(D(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((M(A.upper())-F[C]+26)%26+M('A'))
			else:B=chr((M(A.upper())+F[C]-26)%26+M('A'))
			if A.islower():B=B.lower()
			E+=B
		elif A.isdigit():
			C=I%H
			if G:B=D((R(A)-F[C])%10)
			else:B=D((R(A)+F[C])%10)
			E+=B
		else:E+=A
	return E
def Q(encrypted_packet,key):
	D=encrypted_packet;B=None
	if not D:return
	A=f(D,key,F).split('|')
	try:
		G=A[0]
		try:E=R(A[1])
		except ValueError:E=B
		H=A[2];return G,E,H
	except IndexError:C('Mauvais packet reçu : {}'.format(A));return B,B,B
def L(key,t,content):B=content;A='{}|{}|{}'.format(t,D(X(D(B))),D(B));A=f(A,key);I.send(A)
class g:
	def __init__(A,id):A.id=id
class r(g):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=j;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[E('00000:00000:99099:00000:09990'),E('00000:99990:00900:09000:99990'),E('09999:00090:00900:09999:00000')];A.menu()
	def menu(B):
		A.clear();J(100)
		while F:
			A.show(B.menu_items[B.index_menu][0])
			if G.is_pressed()and H.is_pressed():A.clear();J(100);B.menu_items[B.index_menu][1]()
			elif G.is_pressed():
				if K(Z):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif H.is_pressed():
				if K(U):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		J=B.image_lait.split(a);G=[];H=P
		for D in Y(J):
			if b in D and not H:
				I=D.rfind(b);G.append(D[:I]+V+D[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				H=F
			else:G.append(D)
		B.image_lait=a.join(Y(G));C(B.image_lait);C(B.quantite_de_lait);A.show(E(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(a);D=[];H=P
		for G in Y(i(I)):
			if V in G and not H:
				D.append(G.replace(V,b,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				H=F
			else:D.append(G)
		B.image_lait=a.join(Y(i(D)));C(B.image_lait);C(B.quantite_de_lait);A.show(E(B.image_lait))
	def mode_compteur(B):
		A.show(E(B.image_lait));K('ab')
		while not W.is_touched():
			if G.is_pressed()and H.is_pressed():
				if B.quantite_de_lait==0:A.scroll('0ml')
				else:A.scroll(D(B.quantite_de_lait)+'00ml')
				A.show(E(B.image_lait));J(1000)
				if G.is_pressed()and H.is_pressed():B.image_lait=j;B.quantite_de_lait=0;A.show(E(B.image_lait))
			elif G.is_pressed():
				if K(Z):B.add_lait();K(Z)
			elif H.is_pressed():
				if K(U):B.remove_lait();K(U)
		B.menu()
	def mode_statut(E):
		while not W.is_touched():
			C=Q(I.receive(),B)
			if C and C[0]==k:A.show(D(C[2]))
		E.menu()
	def mode_temperature(B):
		while not W.is_touched():A.show('x')
		B.menu()
	def mode_find(D):
		while not W.is_touched():
			B=I.receive_full()
			if B:
				B=B[1];C(B)
				if B<-120:A.show(b)
				elif B>-40:A.show(V)
				else:A.show(abs(B)//10-2)
		D.menu()
class s(g):
	def __init__(A,id):super().__init__(id);A.statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.main()
	def main(E):
		M=0
		while F:
			for O in range(10000):
				S=Q(I.receive(),B)
				if O%500==0:
					N=(c.get_x()+c.get_y()+c.get_z()+l.sound_level()*100)/4;R=abs((N-M)/100);E.history.append(R);E.history.pop(0);C('\x1bc');J=sum(E.history)/X(E.history);C(J)
					if J<.8:E.statut=0;A.show(V)
					elif J<3.:E.statut=1;A.show('1')
					elif J<4.:E.statut=2;A.show('2')
					M=N
				if H.is_pressed()and E.statut>0:d.play(d.PYTHON,wait=P);K(U)
				if G.is_pressed()and E.statut>0:d.stop()
			L(B,k,D(E.statut))
if not n:O=o();A.show(D(O));J(500);A.clear();q()
else:O=0
h=p()
if h==T:t=r(O)
elif h==S:t=s(O)
else:A.scroll('ROLE ERROR')