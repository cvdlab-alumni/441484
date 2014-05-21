
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, '/Users/Amirs/Desktop/grafica computazionale/lar-cc/lib/py')


from importEs1 import *


dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])

def bezierS1(controlpoints):
   return BEZIER(S1)(controlpoints)

def bezierS2(f):
   return BEZIER(S2)(f)

def bezierMappata_1D(controlpoints):
   return MAP(bezierS1(controlpoints))(INTERVALS(1)(32))


def bezierMappata_2D(functions):
   return MAP(BEZIER(S2)(functions))(dom2D)

def spiralStair(width=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
   V,CV = larSolidHelicoid(width,R,r,pitch,nturns,steps)()
   W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
      for k,v in enumerate(V[:-4]) if k%4==0])
   for k,w in enumerate(W[:-12]):
      if k%6==0:
         W[k+1][2] = W[k+10][2]; W[k+3][2] = W[k+11][2]
         nsteps = len(W)/12
         CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8]) for k in range(nsteps)]
         return W,CW

def ColorPlasm(color):
    return [color[0]/255., color[1]/255., color[2]/255.]






def VIEW_MODEL(master):
   hpc = SKEL_1(STRUCT(MKPOLS(master)))
   hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
   VIEW(hpc)




def REMOVE_CELL(master):
   def REMOVE_CELL0(scelta=[]):
      if len(scelta) == 0:
         v=True
         while v == True:
            i = input("Enter a number: (scrivere -1 per uscire) ")
            if(i < 0):
               v=False
            scelta.append(i)
      master1 = master[0], [cell for k,cell in enumerate(master[1]) if not (k in scelta)] 
      return master1
   return REMOVE_CELL0

#master = REMOVE_CELL(master)([94,92,90,87,85,83])
diagram=master




angle = PI/2; axis = UNITVECT([0,0,1])
a,b,c = SCALARVECTPROD([ angle, axis ])
diagram1 = larApply(r(a,b,c))(diagram)
# primo quadrante

angle = PI; axis = UNITVECT([0,0,1])
a,b,c = SCALARVECTPROD([ angle, axis ])
diagram4 = larApply(r(a,b,c))(diagram1)
# 3 quadrante



angle = 0; axis = UNITVECT([0,0,1])
a,b,c = SCALARVECTPROD([ angle, axis ])
diagram3 = larApply(r(a,b,c))(master2)

angle = PI; axis = UNITVECT([0,0,-1])
a,b,c = SCALARVECTPROD([ angle, axis ])
diagram2 = larApply(r(a,b,c))(checkModel(master3))
#



#angle = PI; axis = UNITVECT([0,0,1])
#a,b,c = SCALARVECTPROD([ angle, axis ])
#diagram3 = larApply(r(a,b,c))(diagram2)

master = assemblyDiagramInit([3,3,8])([[27.5,7,27.5],[18,8,18],[1.8,10.5,1.8,10.5,1.8,10.5,1.8,10.5]])

V,CV = master

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

master = REMOVE_CELL(master)([39,38,37,36,35,34,33])


d3 = assemblyDiagramInit([2,3,2])([[26.5,1],[1,4,3],[8,2.5]])

master = diagram2cell(d3,master,50) 

master = REMOVE_CELL(master)([72])
master = REMOVE_CELL(master)([66])










d1 = assemblyDiagramInit([1,4,1])([[7],[.3,4,.3,13.7],[10.5]])
d2 = assemblyDiagramInit([1,4,1])([[7],[.3,4,.3,13.7],[.3]])

master = diagram2cell(d1,master,31) 

master = diagram2cell(d2,master,30) 
master = diagram2cell(d1,master,29) 
master = diagram2cell(d2,master,28) 
master = diagram2cell(d1,master,27) 
master = diagram2cell(d2,master,26) 
master = diagram2cell(d1,master,25) 





master = REMOVE_CELL(master)([70,78,86,94,33,31,29,27])
master = REMOVE_CELL(master)([64,67,74,78,81,85])



# adesso la cella 74 rappresenta l'ascensore al fermo al terzo piano
# 88 e' la porta, da rendere trasparente
# 33,35,37,39 vanno messe in una catena e rese trasparenti



#VIEW_MODEL(master)

diagram22 = assemblyDiagramInit([1,2,1])([[7],[15,3],[.3]])
master = diagram2cell(diagram22,master,78) 
master = diagram2cell(diagram22,master,73) 
master = diagram2cell(diagram22,master,67) 


diagram11 = assemblyDiagramInit([1,2,1])([[7],[3,15],[.3]])
master = diagram2cell(diagram11,master,29) 
master = diagram2cell(diagram11,master,28) 
master = diagram2cell(diagram11,master,27) 


master = REMOVE_CELL(master)([81,80,83,78,85,76])





master = diagram2cell(diagram4,master,49) 

master = diagram2cell(diagram4,master,47) 
master = diagram2cell(diagram4,master,45) 
master = diagram2cell(diagram4,master,43) 


master = diagram2cell(diagram3,master,34) 
master = diagram2cell(diagram3,master,32) 
master = diagram2cell(diagram3,master,30) 
master = diagram2cell(diagram3,master,28) 



master = diagram2cell(diagram2,master,23) 
master = diagram2cell(diagram2,master,21) 
master = diagram2cell(diagram2,master,19) 
master = diagram2cell(diagram2,master,17) 

master = diagram2cell(diagram1,master,7) 
master = diagram2cell(diagram1,master,5) 
master = diagram2cell(diagram1,master,3) 
master = diagram2cell(diagram1,master,1) 





#master = REMOVE_CELL(master)([73,71,69,67])






hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#VIEW(hpc)


#VIEW_MODEL(master)


#VIEW(struttura)




struttura = STRUCT(MKPOLS(master))

# curve


m1r = [[0, 0,0], [4.55, -6.26,0], [10, -9.39,0], [14,0,0]]
r1 = BEZIER(S1)(m1r)






m1r = [[0, 0,0], [14,0,0]]
r2 = BEZIER(S1)(m1r)


r1 = bezierMappata_2D([r1,r2])

m1r = [[0, 0,0.5], [14,0,0.5]]
r2 = BEZIER(S1)(m1r)

i2 = [[0, 0,0.5], [4.55, -6.26,0.5], [10, -9.39,0.5], [14,0,0.5]]
r22 = BEZIER(S1)(i2)

r2 = bezierMappata_2D([r22,r2])

r2=STRUCT([r2,r1])




i2 = [[0, 0,0.5], [4.55, -6.26,0.5], [10, -9.39,0.5], [14,0,0.5]]
r11 = BEZIER(S1)(i2)

m1r = [[0, 0,0], [4.55, -6.26,0], [10, -9.39,0], [14,0,0]]
r22 = BEZIER(S1)(m1r)

r3 = bezierMappata_2D([r22,r11])

r2=STRUCT([r2,r3])








a = [[0, 0,0], [14,0,0]]
aa = BEZIER(S1)(a)

b = [[0, 0,0.5], [14,0,0.5]]
bb = BEZIER(S1)(b)


r3 = bezierMappata_2D([aa,bb])

r2=STRUCT([r2,r3])
giardino1 = COLOR(ColorPlasm([23,114,69]))(r2)














m1r = [[25, 10,0],[10,5,0],[16, 0,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0],[38, -30.26,0],[38, -30.26,0], [45, -2.39,0], [55,-40,0],[60,0,0],[56,10,0]]
r1 = BEZIER(S1)(m1r)
m1r = [[25, 0,0], [45,0,0]]
r2 = BEZIER(S1)(m1r)
r1 = bezierMappata_2D([r1,r2])
m1r = [[25, 0,0.5], [45,0,0.5]]
r2 = BEZIER(S1)(m1r)
i2 = [[25, 10,0.5],[10,5,0.5],[16, 0,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [38, -30.26,0.5], [45, -2.39,0.5], [55,-40,0.5],[60,0,0.5],[56,10,0.5]]
r22 = BEZIER(S1)(i2)
r2 = bezierMappata_2D([r22,r2])
r2=STRUCT([r2,r1])
r11 = BEZIER(S1)(i2)
m1r = [[25, 10,0],[10,5,0],[16, 0,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0], [38, -30.26,0],[38, -30.26,0],[38, -30.26,0], [45, -2.39,0], [55,-40,0],[60,0,0],[56,10,0]]
r22 = BEZIER(S1)(m1r)
r3 = bezierMappata_2D([r22,r11])
r2=STRUCT([r2,r3])
a = [[25, 0,0], [45,0,0]]
aa = BEZIER(S1)(a)
b = [[25, 0,0.5], [45,0,0.5]]
bb = BEZIER(S1)(b)
r3 = bezierMappata_2D([aa,bb])
giardino2=STRUCT([r2,r3])



#giardino2 = R([1,2])(PI/2)(giardino2)

#giardino2 = T([1,2])([60,-20])(giardino2)



giardino2 = COLOR(ColorPlasm([23,114,69]))(giardino2)
struttura = COLOR(ColorPlasm([255,204,153]))(struttura)




piccolosopra = [[0, 5,0.5], [-20, 18,0.5], [0,31,0.5]]
piccolosopra = BEZIER(S1)(piccolosopra)

piccolosotto = [[0, 5,0], [-20, 18,0], [0,31,0]]
piccolosotto = BEZIER(S1)(piccolosotto)


r1 = bezierMappata_2D([piccolosotto,piccolosopra])





grandesopra = [[0, 0,0.5], [-25, 18,0.5], [0,36,0.5]]
grandesopra = BEZIER(S1)(grandesopra)

grandesotto = [[0, 0,0], [-25, 18,0], [0,36,0]]
grandesotto = BEZIER(S1)(grandesotto)


r2 = bezierMappata_2D([grandesotto,grandesotto])


r3 = bezierMappata_2D([grandesotto,piccolosotto])


r4 = bezierMappata_2D([grandesopra,piccolosopra])



giardino3=STRUCT([r1,r2,r3,r4])





grandesopra2 = [[0, 0,40], [-25, 18,40], [0,36,40]]

grandesopra2 = BEZIER(S1)(grandesopra2)

#giardino4 = T([3])([41])(giardino3)

r5 = bezierMappata_2D([grandesopra2,grandesotto])


giardino3=STRUCT([giardino3,r5])






piccolosopra2 = [[0, 5,40], [-20, 18,40], [0,31,40]]

piccolosopra2 = BEZIER(S1)(piccolosopra2)

#giardino4 = T([3])([41])(giardino3)

r5 = bezierMappata_2D([piccolosotto,piccolosopra2])

giardino3=STRUCT([giardino3,r5])



r5 = bezierMappata_2D([grandesopra2,piccolosopra2])

giardino3=STRUCT([giardino3,r5])

giardino3 = COLOR(ColorPlasm([23,114,69]))(giardino3)
glass = [0.1,0.2,0.47,1,  0,0,0,0.48,  2,2,2,1, 0,0,0,1, 50]

giardino3 = MATERIAL(glass)(giardino3)

giardino3 = T([2])([4.5])(giardino3)



# scala esterna d'emergenza


a=STRUCT(MKPOLS(spiralStair(0.7,3.3,1.5,.3,8.2,3, 20)))
c=CUBOID([1.8,3.9,0.5])
c = T([1,2])([1.3,-4])(c)


#sostituire cuboid con larGRID





c2=CUBOID([1.8,3.9,0.5])
c2 = T([1,2,3])([-3.3,-3.8,12.2])(c2)

a = STRUCT([a,c,c2])


scala = T([1,2])([31.3,40])(a)


scala2 = T(3)(12.2)(scala)
scala3 = T(3)(12.2)(scala2)


scala = STRUCT([scala,scala2,scala3])
scala = T(2)(8)(scala)

scala = T(3)(1.5)(scala)
scala = COLOR(ColorPlasm([128,128,128]))(scala)

GRID = COMP([INSR(PROD),AA(QUOTE)])


#scala = MATERIAL([1,1,1,0.1, 0,0,0.8,0.5, 1,1,1,0.1, 1,1,1,0.1, 100])(scala)



gradino = CUBOID([2.8,0.3,0.3])
scalaint1 = STRUCT( CAT(N(35)([gradino, T([2,3])([0.2,0.4])])))
#scala1 = R([1,2])(PI/2)(scala1)
scalaint20 = STRUCT( CAT(N(41)([gradino, T([2,3])([0.32,0.3])])))

#scala1 = T([1,2])([2.5,12.8])(scala1)
#scala2 = T(3)(3.7)(scala1)
scalaint2 = T([1,2,3])([7.2,7,14.1])(R([1,2])(PI)(scalaint20))
scalaint3 = T([2,3])([-6,26.3])(scalaint20)
piano = CUBOID([2.8,13.5,0.3])
piano = T([1,2,3])([4.7,-6.3,38.4])(piano)


scala_interna = STRUCT([scalaint1,scalaint2,scalaint3, piano])
scala_interna = T([1,2])([27,22])(scala_interna)
scala_interna = COLOR(ColorPlasm([128,128,128]))(scala_interna)

#scala_interna = T(2)(40.7)(scala_interna)






baseBalcone = CUBOID([1.5,3.5,0.2])
palettoRinghiera = CUBOID([0.05,0.05,0.65])
paletti = STRUCT(NN(24)([palettoRinghiera,T(2)(0.15)]))
paletti = T(3)(0.2)(paletti)
palettoRinghieraX = palettoRinghiera
palettoRinghieraX = T([1,2])([1,2])(palettoRinghieraX)
palettiX = STRUCT(NN(10)([palettoRinghiera,T(2)(0.15)]))
palettiX = R([1,2])(PI/2)(palettiX)
palettiX = T([1,3])([1.5,0.2])(palettiX)
upRinghieraY = CUBOID([0.05,3.5,0.05])
upRinghieraY = T(3)(0.85)(upRinghieraY)

upRinghieraX = CUBOID([1.5,0.05,0.05])
upRinghieraX = T(3)(0.85)(upRinghieraX)
upRinghieraX  =STRUCT(NN(2)([upRinghieraX,T(2)(3.45)]))
palettiX = STRUCT(NN(2)([palettiX,T(2)(3.45)]))
upRinghiera = STRUCT([upRinghieraX,upRinghieraY])
balcone = STRUCT([baseBalcone,paletti,upRinghiera,palettiX])




balcone1 = R([1,2])(PI/2)(balcone)
balcone1 = T([1,2,3])([12,-1,.3])(balcone1)
balcone1 = S([1,2,3])([2,2,3])(balcone1)
balconiRetro = STRUCT(NN(4)([balcone1,T(3)(12.5)]))
balconiRetro = STRUCT(NN(2)([balconiRetro,T(1)(21)]))



balcone = R([1,2])(-PI/2)(balcone)
balcone = T([1,2,3])([8.5,23.3,.3])(balcone)
balcone = S([1,2,3])([2,2,3])(balcone)

balconiFronte = STRUCT(NN(4)([balcone,T(3)(12.5)]))
balconiFronte = STRUCT(NN(2)([balconiFronte,T(1)(21)]))





tettoRetro= CUBOID([7,2,0.1])
tettoRetro = T([1,2,3])([17,-2,47.5])(tettoRetro)

tettiRetro = STRUCT(NN(2)([tettoRetro,T(1)(21.1)]))

tettiFronte = STRUCT(NN(2)([tettiRetro,T(2)(46)]))

balconi = STRUCT([balconiRetro,balconiFronte,tettiFronte,tettiRetro])




struttura = STRUCT([struttura,giardino2,giardino1,giardino3, scala,scala_interna,balconi])

VIEW(struttura)




