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
    result = calculation.GrowthEquation(project.all_affinity[cycle], project.molecules)
    
    # Para exibição de cada ciclo
    print( '\nCYCLE: ',cycle )
    print('AFF: %.4f        AMOUNT: %i' %(project.all_affinity[cycle], project.all_amount[cycle]))
    print('BITS: %.4f       SIZE: %.2f' %(bits, project.all_averageSize[cycle]))
    print('CALCULADO: %.4f'%(result))

    if ( project.all_affinity[cycle] >= 1 ):
        break

    cycle += 1
    






#Para construção de graficos                                                       <-- Lista de dados
list_affinity = project.all_affinity
list_entropy  = entropy.result_entropy
list_size   = project.all_averageSize                                                                                                                
list_amount       = project.all_amount
list_affinity_calculate = calculation.all_results
  


# GENERATING GRAPHICS



# 1° - AFINITY X CYCLE (CALCULATED X SIMULATED)

axis_x = list_cycle
axis1_y = list_affinity
# CALCULATED
axis2_y = list_affinity_calculate

plt.rcParams['figure.figsize'] = (8,12)
plt.title('MUTATION RATE %d (CALCULATED X SIMULATED)'%alpha)
plt.subplot(1,2,1)
plt.plot( axis_x , axis1_y )
plt.plot( axis_x , axis2_y )
plt.xlabel('CYCLE')
plt.ylabel('AFFINITY')
plt.grid(True)

plt.show()

#2° - QUANTITY OF MOLECULES X CYCLE 

# SIMULATED
axis3_y = list_amount
# CALCULATED  
axis4_y = list_amount

plt.title('MUTATION RATE %d (CALCULATED X SIMULATED)'%alpha)
plt.subplot(1,2,2)
plt.plot( axis_x , axis3_y )
plt.plot( axis_x , axis4_y )
plt.xlabel('CYCLE')
plt.ylabel('QUANTITY OF MOLECULES')
plt.grid(True)
plt.show()


    
