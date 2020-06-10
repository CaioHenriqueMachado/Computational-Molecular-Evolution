import random

class Selex:
    def __init__(self, amount, size, size_target):
        self.amount = amount
        self.size = size
        self.size_target = size_target
        self.target = ''
        self.target = Base(self.size_target).Random()
        print('TARGET:' + self.target)


    def Generator(self):
        self.molecules = []
        self.amount_aff = 0
        for i in range( self.amount ) :
            self.molecules.append(Base(self.size).Random())
        print(self.molecules)
    
        #MOLECULE COUNTER WHITH AFFINITY
        for molecule in self.molecules:
            if ( molecule.count(self.target) ):
                self.amount_aff +=1


    #DUPLICATING MOLECULE WITH MUTATION/ERROR (POLYMERASE CHAIN REACTION)
    def PolymeraseChainReaction(self, alpha):
        self.alpha = alpha
        amount_current = len(self.molecules)
        if (amount_current == self.amount + 1):     #FOR FIRST CYCLE (Depois passar ciclo no parametros e colocar if clico ==1)
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
                        new_base = Base(1).Random()
                        while( new_base == molecule[j] ):                                                
                            new_base = Base(1).Random()

                        new_molecule+= new_base

                new_molecules.append( new_molecule )
            self.molecules = self.molecules + new_molecules
            print(self.molecules)

    #LIMITING THE AMOUNT OF MOLECULES
    def ConstantPopulation(self, max_pop):
        amount_current = len(self.molecules)
        CP = []

        while ( amount_current > max_pop ):
            i = random.randint( 0, ( amount_current ) -1 )
            del( self.molecules[i] )
            amount_current = len(self.molecules)
        print(self.molecules)

class Base:
    def __init__(self, amount):
        amount = int(amount)
        bases = [ "A", "T", "C", "G" ]
        self.sequence = ''
        for i in range(amount):
            self.sequence+=  random.choice(bases)

    def Random(self):
        return self.sequence

'''
NOTAS DO DIA 09/06/2020

MUTAÇÃO:
Três opções a serem seguidas:
 - Se a molécula não sofrer mutação, não muda nada na molécula. Se ela sofrer mutação, aplicar o mesmo % em cada nucleotideo da molécula.
 - Se a molécula não sofrer mutação, não muda nada na molécula. Se ela sofrer mutação, aplicar um % diferente em cada nucleotideo da molécula.
 - Aplicar percentual de mutação em cada nucleotideo da molécula.(APLICADO)

FUNÇÃO PCR:
 - O percentual de mutação NÃO aceita que um nucleotideo mudado tenha chance de mudar para ele mesmo. Exemplo: T mudar para T.

'''
