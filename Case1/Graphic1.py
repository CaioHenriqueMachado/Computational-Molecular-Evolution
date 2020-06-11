from pylab              import *   
from SelexClass         import Selex 
from CalculationClass   import Calculation
from EntropyClass       import ShannonEntropy

# ESTE CÓDIGO É PARA GERAR GRÁFICOS VARIANDO TAXA DE MUTAÇÃO OU EFICIÊNCIA DE FILTRO

# QUANTITY OF MOLECULES
mols = 500

# MOLECULES SIZE
tam = 50

# MUTATION RATE(%):
alpha = 10

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
lista_entropy  = []


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
    test = calculation.GrowthEquation(project.all_affinity[cycle], project.molecules)
    
    # Para exibição de cada ciclo
    print( '\nCYCLE: ',cycle )
    print('AFF: %.4f        AMOUNT: %i' %(project.all_affinity[cycle], project.all_amount[cycle]))
    print('BITS: %.4f       SIZE: %.2f' %(bits, project.all_averageSize[cycle]))
    print('CALCULADO: %.4f'%(test))

    if ( project.all_affinity[cycle] >= 1 ):
        break

    cycle += 1
    




 #Para construção de graficos                                                       <-- Lista de dados
lista_afinidade = project.all_affinity
lista_entropy  = entropy.result_entropy
list_size   = project.all_averageSize                                                                                                                
list_amount       = project.all_amount
 
  

# Gerando 4 graficos 

#Primeiro (Afinidade X Ciclo) 
    
grafico1_x = list_cycle
grafico1_y = lista_afinidade 

plt.rcParams['figure.figsize'] = (12,8)

plt.subplot(2,2,1)
plt.title('AFINIDADE (mol. afins)')
plt.plot( grafico1_x , grafico1_y, c ='#0000ff',lw = 3)
plt.xlabel('Ciclo/Round')
plt.ylabel('Afinidade(%)')

plt.grid(True)

#Segundo (QTD_moleculas X Ciclo)   
grafico2_x = list_cycle
grafico2_y = list_amount

plt.subplot(2,2,2)
plt.title('QUANTIDADE DE MOLÉCULAS')
plt.plot( grafico2_x , grafico2_y, c ='#0000ff',lw = 3)
plt.xlabel('Ciclo/Round')
plt.ylabel('QTD_moléculas')
plt.grid(True)

#Terceiro (Entropia X Ciclo)   
grafico3_x = list_cycle
grafico3_y = lista_entropy 

plt.subplot(2,2,3)
plt.title('ENTROPIA MÉDIA DAS MOLÉCULAS (Bits)')
plt.plot( grafico3_x , grafico3_y, c ='#0000ff',lw = 3 )
plt.xlabel('Ciclo/Round')
plt.ylabel('Entropia')
plt.grid(True)

#Quarto (Tamanho medio X Ciclo)   
grafico4_x = list_cycle
grafico4_y = list_size

plt.subplot(2,2,4)
plt.title('TAMANHO MÉDIO DAS MOLÉCULAS (Base)')
plt.plot( grafico4_x , grafico4_y, c ='#0000ff',lw = 3 )
plt.xlabel('Ciclo/Round')
plt.ylabel('Tamanho Médio')
plt.grid(True)

plt.show()
