import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, '/Users/Amirs/Desktop/grafica computazionale/lar-cc/lib/py')


from sysml import *






def MERGE_AND_REMOVE(shape, size,toMerge,master):
	cellDiagram=1
	for v in shape:
		cellDiagram=cellDiagram*v
	diagram = assemblyDiagramInit(shape)(size)
	minBlock = len(master[1])-1
	master = diagram2cell(diagram,master,toMerge) 
	hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
	totalBlocks = minBlock+cellDiagram
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)
	hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
	hpc = cellNumbering (diagram,hpc)(range(minBlock, totalBlocks),CYAN,2)
	VIEW(hpc)
	scelta = []
	v = False
   	while v == False:
	    i = input("Enter a number: (scrivere -1 per uscire) ")
	    if len(scelta) == 0:
	    	v = True
	    scelta.append(i)
	master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in scelta)] 
	hpc = STRUCT(MKPOLS(master))
	VIEW(hpc)
	return master




def REMOVE_CELL(master):

	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

	VIEW(hpc)
	scelta = []
	v=False
   	while v==False:
	    i = input("Enter a number: (scrivere -1 per uscire) ")
	    if len(scelta) == 0:
	    	v=True
	    scelta.append(i)
	master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in scelta)] 
	hpc = STRUCT(MKPOLS(master))
	VIEW(hpc)
	return master





def REMOVE_CELL(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)
	def REMOVE_CELL0(scelta=[]):
		if len(scelta) == 0:
			v=True
   			while v == True:
   				i = input("Enter a number: (scrivere -1 per uscire) ")
	    		if(i < 0):
	    			v=False
	    		scelta.append(i)
		master1 = master[0], [cell for k,cell in enumerate(master[1]) if not (k in scelta)] 
		hpc = STRUCT(MKPOLS(master1))
		VIEW(hpc)
		return master1
	return REMOVE_CELL0





def MERGE_AND_REMOVE(shape, size,toMerge,master):
	cellDiagram=1
	for v in shape:
		cellDiagram=cellDiagram*v
	diagram = assemblyDiagramInit(shape)(size)
	minBlock = len(master[1])-1
	totalBlocks = minBlock+cellDiagram
	master = diagram2cell(diagram,master,toMerge) 
	def MERGE_AND_REMOVE0(scelta=[]):
		if len(scelta) == 0:
			hpc = SKEL_1(STRUCT(MKPOLS(master)))
			hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
			VIEW(hpc)
			hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
			hpc = cellNumbering (diagram,hpc)(range(minBlock, totalBlocks),CYAN,2)
			VIEW(hpc)
			v=True
			while v==True:
   				i = input("Enter a number: (scrivere -1 per uscire) ")
	    		if(i < 0):
	    			v=False
	    		scelta.append(i)
		master1 = master[0], [cell for k,cell in enumerate(master[1]) if not (k in scelta)] 
		hpc = STRUCT(MKPOLS(master1))
		VIEW(hpc)
		return master1
	return MERGE_AND_REMOVE0



def VIEW_MODEL(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)


""" Drawing numbers of cells """
def cellNumbering (larModel,hpcModel):
   V,CV = larModel
   def cellNumbering0 (cellSubset,color=WHITE,scalingFactor=1):
      text = TEXTWITHATTRIBUTES (TEXTALIGNMENT='centre', TEXTANGLE=0, 
                     TEXTWIDTH=0.1*scalingFactor, 
                     TEXTHEIGHT=0.2*scalingFactor, 
                     TEXTSPACING=0.025*scalingFactor)
      hpcList = [hpcModel]
      i =0
      for cell in cellSubset:
         point = CCOMB([V[v] for v in CV[i]])
         hpcList.append(T([1,2,3])(point)(COLOR(color)(text(str(cell)))))
         i=i+1
      return STRUCT(hpcList)
   return cellNumbering0










DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([7,5,2])([[.3,4,.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])


master = REMOVE_CELL(master)([13,17,37,33,53,57])


# per farlo manualmente
#master = REMOVE_CELL(master)()



VIEW_MODEL(master)



# QUESTA FUNZIONE VISUALIZZA I CELLNUMBERS E FA SCEGLIERE ALL'UTENTE QUALI E QUANTI BLOCCHI ELIMINARE
#master=MERGE_AND_REMOVE([3,1,2],[[2,1,2],[.3],[2.2,.5]],47,master)()
# 65



master=MERGE_AND_REMOVE([3,1,2],[[2,1,2],[.3],[2.2,.5]],47,master)([65])





#master= MERGE_AND_REMOVE([5,1,3],[[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]],52,master)()
# 71 e 77

master= MERGE_AND_REMOVE([5,1,3],[[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]],52,master)([71,77])



