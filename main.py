# le code original se trouve dans src/source.py
s='TEMP'
r='GETTEMP'
q='CMD'
p='STATUT'
o=reversed
j='SETQLAIT'
i='0ml'
h='90000:00000:00000:00000:00000'
g='00000:00000:90909:00000:00000'
f=enumerate
c='00000:00000:00000:00000:00000'
b=list
a=len
Y='E'
X='P'
W='a'
V=int
S='b'
R=ord
Q=':'
O='0'
N=False
M='9'
F=print
E=str
C=True
from microbit import button_a as H,button_b as I,pin_logo as Z,sleep as G,display as A,Image as D,accelerometer as d,microphone as t
import music as e,sys,radio as J,random as u
from microbit import temperature as k
v=N
w='09999:00000:00000:00000:00000'
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
J.on()
J.config(channel=69,group=42)
def x():
	I='CONF';H='ASK';G='ID';A.show(D(g));L(B,G,H)
	while C:
		E=P(J.receive(),B)
		if E:
			if E[0]==G and E[2]==H:L(B,G,I);F('ID: 2');return 2
			if E[0]==G and E[2]==I:F('ID: 1');return 1
def y():
	E='ROLE';A.show('?')
	while C:
		D=P(J.receive(),B)
		if H.is_pressed()or D and D[0]==E and D[2]==X:L(B,E,Y);A.show(X);G(1000);A.clear();F('Parent');return X
		if I.is_pressed()or D and D[0]==E and D[2]==Y:L(B,E,X);A.show(Y);G(1000);A.clear();F('Child');return Y
def T(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=V(A);return A
	if B:
		A=R(B[0])<<7;D=1000003
		for F in B:A=C(A*D^R(F))
		A^=a(B)
		if A==-1:A=-2
		return E(A)
	return''
def z():
	Q='CHECK';O='superhash_of_a: {}';N='a: {}';K='SCE';global B
	if U==1:
		I=u.randint(0,999999999);F(N.format(I));L(B,K,I);M=T(T(E(I)));F(O.format(M));A.show(D(g))
		while C:
			H=P(J.receive(),B)
			if H:
				if H[0]==K:
					if H[2]==M:B=B+T(E(I));G(500);L(B,K,Q);A.show(D.YES);G(500);return
					A.show(D.NO);sys.exit()
	if U==2:
		A.show(D(g))
		while C:
			H=P(J.receive(),B)
			if H:
				if H[0]==K:break
		I=V(H[2]);F(N.format(I));M=T(T(E(I)));F(O.format(M));L(B,K,M);B=B+T(E(I))
		while C:
			H=P(J.receive(),B)
			if H:
				if H[0]==K:
					if H[2]==Q:A.show(D.YES);G(500);return
					A.show(D.NO);sys.exit()
def K(button):
	A=button
	if A.lower()==W:
		while H.is_pressed()and not I.is_pressed():0
		if I.is_pressed():return N
		return C
	if A.lower()==S:
		while I.is_pressed()and not H.is_pressed():0
		if H.is_pressed():return N
		return C
	if A.lower()=='ab':
		while H.is_pressed()or I.is_pressed():0
def l(message,key,decryption=N):
	G=decryption;D='';H=a(key);F=[R(A)for A in key]
	for(I,A)in f(E(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((R(A.upper())-F[C]+26)%26+R('A'))
			else:B=chr((R(A.upper())+F[C]-26)%26+R('A'))
			if A.islower():B=B.lower()
			D+=B
		elif A.isdigit():
			C=I%H
			if G:B=E((V(A)-F[C])%10)
			else:B=E((V(A)+F[C])%10)
			D+=B
		else:D+=A
	return D
def P(encrypted_packet,key):
	D=encrypted_packet;B=None
	if not D:return
	A=l(D,key,C).split('|')
	try:
		G=A[0]
		try:E=V(A[1])
		except ValueError:E=B
		H=A[2];return G,E,H
	except IndexError:F('Mauvais packet reçu : {}'.format(A));return B,B,B
def L(key,t,content):B=content;A='{}|{}|{}'.format(t,E(a(E(B))),E(B));A=l(A,key);J.send(A)
class A0:
	def __init__(A):A.StrucMdpActu=h;A.StrucMdpFin=w;A.imageMdp=D(A.StrucMdpActu);A.placedPinMdp=c
	def check_entry(A):
		B=N
		if A.StrucMdpFin==A.placedPinMdp:B=C
		A.placedPinMdp=c;return B
	def change_position(A,direction):
		D=direction
		for(B,E)in f(A.StrucMdpActu):
			if E==M:
				if D=='r':
					if B==28:A.StrucMdpActu='00000:00000:00000:00000:00009';return C
					if A.StrucMdpActu[B+1]==Q:A.StrucMdpActu=A.StrucMdpActu[:B]+'0:'+M+A.StrucMdpActu[B+3:];return C
					A.StrucMdpActu=A.StrucMdpActu[:B]+O+M+A.StrucMdpActu[B+2:];return C
				if D=='l':
					if A.StrucMdpActu[B-1]==Q:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'9:'+O+A.StrucMdpActu[B+1:];return C
					if A.StrucMdpActu[B-2]==Q:A.StrucMdpActu=A.StrucMdpActu[:B-2]+':9'+O+A.StrucMdpActu[B+1:]
					elif B==1:A.StrucMdpActu=h;return C
					elif B==0:A.StrucMdpActu=h;return C
					else:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'09'+O+A.StrucMdpActu[B+1:]
					return C
	def place_pin_mdp(A):
		for(B,D)in f(A.StrucMdpActu):
			if D==M:
				if B==0:A.placedPinMdp=M+A.placedPinMdp[1:]
				elif B==29:A.placedPinMdp=A.placedPinMdp[0:-1]+M
				elif A.placedPinMdp[B-1]==Q:A.placedPinMdp=A.placedPinMdp[0:B-1]+':9'+A.placedPinMdp[B+1:]
				else:A.placedPinMdp=A.placedPinMdp[0:B]+M+A.placedPinMdp[B+1:]
				F(B,'index');F(A.placedPinMdp);return C
	def show_image_pin_placed(B):A.show(D(B.placedPinMdp));F(B.placedPinMdp);G(500)
def A1():
	E=0;B=A0()
	while C:
		A.show(D(B.StrucMdpActu))
		if H.is_pressed()and I.is_pressed():E+=1;G(1000);B.place_pin_mdp()
		if H.is_pressed():
			if K(W):B.change_position(direction='l');K(W)
		if I.is_pressed():
			if K(S):B.change_position(direction='r');K(S)
		if E==4:
			if B.check_entry():B.show_image_pin_placed();A.show(D.YES);G(500);A.clear();return C
			B.show_image_pin_placed();A.show(D.NO);G(500);A.clear();E=0
class m:
	def __init__(A,id):A.id=id
class A2(m):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=c;A.index_menu=0;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find)];A.IMAGE_SLEEP_SEQUENCE=[D('00000:00000:99099:00000:09990'),D('00000:99990:00900:09000:99990'),D('09999:00090:00900:09999:00000')];A1();A.menu()
	def menu(B):
		A.clear();G(100)
		while C:
			A.show(B.menu_items[B.index_menu][0])
			if H.is_pressed()and I.is_pressed():A.clear();G(100);B.menu_items[B.index_menu][1]()
			elif H.is_pressed():
				if K(W):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=3
			elif I.is_pressed():
				if K(S):
					B.index_menu+=1
					if B.index_menu>3:B.index_menu=0
	def add_lait(B):
		J=B.image_lait.split(Q);G=[];H=N
		for E in b(J):
			if M in E and not H:
				I=E.rfind(M);G.append(E[:I]+O+E[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				H=C
			else:G.append(E)
		B.image_lait=Q.join(b(G));F(B.image_lait);F(B.quantite_de_lait);A.show(D(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(Q);E=[];H=N
		for G in b(o(I)):
			if O in G and not H:
				E.append(G.replace(O,M,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				H=C
			else:E.append(G)
		B.image_lait=Q.join(b(o(E)));F(B.image_lait);F(B.quantite_de_lait);A.show(D(B.image_lait))
	def mode_compteur(C):
		A.show(D(C.image_lait));K('ab')
		while not Z.is_touched():
			if H.is_pressed()and I.is_pressed():
				if C.quantite_de_lait==0:A.scroll(i)
				else:A.scroll(E(C.quantite_de_lait)+i)
				A.show(D(C.image_lait));G(1000)
				if H.is_pressed()and I.is_pressed():C.image_lait=c;C.quantite_de_lait=0;A.show(D(C.image_lait))
			elif H.is_pressed():
				if K(W):C.add_lait();L(B,j,E(C.quantite_de_lait));K(W)
			elif I.is_pressed():
				if K(S):C.remove_lait();L(B,j,E(C.quantite_de_lait));K(S)
		C.menu()
	def mode_statut(D):
		while not Z.is_touched():
			C=P(J.receive(),B)
			if C and C[0]==p:A.show(E(C[2]))
		D.menu()
	def mode_temperature(D):
		L(B,q,r)
		while not Z.is_touched():
			C=P(J.receive(),B)
			if C:
				if C[0]==s:A.scroll(E(C[2]));break
		D.menu()
	def mode_find(C):
		while not Z.is_touched():
			B=J.receive_full()
			if B:
				B=B[1];F(B)
				if B<-120:A.show(M)
				elif B>-40:A.show(O)
				else:A.show(abs(B)//10-2)
		C.menu()
class A3(m):
	def __init__(A,id):super().__init__(id);A.statut=0;A.old_statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.playing_music=N;A.quantite_de_lait=0;A.main()
	def main(D):
		R=0
		while C:
			for U in range(10000):
				M=P(J.receive(),B)
				if U%500==0:
					T=(d.get_x()+d.get_y()+d.get_z()+t.sound_level()*100)/4;W=abs((T-R)/100);D.history.append(W);D.history.pop(0);Q=sum(D.history)/a(D.history)
					if Q<.8:D.statut=0;A.show(O)
					elif Q<3.:D.statut=1;A.show('1')
					elif Q<4.:D.statut=2;A.show('2')
					R=T
				if D.statut!=D.old_statut:L(B,p,E(D.statut));D.old_statut=D.statut
				if I.is_pressed()and D.statut>0:
					if not D.playing_music:e.play(e.PYTHON,wait=N);D.playing_music=C
					else:e.stop();D.playing_music=N
					K(S)
				if H.is_pressed():A.scroll(E(D.quantite_de_lait)+i)
				if M:
					if M[0]==q and M[2]==r:G(100);L(B,s,E(k()));F('TEMP: {}'.format(k()))
					if M[0]==j:D.quantite_de_lait=V(M[2]);F('SETQLAIT: {}'.format(D.quantite_de_lait))
if not v:U=x();A.show(E(U));G(500);A.clear();z()
else:U=0
n=y()
if n==X:A4=A2(U)
elif n==Y:A4=A3(U)
else:A.scroll('ROLE ERROR')