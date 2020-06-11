import random

class Selex:
    def __init__(self, amount, size, size_target):
        self.amount = amount
        self.size = size
        self.size_target = size_target
        self.target = ''
        self.target = Tools().RandomBase(self.size_target)
        print('TARGET:' + self.target)


    def Generator(self):
        self.molecules = []

        for i in range( self.amount ) :
            self.molecules.append(Tools().RandomBase(self.size))
        print('GENERATOR')
        print(self.molecules)
    
 


    #DUPLICATING MOLECULE WITH MUTATION/ERROR (POLYMERASE CHAIN REACTION)
    def PolymeraseChainReaction(self, alpha):
        self.alpha = alpha
        amount_current = len(self.molecules)
        if (amount_current == self.amount):     #FOR FIRST CYCLE (Depois passar ciclo no parametros e colocar if clico ==1)
            exit
        else:
            for i in range(len(self.molecules)):
                molecule = self.molecules[i]
                new_molecules = []
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
        print('PCR')
        print(self.molecules)

    #LIMITING THE AMOUNT OF MOLECULES
    def ConstantPopulation(self, max_pop):
        amount_current = len(self.molecules)

        while ( amount_current > max_pop ):
            i = random.randint( 0, ( amount_current ) -1 )
            del( self.molecules[i] )
            amount_current = len(self.molecules)
        print('CP')
        print(self.molecules)

    
    #Filtrando moléculas com base na eficiencia de filtro
    def Filter(self, beta):
        self.amount_aff = []
        self.beta = beta
        molecule_affinity = []
        for molecule in self.molecules:
            efficiency_percentage = random.randint( 1,100 )
            if ( molecule.count(self.target) > 0 or efficiency_percentage <= self.beta ): 
                molecule_affinity.append(molecule)
        self.molecules = molecule_affinity

        self.amount_aff.append(Tools().AffinityAmount(self.target, self.molecules))

       

class Tools:
    def RandomBase(self, amount):
        amount = int(amount)
        bases = [ "A", "T", "C", "G" ]
        self.sequence = ''
        for i in range(amount):
            self.sequence+=  random.choice(bases)
        return self.sequence

    #COUNTER AFFINITY FOR CYCLO
    def AffinityAmount(self, target, molecules):
        affinity = 0
        for molecule in molecules:
            if ( molecule.count(target) ):
                affinity += 1
        affinity = affinity / len(molecules)
        return affinity


instance = Selex(  2, 10, 5)
instance.Generator()

#Com Taxa de mutação (%):
instance.PolymeraseChainReaction(100)

#Limite de moléculas:
instance.ConstantPopulation(500)

instance.Filter(100)
print('TEST')
print(instance.amount_aff)

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
 - O filtro é aplicado somente para as moléculas não afins.Moléculas não afins tem % Beta de FICAR no ciclo(APLICADO)
 - As moleculas afim pode ter mais chances de ficar.
'''