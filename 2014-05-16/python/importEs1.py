
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, '/Users/Amirs/Desktop/grafica computazionale/lar-cc/lib/py')


from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])


# complesso totale diviso in 4
master = assemblyDiagramInit([4,4,2])([[1,4.8,11.2, 1],[1,10.1,15.3,1],[.3,10.5]])

master2 = assemblyDiagramInit([4,4,2])([[1,10.1,15.3,1],[1,11.2,4.8,1],[.3,10.5]])
master3 = assemblyDiagramInit([4,4,2])([[1,10.1,15.3,1],[1,4.8,11.2,1],[.3,10.5]])




V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)









V2,CV2 = master2
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(CV2)),CYAN,2)
#VIEW(hpc2)







V3,CV3 = master3
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(CV3)),CYAN,2)
#VIEW(hpc3)


toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([3,1,1])([[0.2,3.2,7.8],[1.2],[10.5]])
master = diagram2cell(diagram,master,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)







toMerge = 3
#cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([1,3,1])([[1.2],[7.8,3.2,0.2],[10.5]])
master2 = diagram2cell(diagram,master2,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)





toMerge = 5
#cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([1,3,1])([[1.2],[0.2,3.2,7.8],[10.5]])
master3 = diagram2cell(diagram,master3,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)










toRemove = [32]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master
#DRAW(master)

master2 = master2[0], [cell for k,cell in enumerate(master2[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master

master3 = master3[0], [cell for k,cell in enumerate(master3[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master


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







toMerge = 8
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([3,1,2])([[3.8,4.8,1.4],[1],[8,2.5]])
master2 = diagram2cell(diagram,master2,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella


hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)





toMerge = 14
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  # solidifica una cella
#VIEW(STRUCT([hpc,cell]))     

# 


diagram = assemblyDiagramInit([3,1,2])([[3.8,4.8,1.4],[1],[8,2.5]])
master3 = diagram2cell(diagram,master3,toMerge)   # ha fatto la porta che e' alzata a partire dalla cella
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)














toRemove = [34]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master
#DRAW(master)

master2 = master2[0], [cell for k,cell in enumerate(master2[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master

master3 = master3[0], [cell for k,cell in enumerate(master3[1]) if not (k in toRemove)]  # rimuove la cella della porta dal master


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)





hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)













# cucina
toMerge =11
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None]) 


diagram = assemblyDiagramInit([3,4,1])([[0.2,4.4,0.2],[0.2,6.4,3.3,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [5,6,10]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)



master = diagram2cell(diagram,master,toMerge) 
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)





# cucina
toMerge =11


diagram = assemblyDiagramInit([4,3,1])([[0.2,6.4,3.3,0.2],[0.2,4.4,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)

#VIEW(hpc)

toRemove = [6,7,4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master2= diagram2cell(diagram,master2,toMerge) 
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)









# cucina
toMerge =10


diagram = assemblyDiagramInit([4,3,1])([[0.2,6.4,3.3,0.2],[0.2,4.4,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [8,7,4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master3= diagram2cell(diagram,master3,toMerge) 
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)








# salotto 
toMerge =17

diagram = assemblyDiagramInit([5,7,1])([[0.2,3.2,0.4,7.2,0.2],[0.2,3.6,1.2,1.4,2,1.2,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)



toRemove = [7,8,9,10,11,12,13,30,4,5,22,23,24,25,26,32,31,19,18,17,16]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)



# salone + cucina

master = diagram2cell(diagram,master,toMerge)   # 
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)











# salotto 
toMerge =9

diagram = assemblyDiagramInit([7,5,1])([[0.2,3.6,1.2,1.4,2,1.2,0.2],[0.2,7.2,0.4,3.2,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)



toRemove = [8,7,6,11,12,13,16,17,18,21,22,23,24,26,27,28,29,33,3,10,15,20]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)



# salone + cucina

master2 = diagram2cell(diagram,master2,toMerge)   # 
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)








# salotto 
toMerge =11

diagram = assemblyDiagramInit([7,5,1])([[0.2,3.6,1.2,1.4,2,1.2,0.2],[0.2,3.2,0.4,7.2,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)



toRemove = [1,8,13,18,23,28,6,11,16,21,26,17,22,27,20,28,31,25]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)



# salone + cucina

master3= diagram2cell(diagram,master3,toMerge) 
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)













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
#DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)










toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([8,3,1])([[0.2,1.2,3.2,1.2,0.4,3.2,6,.2],[0.2,4.8,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [6,7,15,16,19,10,4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)




master2 = diagram2cell(diagram,master2,toMerge)
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)








toMerge = 15
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([8,3,1])([[0.2,1.2,3.2,1.2,0.4,3.2,6,.2],[0.2,4.8,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))    
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4,8,7,10,16,19,17]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)



master3= diagram2cell(diagram,master3,toMerge) 
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)











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
#DRAW(diagram)




master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 15
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([8,5,1])([[0.2,1.2,3.2,1.6,3.2,0.4,5.6,0.2],[0.2,7.2,0.4,3.2,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [3,22,28,6,11,16,21,31,32,23,18,13,8,14,24,33]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)




master2 = diagram2cell(diagram,master2,toMerge)
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)







toMerge = 16
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([8,5,1])([[0.2,1.2,3.2,1.6,3.2,0.4,5.6,0.2],[0.2,3.2,0.4,7.2,0.2],[10.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [1,6,11,16,21,26,31,20,22,33,23,18,13,8,32,10]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)



master3= diagram2cell(diagram,master3,toMerge) 
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)














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




toMerge = 13
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([5,1,3])([[1.4,3.2,6.4,3.2,1.4],[1],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4,10]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master2 = diagram2cell(diagram,master2,toMerge)
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)



toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([5,1,3])([[1.4,3.2,6.4,3.2,1.4],[1],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4,10]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master3= diagram2cell(diagram,master3,toMerge) 
hpc3 = SKEL_1(STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)




















toMerge = 94
diagram = assemblyDiagramInit([1,3,3])([[0.2],[1.2,3.2,1.2],[4,4,2.5]])
toRemove = [4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
master = diagram2cell(diagram,master,94)

toMerge = 90
diagram = assemblyDiagramInit([1,1,3])([[0.2],[3.5],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
toRemove = [1]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
master = diagram2cell(diagram,master,90)



hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)









toMerge = 78
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,3])([[3.5],[.2],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [1]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)




master2 = diagram2cell(diagram,master2,toMerge)
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)





toMerge = 87
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])

diagram = assemblyDiagramInit([3,1,3])([[1.2,3.2,1.2],[0.2],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master2 = diagram2cell(diagram,master2,toMerge)
hpc2 = SKEL_1(STRUCT(MKPOLS(master2)))
hpc2 = cellNumbering (master2,hpc2)(range(len(master2[1])),CYAN,2)
#VIEW(hpc2)












toMerge = 94
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])

diagram = assemblyDiagramInit([3,1,3])([[1.2,3.2,1.2],[0.2],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [4]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)

master3= diagram2cell(diagram,master3,toMerge) 
hpc3 = (STRUCT(MKPOLS(master3)))
hpc3 = cellNumbering (master3,hpc3)(range(len(master3[1])),CYAN,2)
#VIEW(hpc3)





toMerge = 84
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,3])([[3.5],[.2],[4,4,2.5]])
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(diagram[1])),CYAN,2)
#VIEW(hpc)

toRemove = [1]
diagram = diagram[0], [cell for k,cell in enumerate(diagram[1]) if not (k in toRemove)]
#DRAW(diagram)


master3= diagram2cell(diagram,master3,toMerge) 



toRemove = [50,52,53]
master3 = master3[0], [cell for k,cell in enumerate(master3[1]) if not (k in toRemove)]



#VIEW(STRUCT(MKPOLS(master)))

#VIEW(STRUCT(MKPOLS(master2)))
