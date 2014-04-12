
from importParco import *

tronco = CYLINDER([0.7, 5])(50)
tronco = COLOR(ColorPlasm([101, 67, 33]))(tronco)
foglie = SPHERE(3)([80,80])
foglie = COLOR(ColorPlasm([85,104,50]))(foglie)
foglie = T(3)(6)(foglie)

albero= STRUCT([tronco,foglie])


albero0 = T([1,2])([45,15])(albero)

albero = [T(2)(-10), albero0]
albero = STRUCT(NN(4)(albero)) # prima lista

albero1 = STRUCT([T([1,2])([-50,-35]), albero0])
albero1 = [T(2)(10), albero1]

albero12 = STRUCT(NN(3)(albero1)) # seconda lista
albero121 = T(1)(-60)(albero)

alberoO = [T(1)(-10), albero0]


alberiVert = STRUCT(NN(1)(albero1)) #  lista generica verticale
alberiOrizz = STRUCT(NN(1)(alberoO)) #  lista generica Orizzontale


albero23 = T([1,2])([50,35])(albero12) #ok


albero34 = T([1,2])([-10,35])(albero12) #ok


alberiOrizz1 = STRUCT(NN(5)(alberoO)) #  lista generica Orizzontale

alberiO = T([1,2])([1,40])(alberiOrizz1)  # dietro abbazia


alberiVert1 = STRUCT(NN(2)(albero1)) #  lista generica verticale



baseFont = CYLINDER([10.8, 1])(20)
baseFont = T([1,2])([10,95])(baseFont)  

qab = QUOTE([10,-10,10])
qqq =  QUOTE([0.31,-4]*4)
qqq = PROD([qab, qqq]) #  lista generica verticale
qqq = R([1,2])(PI/2)(qqq)  

qqq = T([1,2])([-52,5])(qqq)  
qqq= COLOR(ColorPlasm([0,49,83]))(qqq)


qqq2 = T([1])([137])(qqq) 



completo = STRUCT([qqq2, qqq, baseFont , alberiO, albero121,albero23, albero34, albero, completo])
#solid_model_3D, prato, parcheggi, palazzi12, viale1, palazzo3, palazzo4, viale2, viale5
VIEW(completo)