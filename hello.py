from pyplasm import *
from larcc import *
# commenti
# probabilmente nel compito sarà meglio ridefinire le funzioni seguenti

import scipy
from scipy import *

def larExtrude(model,pattern):
    """ Multidimensional extrusion 
        model is a LAR model: a pair (vertices, cells)
        pattern is a list of positive and negative sizes (multi-extrusion)
        
        Return a "model"
    """
    V, FV = model
    d, m = len(FV[0]), len(pattern)
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    offset, outcells, rangelimit = len(V), [], d*m
    for cell in FV:
        tube = [v + k*offset for k in range(m+1) for v in cell]
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube, newshape=(m,d,d+1)).tolist()]
    
    outcells = AA(CAT)(TRANS(outcells))
    cellGroups = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    outVertices = [v+[z] for z in coords for v in V]
    outModel = outVertices, CAT(cellGroups)
    return outModel

def larSimplexGrid(shape):
    """ User interface in LARCC.
        
        Return an (hyper-)cuboid of given shape. Vertices have integer coords
    """
    model = V0,CV0 = [[]],[[0]]    # the empty simplicial model
    for item in shape:
        model = larExtrude(model,item * [1])
    return model



# IMPARARE A USARE GRID

 a = [[0,0],[.5,0],[0,.5],[.5,.5],[1,.5],[1.5,.5],[1.5,1],[.25,1]]
 P = AA(MK)(a) ##apply to all -> MK di a. ritorna un array di punti
VIEW(STRUCT(b)) # visualizza i punti


VIEW(JOIN(P)) oppure VIEW(AA(JOIN)([P])) #Join(b) unisce tutti i punti di p e restituisce un oggetto
#VIEW vuole un oggetto come parametro, quindi non devo fare una struct

# se voglio fare piu join separati devo usare per forza AA


# per comporre più oggetti posso fare  c = STRUCT([a,b] e poi VIEW(c)

# apply to all è una funzione doppia. vuole una funzione e un array di punti ai quali applicare la funzione
# invece di un array posso passargli piu array nella forma [a1, a2, a3] ai quali applicare separatamente la funzione

S = AA(JOIN)([P[0:4],P[4:7],P[7]]) #slicing: P[0:4] sottoinsieme di P da 0 incluso a 4 escluso
# SKELETON(1)(S) fa lo scheletro delle figure piene e restituisce una LISTA di punti

VIEW(STRUCT(AA(SKELETON(1))(S))) #usare struct per visualizzare una lista di punti


# SIMPLESSO serve per fare triangoli n-dimensionali
# SIMPLEX(n)
# è un join di n+1 punti affinemente indipendenti chiamati vertici
# n+1 punti sono affinemente indipendenti se n-1 VETTORI sono linearmente indipendenti
# crea una figura geometrica n dimensionale con n+1 punti (vertici) aff. indipendenti
# es. tetraedro (tridimensionale) con 4 vertici non complanari -> SIMPLEX(3)

s0,s1,s2,s3 = [SIMPLEX(d) for d in range(4)]

#SIMPLEX(0) è vuoto, 1 è una retta, 2 un triangolo, 3 un tetraedro
#range(4) = da 0 a 3



# un simplesso generato da un QUALUNQUE sottoinsieme di d+1 vertici (d=dimensione del simplesso) costituisce una faccia del simplesso originale
# chiamata faccetta
# i d+1 vertici sono semplicemente il numero di vertici del simplesso originale

#COMPLESSO SIMPLICIALE
# il complesso simpliciale è un insieme di simplessi (sigma grande) che verifica le condizioni:

# 1 se un simplesso sta nel complesso simpliciale (sigma grande) qualunque sua faccia sta nel complesso
# 2 (IMPORTANTE!!) presi due simplessi in un complesso, l’intersezione è in un complesso, e deve essere quindi una faccia per entrambi i poligoni

# supporto geometrico in un complesso = unione degli insiemi di punti dei suoi simplessi


from random import random as rand
points = [[2*PI*rand(),rand()] for k in range(1000)]
V = [[SQRT(r)*COS(alpha),SQRT(r)*SIN(alpha)] for alpha,r in points]
cells = [[k+1] for k,v in enumerate(V)]
VIEW(MKPOL([V,cells,None]))

from scipy.spatial import Delaunay
FV = Delaunay(array(V)).vertices
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,FV))))
VIEW(SKELETON(1)(STRUCT(MKPOLS((V,FV)))))

#capire come funzione MKPOLS e MKPOL oltre a EXPLODE


#COMPLESSO CUBOIDALE = insieme di cuboidi
# cuboide = quadrato n diensionale -> d=1 segmento, d=2 quadrato, d=3 cubo

#mappa simpliciale
# MAP = funzione di secondo ordine, ossia va applicata due volte per restituire un risultato

# map si applica prima a una funzione simpliciale e poi a un dominio geometrico che verrà trasformato dall’applicazione di quella funzione
# la funzione simpliciale è applicata ai vertici del dominio 
# il tipo di dato del dominio è HPC: tipo di dato geometrico in Plasm


def sphere1(p): return [COS(p[0]), SIN(p[0])] # point function

def circle(r):
    def circle0(p):
alpha = p[0]
        return [r*COS(alpha), r*SIN(alpha)]
    return circle0

obj = MAP(circle(2))(INTERVALS(2*PI)(32))  # per fare un cerchio con un certo raggio

def domain(n): return INTERVALS(2*PI)(n)
VIEW( MAP(sphere1)(domain(32)) )

#domain(32) crea 32 punti tra 0 e 2*Pigreco
# questi punti sono passati alla funzione sphere1 che li mappa in una sfera di raggio 1

#ps: se uso domain(4) lui fa una sfera con 4 punti, ossia un quadrato
# in questo modo posso creare poligoni piani

#sphere1 : viene applicata a tutti i vertici del complesso simpliciale “domain(32)" e ritorna un array di funzioni coordinate


def disk2D(p):
    u,v = p
    return [v*COS(u), v*SIN(u)]


domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(1)(3)]) # 2D domain decompos 
VIEW( MAP(disk2D)(domain2D) ) # questo mi serve per fare figure bidimensionali piene
# se uso 4 invece di 32 faccio un quadrato riempito...ecc... 
# cambiando il 3 invece posso suddividere in n parti la figura ...il risultato è visibile solo con le skeletro

VIEW( SKELETON(1)(MAP(disk2D)(domain2D)) )


q=QUOTE([2,-2,4,4,-5,4,-1,1])

#crea un segmento lungo q.length, in cui i termini negativi rappresentano spazi


base = PROD([q,q])
altezza = PROD([q, Q(n)]) # n dipende da quanto la voglio alzare
# con quello alzo tridimensionalmente qualsiasi disegno



 c1= COLOR(RED)(PROD([base1,Q(4)]))


def helix(r):     
	def helix0(pitch):
		def helix1(p):
			return [r*COS(p[0]), r*SIN(p[0]), (pitch/(2*PI))*p[0]]
		return helix1
	return helix0





# pitch è il passo dell’elica ossia la distanza tra due spire

def domain(len,n):
	return INTERVALS(len)(n) 


VIEW( MAP(helix(0.2)(0.05))(domain(10*(2*PI),320)) )



def helicoid(radius): # point function 
    def helix0(pitch):
        def helix1(p):
            a,r = p
            return [radius*r*COS(a), -radius*r*SIN(a), (pitch/(2*PI))*a]
        return helix1
    return helix0




# il punto a cui viene applicata elica ha punto e raggio (coord polari) stesso discorso del cerchio pieno (u, v)

fun = helicoid(0.5)(0.333)
dom = PROD([INTERVALS(2*PI*3)(64), INTERVALS(1)(4)])

def domain(shape): # simplicial decomposition of domain 
    def domain0(size):
        return S([1,2])(size)(GRID(shape))
    return domain0

dom = domain([64,4])([2*PI*3,1])


pol = MAP(fun)(dom)
VIEW( pol )
VIEW( SKELETON(1)(pol) )

# helicoid gli passo solo due parametri, anche se del terzo ordine

#il terzo glielo passa MAP


# grid prende le coordinate intere
#S è una primitiva che scala
#funzione del terzo ordine (applicata 3 volte)
#prima: a quali coordinate [1,2]= x e y
#2: di quanto deve scalare (size)
#3 
#T trasla
#R rotazione


def dom(n):
    return INTERVALS(2*PI*n)(24*n)


def spiral(pitch,n):
    def spiral0(p):
        alpha = p[0]
        return [COS(alpha), SIN(alpha), alpha*pitch*n/(2*PI*n)
    return spiral0


obj = MAP(spiral(0.2,5))(dom(5))
VIEW(obj)




dom2D = PROD([INTERVALS(2*PI)(24), INTERVALS(1)(1)])
VIEW(dom2D)
VIEW(SKELETON(1)(dom2D))





def spiral(p):
    alpha,r = p
    return [r*COS(alpha), r*SIN(alpha), alpha/(2*PI)]
obj = MAP(spiral)(dom2D)
VIEW(obj)

dom1D = INTERVALS(1)(1)
dom3D = INSR(PROD)([INTERVALS(2*PI)(24), dom1D, dom1D])

def spiral(p):
    alpha,r,h = p
    return [r*COS(alpha), r*SIN(alpha), h*alpha/(2*PI)]

obj = MAP(spiral)(dom3D)
VIEW(obj)



dom1D = INTERVALS(1)(1)
dom3D = INSR(PROD)([INTERVALS(2*PI)(24), dom1D, dom1D])
def spiral(p):
    alpha,r,h = p
    return [r*COS(alpha), r*SIN(alpha), h*alpha/(2*PI)]
obj = MAP(spiral)(dom3D)
VIEW(obj)




dom3D = INSR(PROD)([INTERVALS(2*PI)(24), dom1D, dom1D])
def spiral1(p):
alpha,r,h = p
    return [r*COS(alpha), r*SIN(alpha), alpha/(2*PI)]
def spiral2(p):
    alpha,r,h = p
    return [r*COS(alpha), r*SIN(alpha), alpha/(2*PI) + 0.1]

obj = STRUCT([MAP(spiral1)(dom3D), MAP(spiral2)(dom3D)])
VIEW(obj)
obj = MAP(BEZIER(S3)([spiral1,spiral2]))(dom3D)
VIEW(obj)






