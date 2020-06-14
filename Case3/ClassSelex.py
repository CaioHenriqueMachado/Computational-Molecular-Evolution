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
        self.tank = ( amount * size )
        self.distances = []
        self.all_base = amount * size

    def Generator(self):
        self.molecules = []

        for _ in range( self.amount ) :
            self.molecules.append(Tools().RandomBase(self.size))
            self.tank = 0
    
 
    #DUPLICATING MOLECULE WITH MUTATION/ERROR (POLYMERASE CHAIN REACTION)
    def PolymeraseChainReaction(self, alpha):
        self.alpha = alpha
        new_molecules = []

        for molecule in self.molecules:
            if ( self.tank >= int(len (molecule))):
                self.tank -= int(len(molecule))
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
            else:
                break

        self.molecules = self.molecules + new_molecules
        # self.distances = Tools().CalculateDistance(self.molecules)
        
        
        
    # BREAKING MOLECULES 
    def Break(self, codon_break, prob_break):
        self.codon_break = codon_break
        self.prob_break = prob_break
        current_molecules = []
        for molecule in self.molecules:
            if ( molecule.count(codon_break) == 0 ):
                current_molecules.append(molecule)
            else:
                if ( prob_break < random.randint(1,100) ):
                    current_molecules.append(molecule)
                else:
                    broken_molecule = molecule[0:(molecule.index(codon_break) - 1)]
                    if ( len(broken_molecule) >= len(self.target) ):
                        current_molecules.append(broken_molecule)
                        self.tank += (len(molecule) - len(broken_molecule))
                    else:
                        self.tank += len(molecule)
        self.molecules = current_molecules

    # JOINING MOLECUES
    def Join(self, prob_join):
        self.prob_join = prob_join
        NA = []
        NI = []
        Q_NA = 0
        Q_NI = 0
        for molecule in self.molecules:
            if ( molecule.count(self.target) > 0 and molecule.count(self.ant_target) > 0):
                NA.append(0)
                NI.append(0)
            elif (molecule.count(self.target) > 0):
                NA.append(1)
                NI.append(0)
                Q_NA += 1
            elif ( molecule.count(self.ant_target) > 0 ):
                NA.append(0)
                NI.append(1)
                Q_NI += 1
            else:
                NA.append(0)
                NI.append(0)

        for i in range(len(self.molecules)):
            if (NA[i] == 1 and prob_join < (random.randint(1,100))):
                NA[i] = 0
                Q_NA -= 1
  
        joins=min( Q_NA , Q_NI )
                        
        for _ in range(joins):
            i=0
            j=0
            while ( NA[i] != 1 ):
                i+=1
            while( NI[j] != 1):
                j+=1

            aux = self.molecules[j]
            self.molecules[i] += aux
            self.molecules[j] = 0
            NA[i] = 0
            NI[j] = 0

        aux=[]
        for i in range(len(self.molecules)):
            if (self.molecules[i] == 0):
                aux.append(i)

        aux.sort(reverse=True)

        for i in aux:
            del(self.molecules[i])
            # del(self.distances[i])
        

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
        tam_padrão = self.size * 0.02 * self.alpha
        filtered_molecules = []
        filtered_distances = []
        i=0
        for molecule in self.molecules:
            efficiency_percentage = random.randint( 1,100 )
            if ( molecule.count(self.target) > 0 or efficiency_percentage > self.beta):
                # if ( self.distances[i] <= tam_padrão ):
                filtered_molecules.append(molecule)
                # filtered_distances.append(self.distances[i])
                # else:
                #     self.tank += len(molecule)
            else:
                self.tank += len(molecule)
            i+=1
        self.molecules = filtered_molecules
        # self.distances = filtered_distances
        self.all_affinity.append(Tools().Affinity(self.target, self.molecules))
        self.all_amount.append(len(self.molecules))
        self.all_averageSize.append(Tools().AverageSize(self.molecules))
        self.all_base = (Tools().CalculateBase(self.molecules, self.tank))

    
    

class Tools:
    def RandomBase(self, amount):
        amount = int(amount)
        bases = [ "A", "T", "C", "G" ]
        self.sequence = ''
        for _ in range(amount):
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
    
    # CALCULATING DISTANCE
    def DistanceLevenshtein(self, a, b):
        if not a: return len(b)
        if not b: return len(a)
        return min(Tools().DistanceLevenshtein(a[1:], b[1:])+(a[0] != b[0]), Tools().DistanceLevenshtein(a[1:], b)+1, Tools().DistanceLevenshtein(a, b[1:])+1)
    
    def CalculateDistance(self, molecules):
        # valor = len(molecules) 
        # valor = int(valor / 2)
        # distance = []
        # for i in range(valor):
        #     a = molecules[i]
        #     b = molecules[ valor + i ]
        #     distance.append((Tools().DistanceLevenshtein(a, b)))
        # return (distance + distance)
        pass

    def CalculateBase(self, molecules, tank):
        result = tank
        for molecule in molecules:
            result +=len(molecule)
        return result

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
 - Uma molecula com TARGET e ANT-TARGET não tem chance de juntar novamente.
Opções não exploradas:
 - Uma molecula com TARGET e ANT-TARGET pode se juntar com uma não afim.
 - Uma molecula com TARGET e ANT-TARGET pode se juntar com uma afim.
 - Uma molecula com TARGET e ANT-TARGET ter menas chances de sair do que as outras

DISTANCE:
Aplicado:
 - Está tendo mudança na distancia nos momentos de: Replicação, quebra, junção e filtragem.
 - Uma molecula tem chance de sair de tiver 2x vezes mais mudanças do que a mutação pode fazer.
Opções não exploradas:
 - Adicionar a mudança quando uma molecula quebra, ou quando tem uma junção(Se pensar bem, acaba sendo um erro.
e não irá passar do filtro pois a distancia irá aumentar muito.)
'''





