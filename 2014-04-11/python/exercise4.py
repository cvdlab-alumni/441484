
from importParco import *



def circle (r):
	def circ (p):
		return ([r*COS(p[0]),r*SIN(p[0])])
	return circ

dom = INTERVALS(PI)(6)


# creo e sistemo gli alberi

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



# creo le strisce dei parcheggi

qab = QUOTE([10,-10,10])
qqq =  QUOTE([0.31,-4]*4)
qqq = PROD([qab, qqq]) #  lista generica verticale
qqq = R([1,2])(PI/2)(qqq)  

qqq = T([1,2])([-52,5])(qqq)  
qqq= COLOR(ColorPlasm([0,49,83]))(qqq)


qqq2 = T([1])([137])(qqq) 




# obelisco

baseFont = CYLINDER([10.8, 1])(20)
baseFont = T([1,2])([10,95])(baseFont)  
baseFont= COLOR(ColorPlasm([0,225,255]))(baseFont)


Font = CYLINDER([8.8, 2])(10)
Font = T([1,2])([10,95])(Font)  
Font= COLOR(ColorPlasm([0,127,255]))(Font)


Font1 = CYLINDER([6.8, 4])(5)
Font1 = T([1,2])([10,95])(Font1)
Font1= COLOR(ColorPlasm([255,127,80]))(Font1)


Font2 = CYLINDER([4.8, 40])(4)
Font2 = T([1,2])([10,95])(Font2)  
Font2= COLOR(ColorPlasm([184,134,11]))(Font2)

C3 = CUBOID([6.4,6.4])
p = [3.2,3.2,15]
C3=JOIN([MK(p),C3])

Font3 = R([1,2])(-PI/4)(C3)  
Font3 = T([1,2,3])([5.3,95,37])(Font3)  
Font3= COLOR(ColorPlasm([184,134,11]))(Font3)

Font = STRUCT([Font, Font2, Font1,baseFont, Font3])



# creo un lampione

paloO = CYLINDER([0.3, 15])(100)

paloV = CYLINDER([0.3, 6.1])(100)
paloV=ROTATE([1,3])(-PI/2)(paloV)
paloV=T([1,2,3])([-0.1,0.01,14.6])(paloV)

faro=MAP(circle(0.7))(dom)

aafaro=SOLIDIFY(faro)

aafaro= PROD([aafaro, Q(2)])
aafaro=ROTATE([2,3])(PI/2)(aafaro)
aafaro=ROTATE([1,2])(PI/2)(aafaro)
aafaro=T([1,2,3])([0,0.4,0])(aafaro)

palo3=T([1,2,3])([6,-0.4,14.3])(aafaro)

palo=STRUCT([paloO,paloV,palo3])
palo = COLOR(ColorPlasm([178,178,178]))(palo)

luce= CUBOID([1,0.5,0.2])
luce=T([1,2,3])([6.5,-0.2,14.2])(luce)
luce = COLOR(ColorPlasm([255,255,0]))(luce)

lampione0=STRUCT([palo,luce])
lampione=STRUCT([palo,luce])

lampione=T([1,2])([-55,-45])(lampione)



# ruoto e traslo per sistemarli

T1=T(2)(20)
lampione=STRUCT(NN(2)([T1, lampione]))

lampione2=T([1,2])([-20,35])(lampione)

lampione3=T([1,2])([30,30])(lampione2)


lampione_temp1=ROTATE([1,2])(PI/4)(lampione0)
lampione_temp1=T([1,2])([45,-60])(lampione_temp1)


lampione_temp2=ROTATE([1,2])(-PI/2)(lampione0)
lampione_temp2=T([1,2])([60,70])(lampione_temp2)

T5=T(1)(-20)
lampione_temp2=STRUCT(NN(4)([T5, lampione_temp2]))



lampione_temp3=ROTATE([1,2])(-PI)(lampione0)
lampione_temp3=T([1,2])([75,85])(lampione_temp3)
T4=T(2)(-20)
lampione_temp3=STRUCT(NN(2)([T4, lampione_temp3]))

lampione_temp4=T([1,2])([20,-35])(lampione_temp3)

lampione_temp5=T([1,2])([-30,-30])(lampione_temp4)

lampioni=STRUCT([lampione_temp5, lampione_temp4, lampione_temp3, lampione, lampione2, lampione3, lampione_temp2, lampione_temp1])



# creao il segnale di parcheggio

dom1 = INTERVALS(PI*2)(4)
dom2 = INTERVALS(PI*2)(36)

segnale = MAP(circle(0.05))(dom2)
segnale=T([1,2])([0.25,0.05])(segnale)
segnale=SOLIDIFY(segnale)
segnale= PROD([segnale, Q(4)])


segn=MAP(circle(0.7))(dom1)
segn= PROD([segn, Q(0.1)])

segn=ROTATE([1,2])(PI/4)(segn)
segn=T([1,2])([0.25,0.5])(segn)
segn=ROTATE([2,3])(PI/2)(segn)
segn=T([3])([4])(segn)
segn=T([2])([0.1])(segn)

segn= JOIN(segn)
segn= COLOR(ColorPlasm([0,127,255]))(segn)


obj = PROD([ OFFSET([0.5,0.25])(TEXT("P")) , Q(0.1) ]) 
obj = S([1,2,3])([0.1,0.1,0.1])(obj)
obj=ROTATE([2,3])(PI/2)(obj)
obj=T([1,3])([0.1,4.2])(obj)

segnale = STRUCT([obj, segn, segnale])
segnale=S([1,2,3])([2,2,2])(segnale)
segnale=ROTATE([1,2])(-PI/4)(segnale)
segnale2=ROTATE([1,2])(PI)(segnale)

segnale=T([1,2])([60.5,7])(segnale)

segnale2=T([1,2])([-42.5,33])(segnale2)




#creo la panchina

gamba1 = CUBOID([6,2,3])
gamba2 = T(2)(10)(CUBOID([6,2,3]))
base = T(3)(3)(CUBOID([6,12,1]))
schienale = T(3)(4)(CUBOID([1,12,5]))

panchina = STRUCT([gamba1,gamba2,base,schienale])
panchina1 = T([1,2,3])([-75.5,-21.5,0.5])(panchina)


panchina2 = R([1,2])(PI)(panchina1)
panchina2 = T([1,2])([18.5,-21.5])(panchina2)
panchina3 = T([2])([62.5])(panchina2)



#finale = STRUCT([Font ,panchina3, panchina2, panchina1,segnale2, segnale,lampioni,  qqq2, qqq, baseFont , alberiO, albero121,albero23, albero34, albero, completo])


finale = STRUCT([Font, panchina3, panchina2, panchina1,segnale2, segnale,lampioni,  qqq2, qqq, baseFont , alberiO, albero121,albero23, albero34, albero, completo])

VIEW(finale)


