# le code original se trouve dans src/source.py
A2='STARTLIGHT'
A1='STOPLIGHT'
A0='STOPFIND'
z='STARTFIND'
y='TEMP'
x='GETTEMP'
w='STATUT'
v='e5:1'
u='g5:1'
t='c5:1'
s=reversed
n='SETQLAIT'
m='90000:00000:00000:00000:00000'
l='ab'
k='c6:1'
j='00000:00000:90909:00000:00000'
i=enumerate
g='0ml'
f='00000:00000:00000:00000:00000'
e=list
c='E'
b='P'
a='a'
Z=len
Y=int
V='b'
U=ord
T=':'
R='CMD'
Q='0'
O='9'
J=False
H=print
F=str
D=True
from microbit import button_a as L,button_b as M,pin_logo as d,sleep as K,display as A,Image as E,accelerometer as h,temperature as o,microphone as A3
import music as G,sys,radio as P,random
A4=J
C=J
A5='09999:00000:00000:00000:00000'
B='9cnve2xgkzr2prowcdr5mxkjbxnts9m8h99dqru7'
P.on()
P.config(channel=69,group=42)
def A6():
	L='CONF';K='ASK';J='ID';A.show(E(j));I(B,J,K)
	while D:
		F=S(P.receive(),B)
		if F:
			if F[0]==J and F[2]==K:
				I(B,J,L);H('ID: 2')
				if not C:G.play(k)
				return 2
			if F[0]==J and F[2]==L:
				H('ID: 1')
				if not C:G.play(t)
				return 1
def A7():
	F='ROLE';A.show('?')
	while D:
		E=S(P.receive(),B)
		if L.is_pressed()or E and E[0]==F and E[2]==b:
			I(B,F,c);A.show(b);K(1000);A.clear();H('Parent')
			if not C:G.play(u)
			return b
		if M.is_pressed()or E and E[0]==F and E[2]==c:
			I(B,F,b);A.show(c);K(1000);A.clear();H('Child')
			if not C:G.play(v)
			return c
def W(string):
	B=string
	def C(value):
		A=value;A=A%2**32
		if A>=2**31:A=A-2**32
		A=Y(A);return A
	if B:
		A=U(B[0])<<7;D=1000003
		for E in B:A=C(A*D^U(E))
		A^=Z(B)
		if A==-1:A=-2
		return F(A)
	return''
def A8():
	R='CHECK';Q='superhash_of_a: {}';O='a: {}';M='SCE';global B
	if X==1:
		if not C:G.play(u)
		L=random.randint(0,999999999);H(O.format(L));I(B,M,L);N=W(W(F(L)));H(Q.format(N));A.show(E(j))
		while D:
			J=S(P.receive(),B)
			if J:
				if J[0]==M:
					if J[2]==N:
						B=B+W(F(L));K(500);I(B,M,R)
						if not C:G.play(k)
						A.show(E.YES);K(500);return
					A.show(E.NO)
					if not C:G.play('c#:1')
					sys.exit()
	if X==2:
		if not C:G.play(v)
		A.show(E(j))
		while D:
			J=S(P.receive(),B)
			if J:
				if J[0]==M:break
		L=Y(J[2]);H(O.format(L));N=W(W(F(L)));H(Q.format(N));I(B,M,N);B=B+W(F(L))
		while D:
			J=S(P.receive(),B)
			if J:
				if J[0]==M:
					if J[2]==R:
						if not C:G.play(t)
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
	if A.lower()==V:
		while M.is_pressed()and not L.is_pressed():0
		if L.is_pressed():return J
		return D
	if A.lower()==l:
		while L.is_pressed()or M.is_pressed():0
def p(message,key,decryption=J):
	G=decryption;D='';H=Z(key);E=[U(A)for A in key]
	for(I,A)in i(F(message)):
		if A.isalpha():
			C=I%H
			if G:B=chr((U(A.upper())-E[C]+26)%26+U('A'))
			else:B=chr((U(A.upper())+E[C]-26)%26+U('A'))
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
	A=p(C,key,D).split('|')
	try:
		F=A[0]
		try:E=Y(A[1])
		except ValueError:E=B
		G=A[2];return F,E,G
	except IndexError:H('Mauvais packet reçu : {}'.format(A));return B,B,B
def I(key,t,content):B=content;A='{}|{}|{}'.format(t,F(Z(F(B))),F(B));A=p(A,key);P.send(A)
class A9:
	def __init__(A):A.StrucMdpActu=m;A.StrucMdpFin=A5;A.imageMdp=E(A.StrucMdpActu);A.placedPinMdp=f
	def check_entry(A):
		B=J
		if A.StrucMdpFin==A.placedPinMdp:B=D
		A.placedPinMdp=f;return B
	def change_position(A,direction):
		C=direction
		for(B,E)in i(A.StrucMdpActu):
			if E==O:
				if C=='r':
					if B==28:A.StrucMdpActu='00000:00000:00000:00000:00009';return D
					if A.StrucMdpActu[B+1]==T:A.StrucMdpActu=A.StrucMdpActu[:B]+'0:'+O+A.StrucMdpActu[B+3:];return D
					A.StrucMdpActu=A.StrucMdpActu[:B]+Q+O+A.StrucMdpActu[B+2:];return D
				if C=='l':
					if A.StrucMdpActu[B-1]==T:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'9:'+Q+A.StrucMdpActu[B+1:];return D
					if A.StrucMdpActu[B-2]==T:A.StrucMdpActu=A.StrucMdpActu[:B-2]+':9'+Q+A.StrucMdpActu[B+1:]
					elif B==1:A.StrucMdpActu=m;return D
					elif B==0:A.StrucMdpActu=m;return D
					else:A.StrucMdpActu=A.StrucMdpActu[:B-2]+'09'+Q+A.StrucMdpActu[B+1:]
					return D
	def place_pin_mdp(A):
		for(B,C)in i(A.StrucMdpActu):
			if C==O:
				if B==0:A.placedPinMdp=O+A.placedPinMdp[1:]
				elif B==29:A.placedPinMdp=A.placedPinMdp[0:-1]+O
				elif A.placedPinMdp[B-1]==T:A.placedPinMdp=A.placedPinMdp[0:B-1]+':9'+A.placedPinMdp[B+1:]
				else:A.placedPinMdp=A.placedPinMdp[0:B]+O+A.placedPinMdp[B+1:]
				H(B,'index');H(A.placedPinMdp);return D
	def show_image_pin_placed(B):A.show(E(B.placedPinMdp));H(B.placedPinMdp);K(500)
def AA():
	F=0;B=A9()
	while D:
		A.show(E(B.StrucMdpActu))
		if L.is_pressed()and M.is_pressed():
			if not C:
				if F>2:G.play(['c3:1'])
				else:G.play(['g4:1'])
			F+=1;B.place_pin_mdp();N(l)
		if L.is_pressed():
			if N(a):B.change_position(direction='l');N(a)
		if M.is_pressed():
			if N(V):B.change_position(direction='r');N(V)
		if F==4:
			if B.check_entry():B.show_image_pin_placed();A.show(E.YES);K(500);A.clear();return D
			B.show_image_pin_placed();A.show(E.NO);K(500);A.clear();F=0
class q:
	def __init__(A,id):A.id=id
class AB(q):
	def __init__(A,id):super().__init__(id);A.quantite_de_lait=0;A.image_lait=f;A.index_menu=0;A.light=J;A.menu_items=[('C',A.mode_compteur),('S',A.mode_statut),('T',A.mode_temperature),('F',A.mode_find),('L',A.mode_light)];A.IMAGE_SLEEP_SEQUENCE=[E('00000:00000:99099:00000:09990'),E('00000:99990:00900:09000:99990'),E('09999:00090:00900:09999:00000')];AA();A.menu()
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
				if N(V):
					B.index_menu+=1
					if B.index_menu>Z(B.menu_items)-1:B.index_menu=0
	def add_lait(B):
		K=B.image_lait.split(T);F=[];G=J
		for C in e(K):
			if O in C and not G:
				I=C.rfind(O);F.append(C[:I]+Q+C[I+1:])
				if B.quantite_de_lait>0:B.quantite_de_lait-=1
				G=D
			else:F.append(C)
		B.image_lait=T.join(e(F));H(B.image_lait);H(B.quantite_de_lait);A.show(E(B.image_lait))
	def remove_lait(B):
		I=B.image_lait.split(T);C=[];G=J
		for F in e(s(I)):
			if Q in F and not G:
				C.append(F.replace(Q,O,1))
				if B.quantite_de_lait<25:B.quantite_de_lait+=1
				G=D
			else:C.append(F)
		B.image_lait=T.join(e(s(C)));H(B.image_lait);H(B.quantite_de_lait);A.show(E(B.image_lait))
	def mode_compteur(C):
		A.show(E(C.image_lait));N(l)
		while not d.is_touched():
			if L.is_pressed()and M.is_pressed():
				if C.quantite_de_lait==0:A.scroll(g)
				else:A.scroll(F(C.quantite_de_lait)+g)
				A.show(E(C.image_lait));K(1000)
				if L.is_pressed()and M.is_pressed():C.image_lait=f;C.quantite_de_lait=0;A.show(E(C.image_lait))
			elif L.is_pressed():
				if N(a):C.add_lait();I(B,n,F(C.quantite_de_lait));N(a)
			elif M.is_pressed():
				if N(V):C.remove_lait();I(B,n,F(C.quantite_de_lait));N(V)
		C.menu()
	def mode_statut(E):
		A.show(Q)
		while not d.is_touched():
			D=S(P.receive(),B)
			if D and D[0]==w:
				A.show(F(D[2]))
				if not C:
					if D[2]==Q:G.play(['c4:1'])
					elif D[2]=='1':G.play(['e4:1'])
					else:G.play(['e5:4'])
		E.menu()
	def mode_temperature(D):
		I(B,R,x)
		while not d.is_touched():
			C=S(P.receive(),B)
			if C:
				if C[0]==y:A.scroll(F(C[2]));break
		D.menu()
	def mode_find(D):
		I(B,R,z)
		while not d.is_touched():
			C=P.receive_full()
			if C:
				C=C[1];H(C)
				if C<-120:A.show(O)
				elif C>-30:A.show(Q)
				else:A.show(abs(C)//10-2)
		I(B,R,A0);D.menu()
	def mode_light(C):
		if C.light:I(B,R,A1);A.show(E.NO);K(1000);A.clear();C.light=J
		else:I(B,R,A2);A.show(E.YES);K(1000);A.clear();C.light=D
		C.menu()
class AC(q):
	def __init__(A,id):super().__init__(id);A.statut=0;A.old_statut=0;A.history=[0,0,0,0,0,0,0,0,0,0];A.playing_music=J;A.quantite_de_lait=0;A.findmode=J;A.show_statut=D;A.main()
	def main(C):
		a='99999:99999:99999:99999:99999';X='PING';U=0
		while D:
			for b in range(10000):
				O=S(P.receive(),B)
				if b%500==0:
					if C.findmode:I(B,X,X)
					W=(h.get_x()+h.get_y()+h.get_z()+A3.sound_level()*100)/4;c=abs((W-U)/100);C.history.append(c);C.history.pop(0);T=sum(C.history)/Z(C.history)
					if T<.8:
						C.statut=0
						if C.show_statut:A.show(Q)
					elif T<3.:
						C.statut=1
						if C.show_statut:A.show('1')
					elif T<4.:
						C.statut=2
						if C.show_statut:A.show('2')
					U=W
				if C.statut!=C.old_statut:I(B,w,F(C.statut));C.old_statut=C.statut
				if M.is_pressed()and C.statut>0:
					if not C.playing_music:G.play(G.PYTHON,wait=J);C.playing_music=D
					else:G.stop();C.playing_music=J
					N(V)
				if L.is_pressed():
					if C.quantite_de_lait==0:A.scroll(g)
					else:A.scroll(F(C.quantite_de_lait)+g)
					if not C.show_statut:A.show(E(a))
				if O:
					if O[0]==R and O[2]==x:K(100);I(B,y,F(o()));H('TEMP: {}'.format(o()))
					if O[0]==R and O[2]==z:C.findmode=D
					if O[0]==R and O[2]==A0:C.findmode=J
					if O[0]==R and O[2]==A2:A.show(E(a));C.show_statut=J
					if O[0]==R and O[2]==A1:A.clear();C.show_statut=D
					if O[0]==n:C.quantite_de_lait=Y(O[2]);H('SETQLAIT: {}'.format(C.quantite_de_lait))
G.play(k)
if not A4:X=A6();A.show(F(X));K(500);A.clear();A8()
else:X=0
r=A7()
if r==b:AD=AB(X)
elif r==c:AD=AC(X)
else:A.scroll('ROLE ERROR')