h='00000:00000:00000:00000:00000'
g=reversed
c='00000:00000:90909:00000:00000'
b=len
Z='0'
Y='9'
X=':'
W='b'
V='a'
U=list
S=False
R='P'
Q='E'
P=int
M=ord
F=str
E=True
D=print
from microbit import button_a as G,button_b as H,pin_logo as T,sleep as I,display as A,Image as C
import sys,radio as J,random as i
j=E
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
J.on()
J.config(channel=69,group=42)
def k():
	I='CONF';H='ASK';G='ID';A.show(C(c));L(B,G,H)
	while E:
		F=a(J.receive(),B)
		if F:
			if F[0]==G and F[2]==H:L(B,G,I);D('ID: 2');return 2
			if F[0]==G and F[2]==I:D('ID: 1');return 1
def l():
	F='ROLE';A.show('?')
	while E:
		C=J.receive()
		if G.is_pressed()or C==Q:L(B,F,Q);A.show(R);I(1000);A.clear();D('Parent');return R
		if H.is_pressed()or C==R:L(B,F,R);A.show(Q);I(1000);A.clear();D('Child');return Q
def N(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=P(A);return A
	if B:
		A=M(B[0])<<7;D=1000003
		for E in B:A=C(A*D^M(E))
		A^=b(B)
		if A==-1:A=-2
		return F(A)
	return''
def m():
	R='superhash_of_a: {}';Q='a: {}';M='SCE';global B
	if O==1:
		G=i.randint(0,999999999);D(Q.format(G));L(B,M,G);K=N(N(F(G)));D(R.format(K));A.show(C(c))
		while E:
			H=a(J.receive(),B)
			if H:
				if H[0]==M:
					if H[2]==K:B=B+N(F(G));A.show(C.YES);I(500);return
					A.show(C.NO);sys.exit()
	if O==2:
		A.show(C(c))
		while E:
			H=a(J.receive(),B)
			if H:
				if H[0]==M:break
		G=P(H[2]);D(Q.format(G));K=N(N(F(G)));D(R.format(K));L(B,M,K);B=B+N(F(G));A.show(C.YES);I(500)
def K(button):
	A=button
	if A.lower()==V:
		while G.is_pressed()and not H.is_pressed():0
		if H.is_pressed():return S
		return E
	if A.lower()==W:
		while H.is_pressed()and not G.is_pressed():0
		if G.is_pressed():return S
		return E
	if A.lower()=='ab':
		while G.is_pressed()or H.is_pressed():0
def d(message,key,decryption=S):
	G=decryption;D='';H=b(key);E=[M(A)for A in key]
	for(I,A)in enumerate(F(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((M(A.upper())-E[C]+26)%26+M('A'))
			else:B=chr((M(A.upper())+E[C]-26)%26+M('A'))
			if A.islower():B=B.lower()
			D+=B
		elif A.isdigit():
			C=I%H
			if G:B=F((P(A)-E[C])%10)
			else:B=F((P(A)+E[C])%10)
			D+=B
		else:D+=A
	return D
def a(encrypted_packet,key):
	C=encrypted_packet;B=None
	if not C:return
	A=d(C,key,E).split('|')
	try:
		G=A[0]
		try:F=P(A[1])
		except ValueError:F=B
		H=A[2];return G,F,H
	except IndexError:D('Mauvais packet reçu : {}'.format(A));return B,B,B
def L(key,t,content):B=content;A='{}|{}|{}'.format(t,F(b(F(B))),F(B));A=d(A,key);J.send(A)
class e:
	def __init__(A,id):A.id=id
class n(e):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=h;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_status),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[C('00000:00000:99099:00000:09990'),C('00000:99990:00900:09000:99990'),C('09999:00090:00900:09999:00000')];A.menu()
	def menu(B):
		A.clear();I(100)
		while E:
			A.show(B.menu_items[B.index_menu][0])
			if G.is_pressed()and H.is_pressed():A.clear();I(100);B.menu_items[B.index_menu][1]()
			elif G.is_pressed():
				if K(V):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif H.is_pressed():
				if K(W):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		J=B.image_lait.split(X);G=[];H=S
		for F in U(J):
			if Y in F and not H:
				I=F.rfind(Y);G.append(F[:I]+Z+F[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				H=E
			else:G.append(F)
		B.image_lait=X.join(U(G));D(B.image_lait);D(B.quantite_de_lait);A.show(C(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(X);F=[];H=S
		for G in U(g(I)):
			if Z in G and not H:
				F.append(G.replace(Z,Y,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				H=E
			else:F.append(G)
		B.image_lait=X.join(U(g(F)));D(B.image_lait);D(B.quantite_de_lait);A.show(C(B.image_lait))
	def mode_compteur(B):
		A.show(C(B.image_lait));K('ab')
		while E:
			if T.is_touched():B.menu()
			if G.is_pressed()and H.is_pressed():
				if B.quantite_de_lait==0:A.scroll('0ml')
				else:A.scroll(F(B.quantite_de_lait)+'00ml')
				A.show(C(B.image_lait));I(1000)
				if G.is_pressed()and H.is_pressed():B.image_lait=h;B.quantite_de_lait=0;A.show(C(B.image_lait))
			elif G.is_pressed():
				if K(V):B.add_lait();K(V)
			elif H.is_pressed():
				if K(W):B.remove_lait();K(W)
	def mode_status(B):
		C=0;A.show(B.IMAGE_SLEEP_SEQUENCE[1])
		while E:
			if T.is_touched():B.menu()
			D=J.receive()
			if D=='STATUSr|6|ASLEEP':
				C+=1
				if C%5==0:A.show(B.IMAGE_SLEEP_SEQUENCE[0])
				elif C%2==0:A.show(B.IMAGE_SLEEP_SEQUENCE[2])
				else:A.show(B.IMAGE_SLEEP_SEQUENCE[1])
	def mode_temperature(B):
		while not T.is_touched():A.show('x')
		B.menu()
	def mode_find(C):
		while not T.is_touched():
			B=J.receive_full()
			if B:
				B=B[1];D(B)
				if B<-120:A.show(Y)
				elif B>-40:A.show(Z)
				else:A.show(abs(B)//10-2)
		C.menu()
class o(e):
	def __init__(A,id):super().__init__(id);A.statut=0;A.main()
	def main(A):
		while E:L(B,'STATUT',A.statut);I(1000)
if not j:O=k();A.show(F(O));I(500);A.clear();m()
else:O=0
f=l()
if f==R:p=n(O)
elif f==Q:p=o(O)
else:A.scroll('ROLE ERROR')