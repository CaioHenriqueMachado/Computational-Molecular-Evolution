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
        self.target = Tools().RandomBase(self.size_target)
        self.ant_target = Tools().RandomBase(self.size_target)

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
        
    # BREAKING MOLECULES 
    def Break(self, codon_break, prob_break): #< --- PASSAR Break('TTT', 10)
        self.codon_break = codon_break
        self.prob_break = prob_break
        current_molecules = []
        for molecule in self.molecules:
            if ( molecule.count(codon_break) == 0 ):
                current_molecules.append(molecule)
            else:
                if ( prob_break <= random.randint(1,100) ):
                    current_molecules.append(molecule)
                else:
                    broken_molecule = molecule[0:(molecule.index(codon_break) - 1)]
                    if ( len(broken_molecule) >= len(self.target) ):
                        current_molecules.append(broken_molecule)
        self.molecules = current_molecules

    # JOINING MOLECUES
    def Join(self):
        NA = []
        NI = []
        for molecule in self.molecules:
            if ( molecule.count(self.target) > 0 ):
                NA.append(1)
            else:
                NA.append(0)
            if ( molecule.count(self.ant_target) > 0 ):
                NI.append(1)
            else:
                NI.append(0)




    # LIMITING THE AMOUNT OF MOLECULES
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


BREAK(QUEBRA):
Aplicado:
 - Se localizar o stop codon TTT ele quebra a molecula e apaga do TTT em diante.
 - Se a molecula é menor que o TARGET ele não entra pois não tem chance de ser afim.
Opções não exploradas:
 - Ao quebrar em duas partes, adicionar as duas partes no ciclo(Cuidado: tende a ter mais moléculas não afins)
 - Manter um limite minimo que uma molecula pode ter.
 - Escolher a parte que vai ficar no ciclo.

JOIN:
Aplicado:
 - Junta uma molecula que tem TARGET e uma ANT-TARGET. sendo ela, gerado aleatoriamente e no mesmo tamanho que a TARGET
'''



#JUNÇÃO DE MOLÉCULAS---------(Usando a junção 2)--------------------------------------------------------------------------------------------------------
class ewwe():
    def Junção(self, moleculas, alvo, inverso):
        if (inverso == ''):
            for base in alvo:
                if (base == 'A'):
                    inverso+='T'
                if (base == 'T'):
                    inverso+='A'
                if (base == 'C'):
                    inverso+='G'
                if (base == 'G'):
                    inverso+='C'
        # Para Localizar Moléculas com gene Alvo
        NA=[]
        QTD_NA=0
        for gene in moleculas:
            QTD=len(gene)
            i=0
            afins=0  
            while ((i+len(alvo)-1) < QTD):
                condição=True
                j=0
                while (j < len(alvo)):
                    condição= gene[i+j] == alvo[j]
                    j+=1
                    if (condição == False):
                        j=0
                        break
                if (j == len(alvo)):
                    afins+=1
                    break
                i+=1
            if (afins > 0):                                          
                NA.append(1)
                QTD_NA+=1
            else:
                NA.append(0)

        #Para Localizar Moléculas com genes Inverso
        NI=[]
        QTD_NI=0
        for gene in moleculas:
            QTD=len(gene)
            i=0
            afins=0  
            while ((i+len(inverso)-1) < QTD):
                condição=True
                j=0
                while (j < len(inverso)):
                    condição= gene[i+j] == inverso[j]
                    j+=1
                    if (condição == False):
                        j=0
                        break
                if (j == len(inverso)):
                    afins+=1
                    break
                i+=1
            if (afins > 0):                                          
                NI.append(1)
                QTD_NI+=1
            else:
                NI.append(0)
        
        for i in range(len(moleculas)):
            if (NA[i] == 1 and NI[i] == 1):
                NA[i]=1                             #Se uma molécula tem os 2 genes,se (NA[i]=1  E  NI[i]=0) ela se juntará com uma não afim.
                NI[i]=0                             #Se uma molécula tem os 2 genes,se (NA[i]=0  E  NI[i]=1) ela se juntará com uma afim.
                QTD_NA-=0                           #Se (NA[i]=0) colocar   (QTD_NA-= 1)
                QTD_NI-=1                           #Se (NI[i]=0) colocar   (QTD_NI-= 1)

        x=5                                        #Probabilidade de haver junção.
        for i in range(len(moleculas)):
            if (NA[i] == 1 and x < (random.randint(1,100))):
                NA[i]=0
                QTD_NA-=1
                QTD_NI-=1
                

        junções=min( QTD_NA , QTD_NI )
                        
        for z in range(junções):
            i=0
            j=0
            while ( NA[i] != 1 ):
                i+=1
            while( NI[j] !=1):
                j+=1

            aux=moleculas[j]
            moleculas[i]+=aux
            moleculas[j]=0
            NA[i]=0
            NI[j]=0

        aux=[]
        for i in range(len(moleculas)):
            if (moleculas[i] == 0):
                aux.append(i)

        aux.sort(reverse=True)

        for i in aux:
            del(moleculas[i])
                

        return moleculas
