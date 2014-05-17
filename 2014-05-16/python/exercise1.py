
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, '/Users/Amirs/Desktop/grafica computazionale/lar-cc/lib/py')


from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])


# complesso totale diviso in 4
master = assemblyDiagramInit([4,4,2])([[1,4.8,11.2, 1],[1,10.1,15.3,1],[.3,10.5]])

V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)






toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([3,1,1])([[0.2,3.2,7.8],[1.2],[10.5]])
master = diagram2cell(diagram,master,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [32]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master
#DRAW(master)




hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)









#finestra salone

toMerge = 26
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([1,3,2])([[1],[3.8,4.8,1.4],[8,2.5]])
master = diagram2cell(diagram,master,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [34]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master
#DRAW(master)




hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

















# cucina
toMerge =11
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None]) 


diagram = assemblyDiagramInit([3,4,1])([[0.2,4.4,0.2],[0.2,6.4,3.3,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [5,6,10]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
DRAW(diagram)




master = diagram2cell(diagram,master,toMerge) 
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)




# salotto 
toMerge =17

diagram = assemblyDiagramInit([5,7,1])([[0.2,3.2,0.4,7.2,0.2],[0.2,3.6,1.2,1.4,2,1.2,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)



toRemove = [7,8,9,10,11,12,13,30,4,5,22,23,24,25,26,32,31,19,18,17,16]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
DRAW(diagram)



# salone + cucina

master = diagram2cell(diagram,master,toMerge)   # 
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)




# bagno e stanza




toMerge = 12
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([3,8,1])([[0.2,4.8,0.2],[0.2,1.2,3.2,1.2,0.4,3.2,6,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [9,10,11,13,14,18,21]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)



# camere da letto




toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([5,8,1])([[0.2,3.2,0.4,7.2,0.2],[0.2,1.2,3.2,1.6,3.2,0.4,5.6,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [8,14,13,12,11,10,9,2,4,25,26,27,28,30,22,20]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)












# 2 finestre

toMerge = 23
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,5,3])([[1],[1.4,3.2,6.4,3.2,1.4],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4,10]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)






master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



# finestra bagno


toMerge = 56
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,3])([[1],[3.3],[6,2,1.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [1]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)






toMerge = 5
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,3,3])([[1],[1.3,3.2,11],[6,2,1.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)











toMerge = 87
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,3])([[0.2],[3.5],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [1]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)







toMerge = 90
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])

diagram = assemblyDiagramInit([1,3,3])([[0.2],[1.2,3.2,1.2],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



VIEW(STRUCT(MKPOLS(master)))

