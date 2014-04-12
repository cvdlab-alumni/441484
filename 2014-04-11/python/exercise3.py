from pyplasm import *
from larcc import *

def ColorPlasm(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

def larSemiDisk(radius=1.):
    def larDisk0(shape=[36,1]):
        domain = larIntervals(shape)([PI,radius])
        V,CV = domain
        x = lambda V : [p[1]*COS(p[0]) for p in V]
        y = lambda V : [p[1]*SIN(p[0]) for p in V]
        return larMap([x,y])(domain)
    return larDisk0



fl1 =  POLYLINE([[6.23,30.4],[6.23,27.95],[2.51,27.95],[2.51,22.27],[6.23,22.27],[6.23,18.48],[5.68,18.48],[5.68,15.95],[5.13,15.95],[5.13,15.4],[5.68,15.4],[5.68,13.42],[5.13,13.42],[5.13,12.87],[5.68,12.87],[5.68,10.89],[5.13,10.89],[5.13,10.34],[5.68,10.34],[5.68,7.81],[5.13,7.81],[5.13,7.26],[5.68,7.26],[5.68,4.73],[5.13,4.73],[5.13,4.18],[5.68,4.18],[5.68,1.1],[5.13,1.1],[5.13,0.55],[5.68,0.55],[5.68,0],[6.23,0],[6.23,0.55],[11.23,0.55],[11.23,0],[15.03,0],[15.03,0.55],[20.03,0.55],[20.03,0],[20.58,0],[20.58,0.55],[21.13,0.55],[21.13,1.1],[20.58,1.1],[20.58,15.95],[21.13,15.95],[21.13,15.4],[20.58,15.4],[20.58,13.42],[21.13,13.42],[21.13,12.87],[20.58,12.87],[20.58,10.89],[21.13,10.89],[21.13,10.34],[20.58,10.34],[20.58,7.81],[21.13,7.81],[21.13,7.26],[20.58,7.26],[20.58,4.73],[21.13,4.73],[21.13,4.18],[20.58,4.18],[20.58,18.48],[21.84,18.48],[21.84,21.78],[26.75,21.78],[26.75,22.33],[26.2,22.33],[25.65,28.37],[25.65,30.41],[26,30.41],[26,30.76],[25.13,30.76],[25.13,29.22],[20.58,29.22],[20.58,30.4]])
GRID = COMP([INSR(PROD),AA(QUOTE)])




def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0



def circle (r):
	def circ (p):
		return ([r*COS(p[0]),r*SIN(p[0])])
	return circ

dom = INTERVALS(PI)(36)

dom2 = INTERVALS(PI)(24)

def ring(r,R):
	def circle (r):
		def c(p):
			return [r*math.cos(p[0]),r*math.sin(p[0])]
		return c
	esterno = MAP(circle(R))(dom)
	interno = MAP(circle(r))(dom)	
	return STRUCT([esterno,interno])

floor2cont =  POLYLINE([[6.78,30.4],[6.23,30.4],[6.23,27.95],[2.51,27.95],[2.51,22.27],[6.23,22.27],[6.23,18.48],[5.68,18.48],[5.68,15.95],[5.13,15.95],[5.13,15.4],[5.68,15.4],[5.68,13.42],[5.13,13.42],[5.13,12.87],[5.68,12.87],[5.68,10.89],[5.13,10.89],[5.13,10.34],[5.68,10.34],[5.68,7.81],[5.13,7.81],[5.13,7.26],[5.68,7.26],[5.68,4.73],[5.13,4.73],[5.13,4.18],[5.68,4.18],[5.68,1.1],[5.13,1.1],[5.13,0.55],[5.68,0.55],[5.68,0],[6.23,0],[6.23,0.55],[11.23,0.55],[11.23,0],[12.23,0],[12.23,0.55],[12.53,0.55],[12.53,1.1],[9.86,1.1],[9.86,1.65],[9.31,1.65],[9.31,1.1],[6.23,1.1],[6.23,4.18],[6.78,4.18],[6.78,4.73],[6.23,4.73],[6.23,7.26],[6.78,7.26],[6.78, 7.81],[6.23,7.81],[6.23,10.34],[6.78,10.34],[6.78,10.89],[6.23,10.89],[6.23,15.35],[6.78,15.35],[6.78,15.9],[6.23,15.9],[6.23,17.86],[6.78,17.86],[6.78,24.67],[6.23,24.67],[6.23,24.12],[5.68,24.12],[5.68,23.28],[4.28,23.28],[4.28,24.12],[3.73,24.12],[3.73,24.67],[3,24.67],[3,26.07],[3.73,26.07], [3.73,26.62],[4.28,26.62],[4.28,27.2],[5.68,27.2], [5.68, 26.62],[6.23,26.62],[6.23,26.07], [6.78,26.07],[6.78,30.4]])

floor2cont2 =  POLYLINE([[14.03,0],[14.03,0.55],[13.73,0.55],[13.73,1.1],[16.43,1.1],[16.43,1.65],[16.95,1.65],[16.95,1.1],[19.95,1.1],[19.95,4.18],[19.4,4.18],[19.4,4.73],[19.95,4.73],[19.95,7.26],[19.4,7.26],[19.4,7.81],[19.95,7.81],[19.95,10.34],[19.4,10.34],[19.4,10.89],[19.95,10.89],[19.95,15.4],[19.4,15.4],[19.4,15.95],[19.95,15.95],[19.95,18.4],[19.4,18.4],[19.4,25.56],[19.95,25.56],[19.95,22.4],[25.21,22.4],[24.66,28.44],[24.11,28.44],[24.11,29.22],[25,29.22]])
floor2cont3 =  POLYLINE([[14.03,0],[15.03,0],[15.03,0.55],[20.03,0.55],[20.03,0],[20.58,0],[20.58,0.55],[21.13,0.55],[21.13,1.1],[20.58,1.1],[20.58,15.95],[21.13,15.95],[21.13,15.4],[20.58,15.4],[20.58,13.42],[21.13,13.42],[21.13,12.87],[20.58,12.87],[20.58,10.89],[21.13,10.89],[21.13,10.34],[20.58,10.34],[20.58,7.81],[21.13,7.81],[21.13,7.26],[20.58,7.26],[20.58,4.73],[21.13,4.73],[21.13,4.18],[20.58,4.18],[20.58,18.48],[21.84,18.48],[21.84,21.78],[26.75,21.78],[26.75,22.33],[26.2,22.33],[25.65,28.37],[25.65,30.41],[26,30.41],[26,30.76],[25.13,30.76],[25.13,29.22]])



floor2cont4 = POLYLINE([[22.1,29.22],[22.1,28.44],[21.2,28.44],[21.2,27.89],[19.95,27.89],[19.95,27.34],[19.4,27.34],[19.4,27.89],[18.85,27.89],[18.85,28.44],[19.4,28.44],[19.4,30.7]])
floor2cont5 = POLYLINE([[22.1,29.22],[20,29.22],[20,30.7],[19.4,30.7]])



circ1 = SOLIDIFY(ring(6.3,6.9))  # SEMICERCHIO GRANDE STRUTTURA
circ1=T([1,2])([13.1,30.4])(circ1)

CIRC1=MAP(circle(6.9))(dom2)
CIRC1=T([1,2])([13.1,30.4])(CIRC1)



floor2cont3 = (STRUCT([floor2cont2,floor2cont3,floor2cont5,floor2cont4]))

floor2cont3=SOLIDIFY(floor2cont3)


q =QUOTE([3])
qq=QUOTE([1, -1.8, 1])
aa= PROD([qq,q])
a =  POLYLINE([[0.55,0],[0.55,6],[3.55,7],[3.55,9],[7.45,10],[11.35,9],[11.35,7],[14.35,6],[14.35,0],[0.55,0]])
aaa=POLYLINE([[0.55,0],[14.9,0]])
aa= T(1)(5.55)(aa)

qt= T([1, 2])([5.55,3])(q)
qs=R([1,2])(PI/2)(q)
pair_xy = [T(2)(-1), qt]
houseRowxy = STRUCT(NN(1)(pair_xy))



def circle (r):
	def circ (p):
		return ([r*COS(p[0]),r*SIN(p[0])])
	return circ

dom = INTERVALS(PI)(36)

dom2 = INTERVALS(2*PI)(36)


circ0=MAP(circle(0.9))(dom)

circ0=T([1,2])([7.45,2])(circ0)
circ0=PROD([circ0,Q(0.4)])
ak =  POLYLINE([[0,3],[0.55,3]])
ka =  POLYLINE([[1.1,3],[0.55,3]])

pair_xyz = [T(1)(1.1), qs]
pair_xyz1 = [T(1)(0.6), qs]

houseRowxyz = STRUCT(NN(1)(pair_xyz))

houseRowxyz1 = STRUCT(NN(2)(pair_xyz1))
houseRowxyz1 = T(1)(1.4)(houseRowxyz1)


pair_xyz2 = [T(1)(8), houseRowxyz1]



houseRowxyz2 = STRUCT(NN(2)(pair_xyz2))
houseRowxyz2 = T(1)(-6.8)(houseRowxyz2)

pil= STRUCT([qs,houseRowxyz,ak])
bil= STRUCT([qs,houseRowxyz,ka])
bil = T(1)(13.85)(bil)
fil= STRUCT([bil,pil])

CIL = CYLINDER([0.15,2])(32)
CIL=R([2,3])(-PI/2)(CIL)
CIL2=T(1)(6.65)(CIL)
CIL=T(1)(1.6)(CIL2)
aa=PROD([aa,Q(.3)])


a=SOLIDIFY(a)


fin=GRID([[0.4],[2]])

finc=MAP(circle(0.2))(dom)
finc=JOIN(finc)
finc=T([1,2])([0.2,2])(finc)
finc=STRUCT([fin,finc])
finc=T([1,2])([7.5,6])(finc)


porta=GRID([[1.8],[2]])
porta=T([1,2])([6.55,0])(porta)



a = DIFFERENCE([a, finc, porta])


a=PROD([a,Q(0.1)])


FACCIATA = STRUCT([a,aa,qt,houseRowxy,houseRowxyz2, fil,aaa, circ0, CIL,CIL2])


CRO= QUOTE([0.8])
CRO=R([2,1])(PI/2)(CRO)
CROL= QUOTE([0.4])

 

latS=QUOTE([0.55,-3.08])
latSc=QUOTE([0.55,-2.53]*5)
latSc=T(1)(3.63)(latSc)

LATO = STRUCT([latS,latSc])
LATO=PROD([LATO,Q(0.55)])
LATO=PROD([LATO,Q(3)])

LATO= R([1,2])(PI/2)(LATO)
LATO= T(1)(-0.55)(LATO)


MURO = GRID([[19.03],[-0.55,0.55],[6]])

MURO= R([1,2])(PI/2)(MURO)
MURO= T(1)(0.55)(MURO)


CIRC3=MAP(circle(1.86))(dom)
CIRC3 = T([1,2])([7.6,36.9])(CIRC3)


CIRC3=MAP(circle(1.86))(dom)

CIRC3 = T([1,2])([7.6,36.9])(CIRC3)
CIRC3=JOIN(CIRC3)


circ3 = PROD([CIRC3,Q(3)])



CIRC5=MAP(circle(1.86))(dom)
CIRC5=JOIN(CIRC5)

CIRC5= R([1,2])(-PI/3)(CIRC5)

CIRC5 = T([1,2])([12.7,34])(CIRC5)

circ5 = PROD([CIRC5,Q(3)])



CIRC4=MAP(circle(1.86))(dom)
CIRC4=JOIN(CIRC4)

CIRC4= R([1,2])(PI/3)(CIRC4)
CIRC4 = T([1,2])([1.9,34])(CIRC4)

circ4 = PROD([CIRC4,Q(3)])





MURO2 = GRID([[0.55],[3.79],[6]])

MURO2 = T([2])([19.03])(MURO2)



MURO3= GRID([[3.79],[0.1],[6]])
MURO3 = T([1,2])([-3.17,22.82])(MURO3)



MURO4 = GRID([[0.1],[5.68],[6]])
MURO4 = T([1,2])([-3.17,22.82])(MURO4)



MURETTO = GRID([[0.1],[2],[6]])
MURETTO = T([1,2])([0.55,28.6])(MURETTO)


MURODXO= GRID([[0.1],[2],[6]])




circBIG=MAP(circle(6.9))(dom)
circBIG=T([1,2])([7.42,30.4])(circBIG)

circBIG=PROD([circBIG,Q(5)])

TORRE = GRID([[3.72],[5.68],[25]])

TORRE=T([1,2])([-3.17,22.82])(TORRE)


floor2cont2 =  POLYLINE([[19.95,0.55],[19.95,4.18],[19.4,4.18],[19.4,4.73],[19.95,4.73],[19.95,7.26],[19.4,7.26],[19.4,7.81],[19.95,7.81],[19.95,10.34],[19.4,10.34],[19.4,10.89],[19.95,10.89],[19.95,15.4],[19.4,15.4],[19.4,15.95],[19.95,15.95],[19.95,18.4],[19.4,18.4],[19.4,25.56],[19.95,25.56],[19.95,22.4],[25.21,22.4],[24.66,28.44],[24.11,28.44],[24.11,29.22],[25,29.22]])
floor2cont3 =  POLYLINE([[19.95,0.55],[19.95,0],[20.58,0],[20.58,0.55],[21.13,0.55],[21.13,1.1],[20.58,1.1],[20.58,15.95],[21.13,15.95],[21.13,15.4],[20.58,15.4],[20.58,13.42],[21.13,13.42],[21.13,12.87],[20.58,12.87],[20.58,10.89],[21.13,10.89],[21.13,10.34],[20.58,10.34],[20.58,7.81],[21.13,7.81],[21.13,7.26],[20.58,7.26],[20.58,4.73],[21.13,4.73],[21.13,4.18],[20.58,4.18],[20.58,18.48],[21.84,18.48],[21.84,21.78],[26.75,21.78],[26.75,22.33],[26.2,22.33],[25.65,28.37],[25.65,30.41],[26,30.41],[26,30.76],[25.13,30.76],[25.13,29.22]])


floor2cont4 = POLYLINE([[22.1,29.22],[22.1,28.44],[21.2,28.44],[21.2,27.89],[19.95,27.89],[19.95,27.34],[19.4,27.34],[19.4,27.89],[18.85,27.89],[18.85,28.44],[19.4,28.44],[19.4,30.7]])
floor2cont5 = POLYLINE([[22.1,29.22],[20,29.22],[20,30.7],[19.4,30.7]])


floor2cont3 = (STRUCT([floor2cont2,floor2cont3,floor2cont5,floor2cont4]))

floor2cont3=SOLIDIFY(floor2cont3)

floor2cont3=T(1)(-5.8)(floor2cont3)

east = STRUCT([LATO, MURO,MURO2, MURO3,MURO4, T(2)(5.68)(MURO3),MURETTO,TORRE])

FACCIATA=R([2,3])(PI/2)(FACCIATA)



nord=T(1)(-0.4)(FACCIATA)

CIRC2=MAP(circle(1.97))(dom)

circ2 = T([1,2])([17.1,29.22])(CIRC2)
circ2= JOIN(circ2)
circ2=PROD([circ2,Q(6)])

fl0 = GRID([[28],[40]])
fl0=T([1,2])([-5,-0.55])(fl0)

west = PROD([floor2cont3,Q(6)])

sud = STRUCT([circBIG,circ2, circ5, circ4, circ3])

sud= T(1)(-0.4)(sud)





muretto = POLYLINE([[6.23,30.7],[6.23,27.95], [5.68,27.95],[5.68,30.7],[6.23,30.7]])
muretto = SOLIDIFY(muretto)
muretto = PROD([muretto, Q(6)])
muretto= T(1)(-5.65)(muretto)



TORRE= COLOR(ColorPlasm([0,149,182]))(TORRE)



facciateLaterali = STRUCT([nord ,east,west,sud, muretto])

facciateLaterali = COLOR(ColorPlasm([0, 51,153]))(facciateLaterali)

mock_up_3D = STRUCT([fl0, facciateLaterali, TORRE])





ttt = POLYLINE([[0.55,6],[3.55,7],[3.55,9],[7.45,10],[11.35,9],[11.35,7],[14.35,6]])
ttt=PROD([ttt,Q(30.8)])

tetto= R([2,3])(PI/2)(ttt)
tetto= T(2)(30.8)(tetto)

tetto= T(1)(-0.4)(tetto)

ttt2 = POLYLINE([[0.55,5],[0.55,6],[3.55,7],[3.55,9],[7.45,10],[11.35,9],[11.35,7],[14.35,6],[14.35,5]])
ttt2=SOLIDIFY(ttt2)

tetto2= R([2,3])(PI/2)(ttt2)
tetto2= T(2)(30.8)(tetto2)

tetto2= T(1)(-0.4)(tetto2)

model = checkModel(larSemiDisk(6.9)([36,4]))
semicerchio = STRUCT(MKPOLS(model))
semicerchio= T([1,2,3])([7,30.4,5])(semicerchio)


tettoFinale = STRUCT([tetto, tetto2, semicerchio])
tettoFinale = COLOR(ColorPlasm([210,180,140]))(tettoFinale)



solid_model_3D = STRUCT([mock_up_3D, tettoFinale])


solid_model_3D = S([1,2,3])([2,2,2])(solid_model_3D)
solid_model_3D = T([1,2])([-4,-30])(solid_model_3D)




prato = CUBOID([180,180])
prato= T([1,2])([-80,-70])(prato)

prato = COLOR([0.482,0.627,0.356])(prato)


parc1 = GRID([[30],[40]])
parc1=T([1,2])([-5,60])(parc1)

# fare le strisce dei parcheggi ...verranno copiate nel secondo parcheggio



pair_x = [T(2)(-120), parc1]
parc2 = STRUCT(NN(1)(pair_x))



palazzo1 =GRID([[20],[40],[40]])


basePalazzo1 =GRID([[30],[50],[0]])
basePalazzo1 = T([1,2])([-5,-5])(basePalazzo1)
basePalazzo1= COLOR(ColorPlasm([61,43,31]))(basePalazzo1)
finestra1 = GRID([[3],[0],[6]])
finestra1 = T([1,3])([3.5,30])(finestra1)


pair_y = [T(1)(10), finestra1]
finestra2 = STRUCT(NN(1)(pair_y))


finestra12 = STRUCT([finestra1, finestra2])
finestra12= COLOR([0.501,0,0])(finestra12)

pair_y = [T(3)(-10), finestra12]
finestre = STRUCT(NN(2)(pair_y))

finestre = STRUCT([finestre, finestra12])
finestre= COLOR([0.501,0,0])(finestre)


pair_yz = [T(2)(40), finestre]
finestreAltroLato = STRUCT(NN(1)(pair_yz))

pair_xz = R([1,3])(PI/2)(finestre)

pair_xz = [T(1)(60), pair_xz]

finestreLatoLungo = STRUCT(NN(1)(pair_xz))
finestreLatoLungo = R([1,2])(PI/2)(finestreLatoLungo)

finestreLatoLungo = T([2,3])([-16,17])(finestreLatoLungo)


pair_yy = [T(1)(20), finestreLatoLungo]
finestreLatoLungo2 = STRUCT(NN(1)(pair_yy))

finestre = STRUCT([finestre, finestra12, finestreLatoLungo, finestreLatoLungo2, finestreAltroLato])


porta1 =GRID([[7],[0],[9]])
porta1 = R([1,2])(PI/2)(porta1)

porta1 = T(1)(20)(porta1)
porta1 = T(2)(17)(porta1)



palazzo1 = STRUCT([palazzo1, finestre, porta1, basePalazzo1])
palazzo1 = T([1,2])([-70,55])(palazzo1)



viale3 = CUBOID([10,70]) # ok
viale3 = T([1,2])([-40,10])(viale3)


viale4 = CUBOID([20,10])
viale4 = T([1,2])([-55,70])(viale4)

palazzo11 = STRUCT([palazzo1, viale3, viale4])



palazzo2 = R([1,2])(PI)(palazzo1)
palazzo2 = STRUCT([T([1,2])([20,30]), palazzo2]) ## questo  utilizzato per fare il palazzo 3e 4

palazzo22 = R([1,2])(PI)(palazzo11)
palazzo22 = STRUCT([T([1,2])([20,30]), palazzo22]) 

palazzi12 = STRUCT([palazzo11, palazzo22])

viale1 = CUBOID([10,60])
viale1 = T([1,2])([-50,-50])(viale1)


palazzo3 = R([1,2])(-PI/2)(palazzo2)
palazzo3 = T([1,2])([0,30])(palazzo3)
palazzo3 = STRUCT([palazzo3, viale1])
palazzo4 = R([1,2])(PI)(palazzo3)
palazzo4 = T([1,2])([20,40])(palazzo4)



parcheggi = STRUCT([parc2, parc1])
parcheggi = R([1,2])(PI/2)(parcheggi)
parcheggi = T([1,2])([30,10])(parcheggi)



viale2 = CUBOID([90,10])
viale2 = T([1,2])([-35,10])(viale2)


viale5 = CUBOID([100,10]) # ok
viale5 = T([1,2])([-35,58])(viale5)



viale6 = CUBOID([10,30]) # ok
viale6 = T([1,2])([50,-70])(viale6)




completo = STRUCT([solid_model_3D, prato, parcheggi, palazzi12, palazzo3, palazzo4, viale5, viale6])


VIEW(completo)