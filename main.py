# le code original se trouve dans src/source.py
A2='STARTLIGHT'
A1='STOPLIGHT'
A0='STOPFIND'
z='STARTFIND'
y='STATUT'
x='e5:1'
w='g5:1'
v=reversed
r='E'
q='P'
p='90000:00000:00000:00000:00000'
o='ab'
n='c5:1'
m='c6:1'
l='00000:00000:90909:00000:00000'
k='ROLE'
j='ID'
i='SETQLAIT'
h='0ml'
g='00000:00000:00000:00000:00000'
f=list
e=enumerate
c='CMD'
b='a'
a=len
Z=int
W='b'
V=ord
S=':'
R='0'
Q='9'
K=False
H=print
G=str
E=True
import sys,random,music as F,radio as P
from microbit import button_a as L,button_b as M,pin_logo as d,sleep as I,display as A,Image as B,accelerometer as X,temperature as s,microphone as A3
A4=K
C=K
A5=K
A6='09999:00000:00000:00000:00000'
D='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
P.on()
P.config(channel=69,group=42)
def Y(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=Z(A);return A
	if B:
		A=V(B[0])<<7;D=1000003
		for E in B:A=C(A*D^V(E))
		A^=a(B)
		if A==-1:A=-2
		return G(A)
	return''
def A7():
	R='CHECK';Q='superhash_of_a: {}';O='a: {}';M='SCE';global D
	if U==1:
		if not C:F.play(w)
		L=random.randint(0,999999999);H(O.format(L));J(D,M,L);N=Y(Y(G(L)));H(Q.format(N));A.show(B(l))
		while E:
			K=T(P.receive(),D)
			if K and K[0]==M:
				if K[2]==N:
					D=D+Y(G(L));I(500);J(D,M,R)
					if not C:F.play(m)
					A.show(B.YES);I(500);return
				A.show(B.NO)
				if not C:F.play('c#:1')
				sys.exit()
	if U==2:
		if not C:F.play(x)
		A.show(B(l))
		while E:
			K=T(P.receive(),D)
			if K and K[0]==M:break
		L=Z(K[2]);H(O.format(L));N=Y(Y(G(L)));H(Q.format(N));J(D,M,N);D=D+Y(G(L))
		while E:
			K=T(P.receive(),D)
			if K and K[0]==M:
				if K[2]==R:
					if not C:F.play(n)
					A.show(B.YES);I(500);return
				A.show(B.NO)
				if not C:F.play('bb:1')
				sys.exit()
def N(button):
	A=button
	if A.lower()==b:
		while L.is_pressed()and not M.is_pressed():0
		if M.is_pressed():return K
		return E
	if A.lower()==W:
		while M.is_pressed()and not L.is_pressed():0
		if L.is_pressed():return K
		return E
	if A.lower()==o:
		while L.is_pressed()or M.is_pressed():0
def u(message,key,decryption=K):
	F=decryption;D='';H=a(key);E=[V(A)for A in key]
	for(I,A)in e(G(message)):
		if A.isalpha():
			C=I%H
			if F:B=chr((V(A.upper())-E[C]+26)%26+V('A'))
			else:B=chr((V(A.upper())+E[C]-26)%26+V('A'))
			if A.islower():B=B.lower()
			D+=B
		elif A.isdigit():
			C=I%H
			if F:B=G((Z(A)-E[C])%10)
			else:B=G((Z(A)+E[C])%10)
			D+=B
		else:D+=A
	return D
def T(encrypted_packet,key):
	C=encrypted_packet;B=None
	if not C:return
	A=u(C,key,E).split('|')
	try:
		F=A[0]
		try:D=Z(A[1])
		except ValueError:D=B
		G=A[2];return F,D,G
	except IndexError:H('Mauvais packet reçu : {}'.format(A));return B,B,B
def J(key,t,content):B=content;A='{}|{}|{}'.format(t,G(a(G(B))),G(B));A=u(A,key);P.send(A)
class A8:
	def __init__(A):A.StrucMdpActu=p;A.StrucMdpFin=A6;A.imageMdp=B(A.StrucMdpActu);A.placedPinMdp=g
	def check_entered_password(A):
		B=K
		if A.StrucMdpFin==A.placedPinMdp:B=E
		A.placedPinMdp=g;return B
	def cursor_change_position(A,direction):
		C=direction
		for(B,D)in e(A.StrucMdpActu):
			if D==Q:
				if C=='r':
					if B==28:A.StrucMdpActu='00000:00000:00000:00000:00009';return E
					if A.StrucMdpActu[B+1]==S:A.StrucMdpActu=A.StrucMdpActu[:B]+'0:'+Q+A.StrucMdpActu[B+3:];return E
					A.StrucMdpActu=A.StrucMdpActu[:B]+R+Q+A.StrucMdpActu[B+2:];return E
				if C=='l':
					if A.StrucMdpActu[B-1]==S:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'9:'+R+A.StrucMdpActu[B+1:];return E
					if A.StrucMdpActu[B-2]==S:A.StrucMdpActu=A.StrucMdpActu[:B-2]+':9'+R+A.StrucMdpActu[B+1:]
					elif B==1:A.StrucMdpActu=p;return E
					elif B==0:A.StrucMdpActu=p;return E
					else:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'09'+R+A.StrucMdpActu[B+1:]
					return E
	def place_pin_for_password(A):
		for(B,C)in e(A.StrucMdpActu):
			if C==Q:
				if B==0:A.placedPinMdp=Q+A.placedPinMdp[1:]
				elif B==29:A.placedPinMdp=A.placedPinMdp[0:-1]+Q
				elif A.placedPinMdp[B-1]==S:A.placedPinMdp=A.placedPinMdp[0:B-1]+':9'+A.placedPinMdp[B+1:]
				else:A.placedPinMdp=A.placedPinMdp[0:B]+Q+A.placedPinMdp[B+1:]
				H(B,'index');H(A.placedPinMdp);return E
	def show_image_placed_pins(C):A.show(B(C.placedPinMdp));H(C.placedPinMdp);I(500)
def A9():
	G=0;D=A8()
	while E:
		A.show(B(D.StrucMdpActu))
		if L.is_pressed()and M.is_pressed():
			if not C:F.play(['c:1'])
			G+=1;D.place_pin_for_password();N(o)
		if L.is_pressed():
			if N(b):D.cursor_change_position(direction='l');N(b)
		if M.is_pressed():
			if N(W):D.cursor_change_position(direction='r');N(W)
		if G==4:
			if D.check_entered_password():
				D.show_image_placed_pins();A.show(B.YES)
				if not C:F.play(['g:1'])
				I(500);A.clear();return E
			D.show_image_placed_pins();A.show(B.NO)
			if not C:F.play(['g#3:1'])
			I(500);A.clear();G=0
class t:
	def __init__(A,id):A.id=id
class AA(t):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=g;A.index_menu=0;A.light=K;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find),('L',A.mode_light)];A.STATUT_IMAGES=[B.HAPPY,B('00900:00900:00900:00000:00900'),B('90909:90909:90909:00000:90909')];A9();A.menu()
	def menu(B):
		A.clear();I(100)
		while E:
			A.show(B.menu_items[B.index_menu][0])
			if L.is_pressed()and M.is_pressed():A.clear();I(100);B.menu_items[B.index_menu][1]()
			elif L.is_pressed():
				if N(b):
					B.index_menu-=1
					if B.index_menu<0:B.index_menu=a(B.menu_items)-1
			elif M.is_pressed():
				if N(W):
					B.index_menu+=1
					if B.index_menu>a(B.menu_items)-1:B.index_menu=0
	def add_lait(C):
		J=C.image_lait.split(S);F=[];G=K
		for D in f(J):
			if Q in D and not G:
				I=D.rfind(Q);F.append(D[:I]+R+D[I+1:])
				if C.quantite_de_lait>0:C.quantite_de_lait-=1
				G=E
			else:F.append(D)
		C.image_lait=S.join(f(F));H(C.image_lait);H(C.quantite_de_lait);A.show(B(C.image_lait))
	def remove_lait(C):
		I=C.image_lait.split(S);D=[];G=K
		for F in f(v(I)):
			if R in F and not G:
				D.append(F.replace(R,Q,1))
				if C.quantite_de_lait<25:C.quantite_de_lait+=1
				G=E
			else:D.append(F)
		C.image_lait=S.join(f(v(D)));H(C.image_lait);H(C.quantite_de_lait);A.show(B(C.image_lait))
	def mode_compteur(C):
		A.show(B(C.image_lait));N(o)
		while not d.is_touched():
			if L.is_pressed()and M.is_pressed():
				if C.quantite_de_lait==0:A.scroll(h)
				else:A.scroll(G(C.quantite_de_lait)+h)
				A.show(B(C.image_lait));I(1000)
				if L.is_pressed()and M.is_pressed():C.image_lait=g;C.quantite_de_lait=0;J(D,i,G(C.quantite_de_lait));A.show(B(C.image_lait))
			elif L.is_pressed():
				if N(b):C.add_lait();J(D,i,G(C.quantite_de_lait));N(b)
			elif M.is_pressed():
				if N(W):C.remove_lait();J(D,i,G(C.quantite_de_lait));N(W)
		C.menu()
	def mode_statut(B):
		A.show(B.STATUT_IMAGES[0])
		while not d.is_touched():
			E=T(P.receive(),D)
			if E and E[0]==y:
				if E[2]==R:A.show(B.STATUT_IMAGES[0])
				elif E[2]=='1':
					A.show(B.STATUT_IMAGES[1])
					if not C:F.play(['e4:1'])
				else:
					A.show(B.STATUT_IMAGES[2])
					if not C:F.play(['e5:8'])
		B.menu()
	def mode_temperature(B):A.scroll('22C');B.menu()
	def mode_find(L):
		K='00900:00900:00900:00000:00000';J(D,c,z);M=[B(K),B('00009:00090:00900:00000:00000'),B('00000:00090:00999:00000:00000'),B('00000:00070:00900:00090:00009'),B('00000:00050:00900:00900:00900'),B('00000:00030:00900:09000:90000'),B('00000:00020:99900:00000:00000'),B('90000:09010:00900:00000:00000')]
		for(G,N)in e(M*2):
			if d.is_touched():break
			A.show(N)
			if(G==1 or G==10)and not C:F.play(n)
			I(200)
		A.show(B(K));I(200)
		while not d.is_touched():
			E=P.receive_full()
			if E:
				E=E[1];H(E)
				if E<-120:A.show(Q)
				elif E>-30:A.show(R)
				else:A.show(abs(E)//10-2)
		J(D,c,A0);L.menu()
	def mode_light(C):
		if C.light:J(D,c,A1);A.show(B.NO);I(1000);A.clear();C.light=K
		else:J(D,c,A2);A.show(B.YES);I(1000);A.clear();C.light=E
		C.menu()
class AB(t):
	def __init__(A,id):super().__init__(id);A.statut=0;A.old_statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.playing_music=K;A.quantite_de_lait=0;A.findmode=K;A.show_statut=E;A.main()
	def main(C):
		Y='99999:99999:99999:99999:99999';V='PING';U=0
		while E:
			for b in range(10000):
				O=T(P.receive(),D)
				if b%500==0:
					if C.findmode:J(D,V,V)
					if A5:Q=(X.get_x()+X.get_y()+X.get_z()+A3.sound_level()*100)/4
					else:Q=(X.get_x()+X.get_y()+X.get_z())/3
					d=abs((Q-U)/100);C.history.append(d);C.history.pop(0);S=sum(C.history)/a(C.history)
					if S<.8:
						C.statut=0
						if C.show_statut:A.show(R)
					elif S<3.:
						C.statut=1
						if C.show_statut:A.show('1')
					elif S<4.:
						C.statut=2
						if C.show_statut:A.show('2')
					U=Q
				if C.statut!=C.old_statut:
					if not(C.statut==1 and C.old_statut==2):J(D,y,G(C.statut))
					C.old_statut=C.statut
				if M.is_pressed():
					if C.playing_music:F.stop();C.playing_music=K
					if C.statut>0:
						if not C.playing_music:F.play(F.PYTHON,wait=K);C.playing_music=E
					N(W)
				if L.is_pressed():
					if C.quantite_de_lait==0:A.scroll(h)
					else:A.scroll(G(C.quantite_de_lait)+h)
					if not C.show_statut:A.show(B(Y))
				if O:
					if O[0]==c:
						if O[2]=='GETTEMP':I(100);J(D,'TEMP',G(s()));H('TEMP: {}'.format(s()))
						elif O[2]==z:C.findmode=E
						elif O[2]==A0:C.findmode=K
						elif O[2]==A2:A.show(B(Y));C.show_statut=K
						elif O[2]==A1:A.clear();C.show_statut=E
					elif O[0]==i:C.quantite_de_lait=Z(O[2]);H('SETQLAIT: {}'.format(C.quantite_de_lait))
if not C:F.play(m)
if not A4:
	A.show(B(l));J(D,j,'ASK')
	while E:
		O=T(P.receive(),D)
		if O:
			if O[0]==j and O[2]=='ASK':
				J(D,j,'CONF');H('ID: 2')
				if not C:F.play(m)
				U=2;break
			if O[0]==j and O[2]=='CONF':
				H('ID: 1')
				if not C:F.play(n)
				U=1;break
	A.show(G(U));I(500);A.clear();A7()
else:U=0
A.show('?')
while E:
	O=T(P.receive(),D)
	if L.is_pressed()or O and O[0]==k and O[2]==q:
		J(D,k,r);A.show(q);I(1000);A.clear();H('Parent')
		if not C:F.play(w)
		AC=AA(U);break
	if M.is_pressed()or O and O[0]==k and O[2]==r:
		J(D,k,q);A.show(r);I(1000);A.clear();H('Child')
		if not C:F.play(x)
		AC=AB(U);break