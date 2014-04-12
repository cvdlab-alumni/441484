
from pyplasm import *
from mapper import *
from myfont import *

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

GRID = COMP([INSR(PROD),AA(QUOTE)])


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



a=PROD([a,Q(0.1)])



FACCIATA=STRUCT([a,aa,qt,houseRowxy,houseRowxyz2, fil,aaa, circ0, CIL,CIL2])



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


circ3 = PROD([CIRC3,Q(3)])



CIRC5=MAP(circle(1.86))(dom)
CIRC5= R([1,2])(-PI/3)(CIRC5)

CIRC5 = T([1,2])([12.7,34])(CIRC5)

circ5 = PROD([CIRC5,Q(3)])



CIRC4=MAP(circle(1.86))(dom)
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



circBIG=MAP(circle(7))(dom)
circBIG=T([1,2])([7.02,30.6])(circBIG)

circBIG=PROD([circBIG,Q(5)])






TORRE = GRID([[3.32],[5.68],[25]])


TORRE=T([1,2])([-3.17,22.82])(TORRE)
TORRE= COLOR(ColorPlasm([0,149,182]))(TORRE)


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
circ2=PROD([circ2,Q(6)])

fl0 = GRID([[28],[40]])
fl0=T([1,2])([-5,-0.55])(fl0)

west = PROD([floor2cont3,Q(6)])

sud = STRUCT([circBIG,circ2, circ5, circ4, circ3])



muretto = POLYLINE([[6.23,30.7],[6.23,27.95], [5.68,27.95],[5.68,30.7],[6.23,30.7]])
muretto = SOLIDIFY(muretto)
muretto = PROD([muretto, Q(6)])
muretto= T(1)(-5.65)(muretto)

mock_up_3D = STRUCT([fl0,nord,east,west,sud, muretto])


mock_up_3D = SKELETON(1)(mock_up_3D)




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
semicerchio= T([1,2,3])([6.95,30.8,5])(semicerchio)

tettoFinale = STRUCT([tetto, tetto2, semicerchio])
tettoFinale = COLOR([1,0.894,0.768])(tettoFinale)


tettoNavataLat = POLYLINE([[26.5,22.33],[25.8,29.2],[21,29.2],[21,22.33],[26.4,22.33]])
tettoNavataLat= SOLIDIFY(tettoNavataLat)
tettoNavataLat = COLOR(ColorPlasm([210,180,140]))(tettoNavataLat)

tettoNavataLat = T([1,2,3])([-7,0,6.1])(tettoNavataLat)


solid_model_3D = STRUCT([tettoNavataLat, mock_up_3D, tettoFinale])


