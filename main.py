e='00000:00000:00000:00000:00000'
a='0'
Z='9'
Y=False
X='00000:00000:90909:00000:00000'
W=len
U='b'
T='a'
R='P'
Q='E'
P=int
M=ord
F=True
E=str
C=print
from microbit import button_a as G,button_b as H,pin_logo as S,sleep as I,display as A,Image as D
import sys,radio as J,random as f
g=F
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
J.on()
J.config(channel=69,group=42)
def h():
	I='CONF';H='ASK';G='ID';A.show(D(X));L(B,G,H)
	while F:
		E=V(J.receive(),B)
		if E:
			if E[0]==G and E[2]==H:L(B,G,I);C('ID: 2');return 2
			if E[0]==G and E[2]==I:C('ID: 1');return 1
def i():
	E='ROLE';A.show('?')
	while F:
		D=J.receive()
		if G.is_pressed()or D==Q:L(B,E,Q);A.show(R);I(1000);A.clear();C('Parent');return R
		if H.is_pressed()or D==R:L(B,E,R);A.show(Q);I(1000);A.clear();C('Child');return Q
def N(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=P(A);return A
	if B:
		A=M(B[0])<<7;D=1000003
		for F in B:A=C(A*D^M(F))
		A^=W(B)
		if A==-1:A=-2
		return E(A)
	return''
def j():
	R='superhash_of_a: {}';Q='a: {}';M='SCE';global B
	if O==1:
		G=f.randint(0,999999999);C(Q.format(G));L(B,M,G);K=N(N(E(G)));C(R.format(K));A.show(D(X))
		while F:
			H=V(J.receive(),B)
			if H:
				if H[0]==M:
					if H[2]==K:B=B+N(E(G));A.show(D.YES);I(500);return
					A.show(D.NO);sys.exit()
	if O==2:
		A.show(D(X))
		while F:
			H=V(J.receive(),B)
			if H:
				if H[0]==M:break
		G=P(H[2]);C(Q.format(G));K=N(N(E(G)));C(R.format(K));L(B,M,K);B=B+N(E(G));A.show(D.YES);I(500)
def K(button):
	A=button
	if A.lower()==T:
		while G.is_pressed()and not H.is_pressed():0
		if H.is_pressed():return Y
		return F
	if A.lower()==U:
		while H.is_pressed()and not G.is_pressed():0
		if G.is_pressed():return Y
		return F
	if A.lower()=='ab':
		while G.is_pressed()or H.is_pressed():0
def b(message,key,decryption=Y):
	G=decryption;D='';H=W(key);F=[M(A)for A in key]
	for(I,A)in enumerate(E(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((M(A.upper())-F[C]+26)%26+M('A'))
			else:B=chr((M(A.upper())+F[C]-26)%26+M('A'))
			if A.islower():B=B.lower()
			D+=B
		elif A.isdigit():
			C=I%H
			if G:B=E((P(A)-F[C])%10)
			else:B=E((P(A)+F[C])%10)
			D+=B
		else:D+=A
	return D
def V(encrypted_packet,key):
	D=encrypted_packet;B=None
	if not D:return
	A=b(D,key,F).split('|')
	try:
		G=A[0]
		try:E=P(A[1])
		except ValueError:E=B
		H=A[2];return G,E,H
	except IndexError:C('Mauvais packet reçu : {}'.format(A));return B,B,B
def L(key,t,content):B=content;A='{}|{}|{}'.format(t,E(W(E(B))),E(B));A=b(A,key);J.send(A)
class c:
	def __init__(A,id):A.id=id
class k(c):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=e;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_status),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[D('00000:00000:99099:00000:09990'),D('00000:99990:00900:09000:99990'),D('09999:00090:00900:09999:00000')];A.menu()
	def menu(B):
		A.clear();I(100)
		while F:
			A.show(B.menu_items[B.index_menu][0])
			if G.is_pressed()and H.is_pressed():A.clear();I(100);B.menu_items[B.index_menu][1]()
			elif G.is_pressed():
				if K(T):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif H.is_pressed():
				if K(U):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		B.image_lait=B.image_lait.replace(Z,a,1);A.show(D(B.image_lait))
		if B.quantite_de_lait>0:B.quantite_de_lait-=1
		C(B.image_lait);C(B.quantite_de_lait)
	def remove_lait(B):
		E=B.image_lait.rfind(a)
		if E!=-1:B.image_lait=B.image_lait[:E]+Z+B.image_lait[E+1:]
		A.show(D(B.image_lait))
		if B.quantite_de_lait<25:B.quantite_de_lait+=1
		C(B.quantite_de_lait);C(B.image_lait);C(B.quantite_de_lait)
	def mode_compteur(B):
		A.show(D(B.image_lait));K('ab')
		while F:
			if S.is_touched():B.menu()
			if G.is_pressed()and H.is_pressed():
				A.scroll(E(B.quantite_de_lait));A.show(D(B.image_lait));I(1000)
				if G.is_pressed()and H.is_pressed():B.image_lait=e;B.quantite_de_lait=0;A.show(D(B.image_lait))
			elif G.is_pressed():
				if K(T):B.add_lait();K(T)
			elif H.is_pressed():
				if K(U):B.remove_lait();K(U)
	def mode_status(B):
		C=0;A.show(B.IMAGE_SLEEP_SEQUENCE[1])
		while F:
			if S.is_touched():B.menu()
			D=J.receive()
			if D=='STATUSr|6|ASLEEP':
				C+=1
				if C%5==0:A.show(B.IMAGE_SLEEP_SEQUENCE[0])
				elif C%2==0:A.show(B.IMAGE_SLEEP_SEQUENCE[2])
				else:A.show(B.IMAGE_SLEEP_SEQUENCE[1])
	def mode_temperature(B):
		while not S.is_touched():A.show('x')
		B.menu()
	def mode_find(D):
		while not S.is_touched():
			B=J.receive_full()
			if B:
				B=B[1];C(B)
				if B<-120:A.show(Z)
				elif B>-40:A.show(a)
				else:A.show(abs(B)//10-2)
		D.menu()
class l(c):
	def __init__(A,id):super().__init__(id);A.statut=0;A.main()
	def main(A):
		while F:L(B,'STATUT',A.statut);I(1000)
if not g:O=h();A.show(E(O));I(500);A.clear();j()
else:O=0
d=i()
if d==R:m=k(O)
elif d==Q:m=l(O)
else:A.scroll('ROLE ERROR')