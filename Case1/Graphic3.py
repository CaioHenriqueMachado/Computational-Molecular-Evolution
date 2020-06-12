from pylab              import *
from ClassSelex         import Selex 
from ClassCalculation   import Calculation
from ClassEntropy       import ShannonEntropy

# ESTE CÓDIGO É PARA GERAR GRÁFICOS VARIANDO TAXA DE MUTAÇÃO OU EFICIÊNCIA DE FILTRO

# QUANTITY OF MOLECULES
mols = 500

# MOLECULES SIZE
tam = 100

# MUTATION RATE(%):
alpha = 0

# FILTER EFFICIENCY(%):
beta = 20

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

entropy = ShannonEntropy()

calculation = Calculation(alpha, beta, molecules_limit)

# GENERATION OF INITIAL MOLECULES
project.Generator()

list_allClycles =[]
list_affinity =[]
list_entropy =[]
list_size=[]
list_amount=[]

for i in range(5):
    cycle = 1
    while( cycle <= cycles_limit ):
        list_cycle.append(cycle)

        # REPLICATION WITH MUTATION RATE(%)
        project.PolymeraseChainReaction(alpha)

        # LIMITATION OF MOLECULES(%)
        project.ConstantPopulation(molecules_limit)

        # MOLECULES SELECTION
        project.Filter(beta)

        # SHANNON ENTROPY
        bits = entropy.Result(project.molecules)

        # CALCULATE
        test = calculation.GrowthEquation(project.all_affinity[cycle], project.molecules)
        
        # Para exibição de cada ciclo
        print( '\nCYCLE: ',cycle, 'PART: ', i )

        if ( project.all_affinity[cycle] >= 1 ):
            break

        cycle += 1
        


    #Para construção de graficos
    list_allClycles.append(list_cycle)
    list_affinity.append(project.all_affinity)
    list_entropy.append(entropy.result_entropy)
    list_size.append(project.all_averageSize)                                                                                                      
    list_amount.append(project.all_amount)
 
  

# GENERATING GRAPHICS

# 1° - AFINITY X CYCLE

axis1_x = list_allClycles[0]
axis2_x = list_allClycles[1]
axis3_x = list_allClycles[2]
axis4_x = list_allClycles[3]


axis1_1_y = list_affinity[0]
axis1_2_y = list_affinity[1]
axis1_3_y = list_affinity[2]
axis1_4_y = list_affinity[3]


plt.rcParams['figure.figsize'] = (12,8)

plt.subplot(2,2,1)
plt.title('AFFINITY')
plt.plot( axis1_x , axis1_1_y, c='b',lw=3)
plt.plot( axis2_x , axis1_2_y, c='g',lw=3)
plt.plot( axis3_x , axis1_3_y, c='r',lw=3)
plt.plot( axis4_x , axis1_4_y, c='y',lw=3)
plt.xlabel('cycle')
plt.ylabel('affinity(%)')
plt.grid(True)


# 2° - QUANTITY OF MOLECULES X CYCLE 

axis2_1_y = list_amount[0]
axis2_2_y = list_amount[1]
axis2_3_y = list_amount[2]
axis2_4_y = list_amount[3]


plt.subplot(2,2,2)
plt.title('QUANTITY OF MOLECULES')
plt.plot( axis1_x , axis2_1_y, c='b',lw=3)
plt.plot( axis2_x , axis2_2_y, c='g',lw=3)
plt.plot( axis3_x , axis2_3_y, c='r',lw=3)
plt.plot( axis4_x , axis2_4_y, c='y',lw=3)
plt.xlabel('cycle')
plt.ylabel('quantity of molecules')
plt.grid(True)

# 3° - AVERAGE ENTROPY X CYCLE
  
axis3_1_y = list_entropy[0]
axis3_2_y = list_entropy[1]
axis3_3_y = list_entropy[2]
axis3_4_y = list_entropy[3]

plt.subplot(2,2,3)
plt.title('AVERAGE ENTROPY')
plt.plot( axis1_x , axis3_1_y, c='b',lw=3)
plt.plot( axis2_x , axis3_2_y, c='g',lw=3)
plt.plot( axis3_x , axis3_3_y, c='r',lw=3)
plt.plot( axis4_x , axis3_4_y, c='y',lw=3)
plt.xlabel('cycle')
plt.ylabel('entropy(Bits)')
plt.grid(True)

# 4° - AVERAGE SIZE X CYCLE 
axis4_1_y = list_size[0]
axis4_2_y = list_size[1]
axis4_3_y = list_size[2]
axis4_4_y = list_size[3]

plt.subplot(2,2,4)
plt.title('AVERAGE SIZE')
plt.plot( axis1_x , axis4_1_y, c='b',lw=3)
plt.plot( axis2_x , axis4_2_y, c='g',lw=3)
plt.plot( axis3_x , axis4_3_y, c='r',lw=3)
plt.plot( axis4_x , axis4_4_y, c='y',lw=3)
plt.xlabel('cycle')
plt.ylabel('average size(Base)')
plt.grid(True)

plt.show()




# NESSE CÓDIGO A INTENÇÃO FOI GERAR 4 VEZES PARA VER AS 4 LINHAS EM CADA GRAFICOS