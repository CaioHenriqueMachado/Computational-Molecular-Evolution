from Classe_RNA import RNA
from Classe_Filtro import Filtro
from Classe_Equação import Equação
from Classe_Entropia import Entropia

#Entrada de dados...
mol=500#int(input('Quantidade de molécula:'))
tam=50#int(input('Tamanho da molécula:'))
#Taxa de mutação (%):
alfa=0
#Eficiência de filtro(%):
beta=80
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-U-C-G}
alvo= 'CCCCC'
#Gene Inverso:        (não é necessario por nada, a nao ser que queira escolher uma seq. para o gene de ligação
inverso= ''

#Limite de Rounds:
limite=500
#Limite de moléculas:
popMax=500

#Aplicando classes e funçoes...
moleculas=RNA()
filtro=Filtro()
calculado=Equação()
entropia=Entropia()
ciclo=0
afinidade=0


#Gerando as primeiras moleculas:
moleculas_1G , afinidade_1G= moleculas.Gerar(mol, tam, alvo)
m_gerais=moleculas_1G
NA= afinidade_1G*(len(moleculas_1G))
NB=(len(moleculas_1G)) - NA


while(afinidade <1 and ciclo< limite ):
    #Para replicação
    m_duplicadas=moleculas.PCR(m_gerais ,alfa)
    
    #Para quebra de molécula                                                       Quebra todas as moleculas possiveis.
    m_quebradas=moleculas.Quebra(m_duplicadas)

    #Para junção de molécula
    m_juntadas=moleculas.Junção(m_quebradas , alvo , inverso)

    #Para Constant Population
    m_ordenadas = moleculas.CP(m_juntadas, popMax, alvo)

    #Para Filtragem das moleculas
    m_filtrada, afinidade, TAM=filtro.seleção(m_ordenadas, alvo, beta)

    #Para Entropia de Shannon
    bits=entropia.Shannon(m_filtrada)

    #Para Equação de Crescimento
    QTD_C , AFF_C, NA, NB=calculado.Crescimento( NA, NB, alfa, beta, popMax)

    QTD= len(m_filtrada)
    m_gerais = m_filtrada
    ciclo+=1

    #Para exibição de cada ciclo
    print('\nCiclo: %d'%ciclo)
    print('Simulado :     QTD=%d       AFF:%.4f'%(QTD, afinidade))
    print('Calculado:     QTD=%.1f    AFF:%.4f'%(QTD_C , AFF_C)  )
    print('Entropia: %.4f                    TAM: %.1f'%(bits,TAM))












    
