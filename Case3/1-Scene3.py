from ClassSelex         import Selex 
# from ClassEntropy       import ShannonEntropy

# QUANTITY OF MOLECULES
mols = 100

# MOLECULES SIZE
tam = 10

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

# entropy = ShannonEntropy()

# GENERATION OF INITIAL MOLECULES
project.Generator()


cycle = 1
while( cycle <= cycles_limit ):
    # REPLICATION WITH MUTATION RATE(%)
    project.PolymeraseChainReaction(alpha)
    print('1')
    # MOLECULE BREAK
    project.Break( condon_break, prob_break)
    print('2')
    # MOLECULE JOINT
    project.Join(prob_join)
    print('3')
    # MOLECULES SELECTION
    project.Filter(beta)
    print('4')
    # SHANNON ENTROPY
    # bits = entropy.Result(project.molecules)
    
    # Para exibição de cada ciclo
    print( '\nCYCLE: ',cycle )
    print('AFF: %.4f        AMOUNT: %i' %(project.all_affinity[cycle], project.all_amount[cycle]))
    # print('BITS: %.4f       SIZE: %.2f' %(bits, project.all_averageSize[cycle]))
    print('TANK: %d         BASE: %d' %(project.tank, project.all_base))

    if ( project.all_affinity[cycle] >= 1 ):
        break

    cycle += 1