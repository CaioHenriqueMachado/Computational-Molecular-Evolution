from ClassSelex         import Selex 
from ClassEntropy       import ShannonEntropy

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
cycles_limit = 100

# MOLECULES LIMIT
molecules_limit = 500

# BREAK
condon_break = 'TTT'
prob_break = 10

# JOIN
prob_join = 5

# INSTANCE
project = Selex( mols, tam, target)

entropy = ShannonEntropy()

# GENERATION OF INITIAL MOLECULES
project.Generator()


cycle = 1
while( cycle <= cycles_limit ):
    # REPLICATION WITH MUTATION RATE(%)
    project.PolymeraseChainReaction(alpha)

    # MOLECULE BREAK
    project.Break( condon_break, prob_break)

    # MOLECULE JOINT
    project.Join(prob_join)

    # LIMITATION OF MOLECULES(%)
    project.ConstantPopulation(molecules_limit)

    # MOLECULES SELECTION
    project.Filter(beta)

    # SHANNON ENTROPY
    bits = entropy.Result(project.molecules)
    
    # Para exibição de cada ciclo
    print( '\nCYCLE: ',cycle )
    print('AFF: %.4f        AMOUNT: %i' %(project.all_affinity[cycle], project.all_amount[cycle]))
    print('BITS: %.4f       SIZE: %.2f' %(bits, project.all_averageSize[cycle]))

    if ( project.all_affinity[cycle] >= 1 ):
        break

    cycle += 1
    


 #Para construção de graficos                                                       <-- Lista de dados
list_affinity = project.all_affinity
list_entropy  = entropy.result_entropy
list_size   = project.all_averageSize                                                                                                                
list_amount       = project.all_amount
 
  

# GENERATING GRAPHICS

# 1° - AFINITY X CYCLE

axis_x = list_cycle
axis1_y = list_affinity 

plt.rcParams['figure.figsize'] = (12,8)

plt.subplot(2,2,1)
plt.title('AFFINITY')
plt.plot( axis_x , axis1_y, c ='#0000ff',lw = 3)
plt.xlabel('cycle')
plt.ylabel('affinity(%)')
plt.grid(True)


# 2° - QUANTITY OF MOLECULES X CYCLE 

axis2_y = list_amount

plt.subplot(2,2,2)
plt.title('QUANTITY OF MOLECULES')
plt.plot( axis_x , axis2_y, c ='#0000ff',lw = 3)
plt.xlabel('cycle')
plt.ylabel('quantity of molecules')
plt.grid(True)

# 3° - AVERAGE ENTROPY X CYCLE
  
axis3_y = list_entropy 

plt.subplot(2,2,3)
plt.title('AVERAGE ENTROPY')
plt.plot( axis_x , axis3_y, c ='#0000ff',lw = 3 )
plt.xlabel('cycle')
plt.ylabel('entropy(Bits)')
plt.grid(True)

# 4° - AVERAGE SIZE X CYCLE 
axis4_y = list_size

plt.subplot(2,2,4)
plt.title('AVERAGE SIZE')
plt.plot( axis_x , axis4_y, c ='#0000ff',lw = 3 )
plt.xlabel('cycle')
plt.ylabel('average size(Base)')
plt.grid(True)

plt.show()
