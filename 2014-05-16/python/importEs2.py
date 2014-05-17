
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





diagram = larApply(r(0,0,-PI/2))(master)
diagram0 = larApply(r(0,0,PI))(diagram)



master = assemblyDiagramInit([3,2,8])([[27.5,7,27.5],[18,18],[0.5,10.5,0.3,10.5,0.3,10.5,0.3,10.5]])

V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#VIEW(hpc)


master = REMOVE_CELL(master)([23,21,19,17,25,27,29,31])


#VIEW_MODEL(master)






master = diagram2cell(diagram,master,1) 

master = diagram2cell(diagram,master,2) 
master = diagram2cell(diagram,master,3) 
master = diagram2cell(diagram,master,4) 
master = diagram2cell(diagram,master,5) 
master = diagram2cell(diagram,master,6) 
master = diagram2cell(diagram,master,7) 
master = diagram2cell(diagram,master,8) 




master = diagram2cell(diagram0,master,25) 

master = diagram2cell(diagram0,master,26) 
master = diagram2cell(diagram0,master,27) 
master = diagram2cell(diagram0,master,28) 



master = diagram2cell(diagram0,master,17) 
master = diagram2cell(diagram0,master,18) 
master = diagram2cell(diagram0,master,19) 
master = diagram2cell(diagram0,master,20) 


#VIEW_MODEL(master)


struttura = STRUCT(MKPOLS(master))

#VIEW(struttura)






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



giardino2 = R([1,2])(PI/2)(giardino2)

giardino2 = T([1,2])([60,-20])(giardino2)



giardino2 = COLOR(ColorPlasm([23,114,69]))(giardino2)







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




# scala esterna d'emergenza


a=STRUCT(MKPOLS(spiralStair(0.7,3.3,1.5,.3,7,3, 20)))
c=CUBOID([1.9,3.9,0.5])
c = T([1,2])([1.3,-4])(c)








c2=CUBOID([1.9,3.9,0.5])
c2 = T([1,2,3])([-3.5,-4,10.8])(c2)

a = STRUCT([a,c,c2])


scala = T([1,2])([31.3,40])(a)


scala2 = T(3)(10.8)(scala)
scala3 = T(3)(10.8)(scala2)
scala = STRUCT([scala,scala2,scala3])


struttura = STRUCT([struttura,giardino2,giardino1,giardino3, scala])
#VIEW(struttura)

