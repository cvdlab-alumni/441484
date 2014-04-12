from importEs2 import *


b = QUOTE([0.55,-2.53]*4)
c = QUOTE([0.55, -6.67, 0.55])
aaa=PROD([b,c])
aaa=R([1,2])(PI/2)(aaa)
aaa=T([1,2])([17,1.1])(aaa)

aa=QUOTE([0.55])
bb=QUOTE([1.65, -5.57, 1.65])

bbb = T([1])(0.55)(PROD([aa,bb]))
cc=QUOTE([1.65])

ccc=T([2])(0.55)(PROD([cc,c]))
x = STRUCT([ccc, bbb])

x = R([1,2])(-PI/2)(x)

x = T([1,2])([8.56,14])(x)  # croce completa


pair_x = [T(2)(10.68), x]
houseRow = STRUCT(NN(1)(pair_x))

pair_x2 = [T(2)(13.77), x]

houseRow2 = STRUCT(NN(1)(pair_x2))



tresopra = QUOTE([0.55,-1.68]*3)
tresopra=PROD([tresopra,c])
tresopra=R([1,2])(PI/2)(tresopra)
tresopra=T([1,2])([17,16])(tresopra)

zzz = PROD([aa,c])
zzz= R([1,2])(-PI/2)(zzz)
zzz= T([1,2])([8.9,31])(zzz)




z1 = PROD([aa,aa])
z1= R([1,2])(-PI/4)(z1)


pair_xx = [T(1)(5), z1]
houseRowxx = STRUCT(NN(2)(pair_xx))
houseRowxx= T([1,2])([5,33.3])(houseRowxx)

z2 = PROD([aa,aa])
pair_xy = [T(1)(2), z2]
houseRowxy = STRUCT(NN(2)(pair_xy))
houseRowxy= T([1,2])([9.7,34.7])(houseRowxy)



internoA= STRUCT([x, aaa, tresopra,houseRow])
internoA=PROD([internoA,Q(6)])

internoB=STRUCT([houseRow2, zzz, houseRowxx, houseRowxy])


internoB=PROD([internoB,Q(5)])


interno= STRUCT([internoA,internoB])


fl0B=interno
fl0B= T([1])([-4.7])(fl0B)
fl0B= COLOR(ColorPlasm([150, 0, 24]))(fl0B)




muretto = POLYLINE([[6.23,30.7],[6.23,27.95], [5.68,27.95],[5.68,30.7],[6.23,30.7]])
muretto = SOLIDIFY(muretto)
muretto = PROD([muretto, Q(6)])
muretto= T(1)(-5.65)(muretto)



TORRE= COLOR(ColorPlasm([0,149,182]))(TORRE)



facciateLaterali = STRUCT([nord ,east,west,sud, muretto])

facciateLaterali = COLOR(ColorPlasm([0, 51,153]))(facciateLaterali)



mock_up_3D = STRUCT([fl0, facciateLaterali, TORRE, fl0B])





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
semicerchio= T([1,2,3])([7,30.6,5])(semicerchio)


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
parc1 = COLOR(ColorPlasm([112,128,144]))(parc1)

# fare le strisce dei parcheggi ...verranno copiate nel secondo parcheggio



pair_x = [T(2)(-120), parc1]
parc2 = STRUCT(NN(1)(pair_x))
parc2 = COLOR(ColorPlasm([112,128,144]))(parc2)



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
viale3 = COLOR(ColorPlasm([112,128,144]))(viale3)


viale4 = CUBOID([20,10])
viale4 = T([1,2])([-55,70])(viale4)
viale4 = COLOR(ColorPlasm([112,128,144]))(viale4)

palazzo11 = STRUCT([palazzo1, viale3, viale4])



palazzo2 = R([1,2])(PI)(palazzo1)
palazzo2 = STRUCT([T([1,2])([20,30]), palazzo2]) ## questo  utilizzato per fare il palazzo 3e 4

palazzo22 = R([1,2])(PI)(palazzo11)
palazzo22 = STRUCT([T([1,2])([20,30]), palazzo22]) 

palazzi12 = STRUCT([palazzo11, palazzo22])

viale1 = CUBOID([10,60])
viale1 = T([1,2])([-50,-50])(viale1)
viale1 = COLOR(ColorPlasm([112,128,144]))(viale1)


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
viale2 = COLOR(ColorPlasm([112,128,144]))(viale2)


viale5 = CUBOID([100,10]) # ok
viale5 = T([1,2])([-35,58])(viale5)
viale5 = COLOR(ColorPlasm([112,128,144]))(viale5)



viale6 = CUBOID([10,30]) # ok
viale6 = T([1,2])([50,-70])(viale6)
viale6 = COLOR(ColorPlasm([112,128,144]))(viale6)


tettoNavataLat = POLYLINE([[26.2,22.33],[25.65,28.37],[21.13,28.37],[21.14,22.33],[26.2,22.33]])
tettoNavataLat= SOLIDIFY(tettoNavataLat)
tettoNavataLat = S([1,2,3])([2.4,2.4,2.4])(tettoNavataLat)
tettoNavataLat = COLOR(ColorPlasm([210,180,140]))(tettoNavataLat)

tettoNavataLat = T([1,2,3])([-28,-39.7,12.1])(tettoNavataLat)

completo = STRUCT([tettoNavataLat,solid_model_3D, prato, parcheggi, palazzi12, palazzo3, palazzo4, viale5, viale6])

