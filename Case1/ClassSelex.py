import random

class Selex:
    def __init__(self, amount, size, size_target):
        self.cylcle = 0
        self.amount = amount
        self.all_affinity = [0]
        self.all_amount = [amount]
        self.all_averageSize = [size]
        self.size = size
        self.size_target = size_target
        self.target = ''
        self.target = Tools().RandomBase(self.size_target)

    def Generator(self):
        self.molecules = []

        for i in range( self.amount ) :
            self.molecules.append(Tools().RandomBase(self.size))
    
 
    #DUPLICATING MOLECULE WITH MUTATION/ERROR (POLYMERASE CHAIN REACTION)
    def PolymeraseChainReaction(self, alpha):
        self.alpha = alpha
        new_molecules = []

        for molecule in self.molecules:
            new_molecule = ""
            for j in range(len(molecule)):
                mutation_percentage = random.randint( 1,100 )
                if ( mutation_percentage >= alpha):
                    new_molecule+= molecule[j]
                else:
                    new_base = Tools().RandomBase(1)
                    while( new_base == molecule[j] ):                                                
                        new_base = Tools().RandomBase(1)

                    new_molecule+= new_base
                    
            new_molecules.append( new_molecule )

        self.molecules = self.molecules + new_molecules
        

    #LIMITING THE AMOUNT OF MOLECULES
    def ConstantPopulation(self, max_pop):
        amount_current = len(self.molecules)

        while ( amount_current > max_pop ):
            i = random.randint( 0, ( amount_current ) -1 )
            del( self.molecules[i] )
            amount_current = len(self.molecules)

    
    #Filtrando moléculas com base na eficiencia de filtro
    def Filter(self, beta):
        self.beta = beta
        molecule_affinity = []
        for molecule in self.molecules:
            efficiency_percentage = random.randint( 1,100 )
            if ( molecule.count(self.target) > 0 or efficiency_percentage > self.beta ): 
                molecule_affinity.append(molecule)
        self.molecules = molecule_affinity

        self.all_affinity.append(Tools().Affinity(self.target, self.molecules))
        self.all_amount.append(len(self.molecules))
        self.all_averageSize.append(Tools().AverageSize(self.molecules))
    

class Tools:
    def RandomBase(self, amount):
        amount = int(amount)
        bases = [ "A", "T", "C", "G" ]
        self.sequence = ''
        for i in range(amount):
            self.sequence+=  random.choice(bases)
        return self.sequence

    #COUNTER AFFINITY FOR CYCLO
    def Affinity(self, target, molecules):
        affinity = 0
        for molecule in molecules:
            if ( molecule.count(target) ):
                affinity += 1
        affinity = affinity / len(molecules)
        return affinity

    #AVERAGE SIZE
    def AverageSize(self,molecules):
        size_molecule = 0
        average = 0
        for molecule in molecules:
            size_molecule += len(molecule)
        average = size_molecule / len(molecules)
        return average


# instance = Selex(  2, 10, 5)
# instance.Generator()

#Com Taxa de mutação (%):
# instance.PolymeraseChainReaction(100)

#Limite de moléculas:
# instance.ConstantPopulation(500)

# instance.Filter(100)
# print('TEST')
# print(instance.all_aff)

'''
NOTAS:

MUTAÇÃO:
Três opções a serem seguidas:
 - Se a molécula não sofrer mutação, não muda nada na molécula. Se ela sofrer mutação, aplicar o mesmo % em cada nucleotideo da molécula.
 - Se a molécula não sofrer mutação, não muda nada na molécula. Se ela sofrer mutação, aplicar um % diferente em cada nucleotideo da molécula.
 - Aplicar percentual de mutação em cada nucleotideo da molécula.(APLICADO)

FUNÇÃO PCR:
 - O percentual de mutação NÃO aceita que um nucleotideo mudado tenha chance de mudar para ele mesmo. Exemplo: T mudar para T.


FILTRO:
Opções:
 - O filtro é aplicado somente para as moléculas não afins.Moléculas não afins tem % Beta de SAIR do ciclo(APLICADO)
 - As moleculas afim pode ter mais chances de ficar.
'''