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