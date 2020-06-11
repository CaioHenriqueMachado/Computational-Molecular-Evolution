from Classe_RNA         import Selex
from Classe_Filtro      import Filtro
from Classe_Equação     import Equação
from Classe_Entropia    import ShannonEntropy


# QUANTITY OF MOLECULES
mols = 2

# MOLECULES SIZE
tam = 10

# MUTATION RATE(%):
alpha = 10

# FILTER EFFICIENCY(%):
beta = 60

# TARGET
target = 5

# CYCLES LIMIT
cycles_limit = 500

# MOLECULES LIMIT
molecules_limit = 500




project = Selex( mols, tam, target)

entropy = ShannonEntropy()


# GENERATION OF INITIAL MOLECULES
project.Generator()


cycle = 0

#AQUI VAI DAR ERRO PORQUE NÃO TEM NADA NA POSIÇÃO 0 DA AFINIDADE#
while( project.amount_aff[cycle] < 1 and cycle < cycles_limit ):
    # REPLICATION WITH MUTATION RATE(%)
    project.PolymeraseChainReaction(alpha)

    # LIMITATION OF MOLECULES(%)
    project.ConstantPopulation(molecules_limit)

    # MOLECULES SELECTION
    project.Filter(beta)

    # SHANNON ENTROPY
    bits = entropy.Result(project.molecules)
    cycle += 1


#Gerando as primeiras moleculas:

# moleculas_1G , afinidade_1G = moleculas.Gerar( mol, tam, alvo )
# m_gerais = moleculas_1G
# NA = afinidade_1G*(len(moleculas_1G))
# NB =( len( moleculas_1G ) ) - NA

# while( afinidade < 1 and ciclo < limite ):
    #Para replicação
    # m_duplicadas = moleculas.PCR( m_gerais, alfa )
     
    #Para Constant Population
    # m_ordenadas = moleculas.CP( m_duplicadas, popMax, alvo )

    #Para Filtragem das moleculas
    # m_filtrada, afinidade, TAM = filtro.seleção( m_ordenadas, alvo, beta )

    #Para Entropia de Shannon
    # bits = entropia.Shannon( m_filtrada )

    #Para Equação de Crescimento
    # QTD_C , AFF_C, NA, NB = calculado.Crescimento( NA, NB, alfa, beta, popMax)

    # QTD = len( m_filtrada )
    # m_gerais = m_filtrada
    # ciclo+= 1

    #Para exibição de cada ciclo
    # print( '\nCiclo: %d'%ciclo )
    # print( 'Simulado:     QTD=%d       AFF:%.4f'%( QTD, afinidade ) )
    # print( 'Calculado:     QTD=%.1f    AFF:%.4f'%( QTD_C , AFF_C )  )
    # print( 'Entropia: %.4f                    TAM: %.1f'%( bits, TAM ) )

