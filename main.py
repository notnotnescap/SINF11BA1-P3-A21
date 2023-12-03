j='STATUT'
i='00000:00000:00000:00000:00000'
h=reversed
d='00000:00000:90909:00000:00000'
b='9'
a=':'
Z='b'
Y='a'
X=list
W=len
U='0'
T=False
S='P'
R='E'
Q=int
M=ord
F=True
D=str
C=print
from microbit import button_a as G,button_b as H,pin_logo as V,sleep as J,display as A,Image as E,accelerometer as c
import music,sys,radio as I,random as k
l=F
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
I.on()
I.config(channel=69,group=42)
def m():
	J='CONF';H='ASK';G='ID';A.show(E(d));L(B,G,H)
	while F:
		D=P(I.receive(),B)
		if D:
			if D[0]==G and D[2]==H:L(B,G,J);C('ID: 2');return 2
			if D[0]==G and D[2]==J:C('ID: 1');return 1
def n():
	E='ROLE';A.show('?')
	while F:
		D=I.receive()
		if G.is_pressed()or D==R:L(B,E,R);A.show(S);J(1000);A.clear();C('Parent');return S
		if H.is_pressed()or D==S:L(B,E,S);A.show(R);J(1000);A.clear();C('Child');return R
def N(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=Q(A);return A
	if B:
		A=M(B[0])<<7;E=1000003
		for F in B:A=C(A*E^M(F))
		A^=W(B)
		if A==-1:A=-2
		return D(A)
	return''
def o():
	S='superhash_of_a: {}';R='a: {}';M='SCE';global B
	if O==1:
		G=k.randint(0,999999999);C(R.format(G));L(B,M,G);K=N(N(D(G)));C(S.format(K));A.show(E(d))
		while F:
			H=P(I.receive(),B)
			if H:
				if H[0]==M:
					if H[2]==K:B=B+N(D(G));A.show(E.YES);J(500);return
					A.show(E.NO);sys.exit()
	if O==2:
		A.show(E(d))
		while F:
			H=P(I.receive(),B)
			if H:
				if H[0]==M:break
		G=Q(H[2]);C(R.format(G));K=N(N(D(G)));C(S.format(K));L(B,M,K);B=B+N(D(G));A.show(E.YES);J(500)
def K(button):
	A=button
	if A.lower()==Y:
		while G.is_pressed()and not H.is_pressed():0
		if H.is_pressed():return T
		return F
	if A.lower()==Z:
		while H.is_pressed()and not G.is_pressed():0
		if G.is_pressed():return T
		return F
	if A.lower()=='ab':
		while G.is_pressed()or H.is_pressed():0
def e(message,key,decryption=T):
	G=decryption;E='';H=W(key);F=[M(A)for A in key]
	for(I,A)in enumerate(D(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((M(A.upper())-F[C]+26)%26+M('A'))
			else:B=chr((M(A.upper())+F[C]-26)%26+M('A'))
			if A.islower():B=B.lower()
			E+=B
		elif A.isdigit():
			C=I%H
			if G:B=D((Q(A)-F[C])%10)
			else:B=D((Q(A)+F[C])%10)
			E+=B
		else:E+=A
	return E
def P(encrypted_packet,key):
	D=encrypted_packet;B=None
	if not D:return
	A=e(D,key,F).split('|')
	try:
		G=A[0]
		try:E=Q(A[1])
		except ValueError:E=B
		H=A[2];return G,E,H
	except IndexError:C('Mauvais packet reçu : {}'.format(A));return B,B,B
def L(key,t,content):B=content;A='{}|{}|{}'.format(t,D(W(D(B))),D(B));A=e(A,key);I.send(A)
class f:
	def __init__(A,id):A.id=id
class p(f):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=i;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[E('00000:00000:99099:00000:09990'),E('00000:99990:00900:09000:99990'),E('09999:00090:00900:09999:00000')];A.menu()
	def menu(B):
		A.clear();J(100)
		while F:
			A.show(B.menu_items[B.index_menu][0])
			if G.is_pressed()and H.is_pressed():A.clear();J(100);B.menu_items[B.index_menu][1]()
			elif G.is_pressed():
				if K(Y):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif H.is_pressed():
				if K(Z):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		J=B.image_lait.split(a);G=[];H=T
		for D in X(J):
			if b in D and not H:
				I=D.rfind(b);G.append(D[:I]+U+D[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				H=F
			else:G.append(D)
		B.image_lait=a.join(X(G));C(B.image_lait);C(B.quantite_de_lait);A.show(E(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(a);D=[];H=T
		for G in X(h(I)):
			if U in G and not H:
				D.append(G.replace(U,b,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				H=F
			else:D.append(G)
		B.image_lait=a.join(X(h(D)));C(B.image_lait);C(B.quantite_de_lait);A.show(E(B.image_lait))
	def mode_compteur(B):
		A.show(E(B.image_lait));K('ab')
		while not V.is_touched():
			if G.is_pressed()and H.is_pressed():
				if B.quantite_de_lait==0:A.scroll('0ml')
				else:A.scroll(D(B.quantite_de_lait)+'00ml')
				A.show(E(B.image_lait));J(1000)
				if G.is_pressed()and H.is_pressed():B.image_lait=i;B.quantite_de_lait=0;A.show(E(B.image_lait))
			elif G.is_pressed():
				if K(Y):B.add_lait();K(Y)
			elif H.is_pressed():
				if K(Z):B.remove_lait();K(Z)
		B.menu()
	def mode_statut(E):
		while not V.is_touched():
			C=P(I.receive(),B)
			if C and C[0]==j:A.show(D(C[2]))
		E.menu()
	def mode_temperature(B):
		while not V.is_touched():A.show('x')
		B.menu()
	def mode_find(D):
		while not V.is_touched():
			B=I.receive_full()
			if B:
				B=B[1];C(B)
				if B<-120:A.show(b)
				elif B>-40:A.show(U)
				else:A.show(abs(B)//10-2)
		D.menu()
class q(f):
	def __init__(A,id):super().__init__(id);A.statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.main()
	def main(E):
		H=0
		while F:
			for K in range(10000):
				N=P(I.receive(),B)
				if K%500==0:
					J=(c.get_x()+c.get_y()+c.get_z())/3;M=abs((J-H)/100);E.history.append(M);E.history.pop(0);C('\x1bc');G=sum(E.history)/W(E.history);C(G)
					if G<.8:E.statut=0;A.show(U)
					elif G<3.:E.statut=1;A.show('1')
					elif G<4.:E.statut=2;A.show('2')
					H=J
			L(B,j,D(E.statut))
if not l:O=m();A.show(D(O));J(500);A.clear();o()
else:O=0
g=n()
if g==S:r=p(O)
elif g==R:r=q(O)
else:A.scroll('ROLE ERROR')