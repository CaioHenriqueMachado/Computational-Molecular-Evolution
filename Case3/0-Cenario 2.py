#Importando classes...
from Classe_RNA import RNA
from Classe_Filtro import Filtro
from Classe_Entropia import Entropia
from Classe_Distancia import Distancia

#Entrada de dados...
mol=500#int(input('Quantidade de molécula:'))
tam=100#int(input('Tamanho da molécula:'))
#Taxa de mutação (%):
alfa=0
#Eficiência de filtro(%):
beta=80
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-U-C-G}
alvo= 'ACTGG'
#Gene Inverso:        (não é necessario por nada, a nao ser que queira escolher uma seq. para o gene de ligação
inverso= 'TCTG'
#Limite de Rounds:
limite=500

#Reservatório de bases:
Reservatório=0

#Aplicando classes e funçoes...
moleculas=RNA()
distancia=Distancia()
filtro=Filtro()
entropia=Entropia()

ciclo=0
afinidade=0


#Para as primeiras moleculas
moleculas_1G , mutaçoes_1G , distancia_1G,  NA= moleculas.gerar_e_mutar(mol, tam, alfa, alvo)
m_gerais=mutaçoes_1G
d_gerais=distancia_1G


#Inicio do ciclo...
   
while(afinidade <1 and   ciclo< limite ):
    #Para replicação:
    m_duplicadas, Reservatório , replicas=moleculas.PCR(m_gerais, alfa,Reservatório)
    d_duplicadas=distancia.D_Hamming(m_duplicadas , d_gerais, replicas)

    #Para quebra de molécula                                                       
    m_quebradas , d_quebradas, Reservatório=moleculas.Quebra(m_duplicadas, d_duplicadas, Reservatório)

    #Para junção de molécula
    m_juntadas, d_juntadas=moleculas.Junção(m_quebradas,d_quebradas , alvo , inverso)

    #Para Filtragem das moleculas
    m_filtrada , d_filtrada, afinidade, TAM,Reservatório=filtro.seleção(m_juntadas, d_juntadas, alvo, beta, Reservatório)

    #Para entropia de Shannon
    bits=entropia.Shannon(m_filtrada)

    qtd_por_ciclo=Reservatório
    for m in m_filtrada:
        qtd_por_ciclo+=len(m)
    m_gerais = m_filtrada
    d_gerais = d_filtrada
    QTD= len(m_filtrada)
    m_gerais = m_filtrada
    ciclo+=1

    
    #Para exibição de cada ciclo
    print('\nCiclo: %d'%ciclo)
    print('Simulado :     QTD=%d             AFF:%.4f'%(QTD, afinidade))
    print('Entropia: %.4f                    TAM: %.1f'%(bits,TAM))
    print('Bases: %d                         Resevatório:%d'%(qtd_por_ciclo, Reservatório))
    
    




