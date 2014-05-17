
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, '/Users/Amirs/Desktop/grafica computazionale/lar-cc/lib/py')


from importEs1 import *


#VIEW(STRUCT(MKPOLS(master)))
#diagram = R([1,2])(PI/2)(DRAW(master))
diagram = larApply(r(0,0,-PI/2))(master)
diagram0 = larApply(r(0,0,PI))(diagram)


#VIEW(STRUCT(MKPOLS(diagram)))

# complesso totale diviso in 4
master = assemblyDiagramInit([3,2,6])([[27.5,7,27.5],[18,18],[0.5,10.5,10.5,10.5,10.5,0.5]])

V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#VIEW(hpc)



toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  
#VIEW(STRUCT([hpc,cell]))     

# 


master = diagram2cell(diagram,master,toMerge)   
#VIEW(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)






toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge) 
#VIEW(STRUCT(MKPOLS(master)))

hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)




toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)





toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)




toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)






toMerge = 23
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


toMerge = 23
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 23
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 23
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)



toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])  

# 


master = diagram2cell(diagram0,master,toMerge)   
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


#VIEW(STRUCT(MKPOLS(master)))

