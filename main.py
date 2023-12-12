# le code original se trouve dans src/source.py
A3='STARTLIGHT'
A2='STOPLIGHT'
A1='STOPFIND'
A0='STARTFIND'
z='GETTEMP'
y='STATUT'
x='c5:1'
w='e5:1'
v='g5:1'
u=reversed
q='E'
p='P'
o='90000:00000:00000:00000:00000'
n='ab'
m='c6:1'
l='00000:00000:90909:00000:00000'
k=enumerate
i='ROLE'
h='ID'
g='SETQLAIT'
f='0ml'
e='00000:00000:00000:00000:00000'
d=list
b='CMD'
a='a'
Z=len
Y=int
W='b'
V=ord
T=':'
R='0'
Q='9'
J=False
H=print
F=str
D=True
import sys,random,music as G,radio as O
from microbit import button_a as L,button_b as M,pin_logo as c,sleep as K,display as A,Image as E,accelerometer as j,temperature as r,microphone as A4
A5=J
C=J
A6='09999:00000:00000:00000:00000'
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
O.on()
O.config(channel=69,group=42)
def AD():0
def X(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=Y(A);return A
	if B:
		A=V(B[0])<<7;D=1000003
		for E in B:A=C(A*D^V(E))
		A^=Z(B)
		if A==-1:A=-2
		return F(A)
	return''
def A7():
	R='CHECK';Q='superhash_of_a: {}';P='a: {}';M='SCE';global B
	if U==1:
		if not C:G.play(v)
		L=random.randint(0,999999999);H(P.format(L));I(B,M,L);N=X(X(F(L)));H(Q.format(N));A.show(E(l))
		while D:
			J=S(O.receive(),B)
			if J and J[0]==M:
				if J[2]==N:
					B=B+X(F(L));K(500);I(B,M,R)
					if not C:G.play(m)
					A.show(E.YES);K(500);return
				A.show(E.NO)
				if not C:G.play('c#:1')
				sys.exit()
	if U==2:
		if not C:G.play(w)
		A.show(E(l))
		while D:
			J=S(O.receive(),B)
			if J and J[0]==M:break
		L=Y(J[2]);H(P.format(L));N=X(X(F(L)));H(Q.format(N));I(B,M,N);B=B+X(F(L))
		while D:
			J=S(O.receive(),B)
			if J and J[0]==M:
				if J[2]==R:
					if not C:G.play(x)
					A.show(E.YES);K(500);return
				A.show(E.NO)
				if not C:G.play('bb:1')
				sys.exit()
def N(button):
	A=button
	if A.lower()==a:
		while L.is_pressed()and not M.is_pressed():0
		if M.is_pressed():return J
		return D
	if A.lower()==W:
		while M.is_pressed()and not L.is_pressed():0
		if L.is_pressed():return J
		return D
	if A.lower()==n:
		while L.is_pressed()or M.is_pressed():0
def s(message,key,decryption=J):
	G=decryption;D='';H=Z(key);E=[V(A)for A in key]
	for(I,A)in k(F(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((V(A.upper())-E[C]+26)%26+V('A'))
			else:B=chr((V(A.upper())+E[C]-26)%26+V('A'))
			if A.islower():B=B.lower()
			D+=B
		elif A.isdigit():
			C=I%H
			if G:B=F((Y(A)-E[C])%10)
			else:B=F((Y(A)+E[C])%10)
			D+=B
		else:D+=A
	return D
def S(encrypted_packet,key):
	C=encrypted_packet;B=None
	if not C:return
	A=s(C,key,D).split('|')
	try:
		F=A[0]
		try:E=Y(A[1])
		except ValueError:E=B
		G=A[2];return F,E,G
	except IndexError:H('Mauvais packet reçu : {}'.format(A));return B,B,B
def I(key,t,content):B=content;A='{}|{}|{}'.format(t,F(Z(F(B))),F(B));A=s(A,key);O.send(A)
class A8:
	def __init__(A):A.StrucMdpActu=o;A.StrucMdpFin=A6;A.imageMdp=E(A.StrucMdpActu);A.placedPinMdp=e
	def check_entered_password(A):
		B=J
		if A.StrucMdpFin==A.placedPinMdp:B=D
		A.placedPinMdp=e;return B
	def cursor_change_position(A,direction):
		C=direction
		for(B,E)in k(A.StrucMdpActu):
			if E==Q:
				if C=='r':
					if B==28:A.StrucMdpActu='00000:00000:00000:00000:00009';return D
					if A.StrucMdpActu[B+1]==T:A.StrucMdpActu=A.StrucMdpActu[:B]+'0:'+Q+A.StrucMdpActu[B+3:];return D
					A.StrucMdpActu=A.StrucMdpActu[:B]+R+Q+A.StrucMdpActu[B+2:];return D
				if C=='l':
					if A.StrucMdpActu[B-1]==T:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'9:'+R+A.StrucMdpActu[B+1:];return D
					if A.StrucMdpActu[B-2]==T:A.StrucMdpActu=A.StrucMdpActu[:B-2]+':9'+R+A.StrucMdpActu[B+1:]
					elif B==1:A.StrucMdpActu=o;return D
					elif B==0:A.StrucMdpActu=o;return D
					else:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'09'+R+A.StrucMdpActu[B+1:]
					return D
	def place_pin_for_password(A):
		for(B,C)in k(A.StrucMdpActu):
			if C==Q:
				if B==0:A.placedPinMdp=Q+A.placedPinMdp[1:]
				elif B==29:A.placedPinMdp=A.placedPinMdp[0:-1]+Q
				elif A.placedPinMdp[B-1]==T:A.placedPinMdp=A.placedPinMdp[0:B-1]+':9'+A.placedPinMdp[B+1:]
				else:A.placedPinMdp=A.placedPinMdp[0:B]+Q+A.placedPinMdp[B+1:]
				H(B,'index');H(A.placedPinMdp);return D
	def show_image_placed_pins(B):A.show(E(B.placedPinMdp));H(B.placedPinMdp);K(500)
def A9():
	F=0;B=A8()
	while D:
		A.show(E(B.StrucMdpActu))
		if L.is_pressed()and M.is_pressed():
			if not C:
				if F>2:G.play(['c3:1'])
				else:G.play(['g4:1'])
			F+=1;B.place_pin_for_password();N(n)
		if L.is_pressed():
			if N(a):B.cursor_change_position(direction='l');N(a)
		if M.is_pressed():
			if N(W):B.cursor_change_position(direction='r');N(W)
		if F==4:
			if B.check_entered_password():B.show_image_placed_pins();A.show(E.YES);K(500);A.clear();return D
			B.show_image_placed_pins();A.show(E.NO);K(500);A.clear();F=0
class t:
	def __init__(A,id):A.id=id
class AA(t):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=e;A.index_menu=0;A.light=J;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find),('L',A.mode_light)];A.IMAGE_SLEEP_SEQUENCE=[E('00000:00000:99099:00000:09990'),E('00000:99990:00900:09000:99990'),E('09999:00090:00900:09999:00000')];A9();A.menu()
	def menu(B):
		A.clear();K(100)
		while D:
			A.show(B.menu_items[B.index_menu][0])
			if L.is_pressed()and M.is_pressed():A.clear();K(100);B.menu_items[B.index_menu][1]()
			elif L.is_pressed():
				if N(a):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=Z(B.menu_items)-1
			elif M.is_pressed():
				if N(W):
					B.index_menu+=1
					if B.index_menu>Z(B.menu_items)-1:B.index_menu=0
	def add_lait(B):
		K=B.image_lait.split(T);F=[];G=J
		for C in d(K):
			if Q in C and not G:
				I=C.rfind(Q);F.append(C[:I]+R+C[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				G=D
			else:F.append(C)
		B.image_lait=T.join(d(F));H(B.image_lait);H(B.quantite_de_lait);A.show(E(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(T);C=[];G=J
		for F in d(u(I)):
			if R in F and not G:
				C.append(F.replace(R,Q,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				G=D
			else:C.append(F)
		B.image_lait=T.join(d(u(C)));H(B.image_lait);H(B.quantite_de_lait);A.show(E(B.image_lait))
	def mode_compteur(C):
		A.show(E(C.image_lait));N(n)
		while not c.is_touched():
			if L.is_pressed()and M.is_pressed():
				if C.quantite_de_lait==0:A.scroll(f)
				else:A.scroll(F(C.quantite_de_lait)+f)
				A.show(E(C.image_lait));K(1000)
				if L.is_pressed()and M.is_pressed():C.image_lait=e;C.quantite_de_lait=0;I(B,g,F(C.quantite_de_lait));A.show(E(C.image_lait))
			elif L.is_pressed():
				if N(a):C.add_lait();I(B,g,F(C.quantite_de_lait));N(a)
			elif M.is_pressed():
				if N(W):C.remove_lait();I(B,g,F(C.quantite_de_lait));N(W)
		C.menu()
	def mode_statut(E):
		A.show(R)
		while not c.is_touched():
			D=S(O.receive(),B)
			if D and D[0]==y:
				A.show(F(D[2]))
				if not C:
					if D[2]==R:G.play(['c4:1'])
					elif D[2]=='1':G.play(['e4:1'])
					else:G.play(['e5:4'])
		E.menu()
	def mode_temperature(D):
		I(B,b,z)
		while not c.is_touched():
			C=S(O.receive(),B)
			if C:
				if C[0]=='TEMP':A.scroll(F(C[2]));break
		D.menu()
	def mode_find(D):
		I(B,b,A0)
		while not c.is_touched():
			C=O.receive_full()
			if C:
				C=C[1];H(C)
				if C<-120:A.show(Q)
				elif C>-30:A.show(R)
				else:A.show(abs(C)//10-2)
		I(B,b,A1);D.menu()
	def mode_light(C):
		if C.light:I(B,b,A2);A.show(E.NO);K(1000);A.clear();C.light=J
		else:I(B,b,A3);A.show(E.YES);K(1000);A.clear();C.light=D
		C.menu()
class AB(t):
	def __init__(A,id):super().__init__(id);A.statut=0;A.old_statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.playing_music=J;A.quantite_de_lait=0;A.findmode=J;A.show_statut=D;A.main()
	def main(C):
		X='99999:99999:99999:99999:99999';V='PING';T=0
		while D:
			for a in range(10000):
				P=S(O.receive(),B)
				if a%500==0:
					if C.findmode:I(B,V,V)
					U=(j.get_x()+j.get_y()+j.get_z()+A4.sound_level()*100)/4;c=abs((U-T)/100);C.history.append(c);C.history.pop(0);Q=sum(C.history)/Z(C.history)
					if Q<.8:
						C.statut=0
						if C.show_statut:A.show(R)
					elif Q<3.:
						C.statut=1
						if C.show_statut:A.show('1')
					elif Q<4.:
						C.statut=2
						if C.show_statut:A.show('2')
					T=U
				if C.statut!=C.old_statut:I(B,y,F(C.statut));C.old_statut=C.statut
				if M.is_pressed()and C.statut>0:
					if not C.playing_music:G.play(G.PYTHON,wait=J);C.playing_music=D
					else:G.stop();C.playing_music=J
					N(W)
				if L.is_pressed():
					if C.quantite_de_lait==0:A.scroll(f)
					else:A.scroll(F(C.quantite_de_lait)+f)
					if not C.show_statut:A.show(E(X))
				if P:
					if P[0]==b:
						if P[2]==z:K(100);I(B,'TEMP',F(r()));H('TEMP: {}'.format(r()))
						elif P[2]==A0:C.findmode=D
						elif P[2]==A1:C.findmode=J
						elif P[2]==A3:A.show(E(X));C.show_statut=J
						elif P[2]==A2:A.clear();C.show_statut=D
					elif P[0]==g:C.quantite_de_lait=Y(P[2]);H('SETQLAIT: {}'.format(C.quantite_de_lait))
if not C:G.play(m)
if not A5:
	A.show(E(l));I(B,h,'ASK')
	while D:
		P=S(O.receive(),B)
		if P:
			if P[0]==h and P[2]=='ASK':
				I(B,h,'CONF');H('ID: 2')
				if not C:G.play(m)
				U=2;break
			if P[0]==h and P[2]=='CONF':
				H('ID: 1')
				if not C:G.play(x)
				U=1;break
	A.show(F(U));K(500);A.clear();A7()
else:U=0
A.show('?')
while D:
	P=S(O.receive(),B)
	if L.is_pressed()or P and P[0]==i and P[2]==p:
		I(B,i,q);A.show(p);K(1000);A.clear();H('Parent')
		if not C:G.play(v)
		AC=AA(U);break
	if M.is_pressed()or P and P[0]==i and P[2]==q:
		I(B,i,p);A.show(q);K(1000);A.clear();H('Child')
		if not C:G.play(w)
		AC=AB(U);break