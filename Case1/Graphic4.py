from pylab              import *  
from ClassSelex         import Selex 
from ClassCalculation   import Calculation
from ClassEntropy       import ShannonEntropy

# ESTE CÓDIGO É PARA COMPARAR 1 FILTRO DE 20% E 2 FILTROS DE 10%

# QUANTITY OF MOLECULES
mols = 500

# MOLECULES SIZE
tam = 100

# MUTATION RATE(%):
alpha = 0

# FILTER EFFICIENCY(%):
beta = 20

# FILTER EFFICIENCY(%):
beta1 = 10

# TARGET
target = 5

# CYCLES LIMIT
cycles_limit = 500

# MOLECULES LIMIT
molecules_limit = 500

# GRAFICS
list_cycle     = [0]
list_size      = []
list_amount    = []
list_entropy  = []


project = Selex( mols, tam, target)
project1 = Selex( mols, tam, target)

entropy = ShannonEntropy()

calculation = Calculation(alpha, beta, molecules_limit)

# GENERATION OF INITIAL MOLECULES
project.Generator()
project1.Generator()



cycle = 1
while( cycle <= cycles_limit ):
    list_cycle.append(cycle)

    # REPLICATION WITH MUTATION RATE(%)
    project.PolymeraseChainReaction(alpha)
    project1.PolymeraseChainReaction(alpha)

    # LIMITATION OF MOLECULES(%)
    project.ConstantPopulation(molecules_limit)
    project1.ConstantPopulation(molecules_limit)

    # MOLECULES SELECTION
    project.Filter(beta)
    project1.Filter(beta1)
    project1.Filter(beta1)

    # SHANNON ENTROPY
    bits = entropy.Result(project.molecules)

    # CALCULATE
    test = calculation.GrowthEquation(project.all_affinity[cycle], project.molecules)
    
    # Para exibição de cada ciclo
    print( '\nCYCLE: ',cycle )

    if ( project.all_affinity[cycle] >= 1 ):
        break

    cycle += 1
    

affinity1 =[0]
amount1 =[0]
for i in range(len(project1.all_affinity)):
    if (i %2 != 0):
        affinity1.append(project1.all_affinity[i])
        amount1.append(project1.all_amount[i])

 #Para construção de graficos                                                       <-- Lista de dados
list_affinity   = project.all_affinity
list_affinity1  = affinity1                  
list_amount     = project.all_amount
list_amount1    = amount1
 

# GENERATING GRAPHICS

# 1° - AFINITY X CYCLE

axis_x = list_cycle
axis1_0_y = list_affinity 
axis1_1_y = list_affinity1

plt.rcParams['figure.figsize'] = (12,8)

plt.subplot(1,2,1)
plt.title('ONE FILTER')
plt.plot( axis_x , axis1_0_y, c ='b',lw = 3)
plt.plot( axis_x , axis1_1_y, c ='g',lw = 3)
plt.xlabel('cycle')
plt.ylabel('affinity(%)')
plt.grid(True)


# 2° - QUANTITY OF MOLECULES X CYCLE 

axis2_0_y = list_amount
axis2_1_y = list_amount1

plt.subplot(1,2,2)
plt.title('TWO FILTERS')
plt.plot( axis_x , axis2_0_y, c ='b',lw = 3)
plt.plot( axis_x , axis2_1_y, c ='g',lw = 3)
plt.xlabel('cycle')
plt.ylabel('quantity of molecules')
plt.grid(True)


plt.show()

