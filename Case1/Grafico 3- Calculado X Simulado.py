from pylab              import *   
from Classe_RNA         import RNA
from Classe_Filtro      import Filtro
from Classe_Equação     import Equação
from Classe_Entropia    import Entropia
#Entrada de dados...
#int(input('Quantidade de molécula:'))
mol = 500
#int(input('Tamanho da molécula:'))
tam = 50
#Taxa de mutação (%):
alfa = 20
#Eficiência de filtro(%):
beta = 60
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-T-C-G}
alvo = 'AAAAA'
#Limite de Rounds:
limite = 1000
#Limite de moléculas:
popMax = 500

#Aplicando classes e funçoes...
moleculas   = RNA()
filtro      = Filtro()
calculado   = Equação()
entropia    = Entropia()
ciclo       = 0
afinidade   = 0

lista_afinidade = [ 0 ]
lista_ciclo     = [ 0 ]
lista_QTD       = [ 0 ]
lista_QTD_C     = [ 0 ]
lista_AFF_C     = [ 0 ]

#Gerando as primeiras moleculas:
moleculas_1G , afinidade_1G = moleculas.Gerar(mol, tam, alvo)
m_gerais = moleculas_1G
NA = afinidade_1G*(len(moleculas_1G))
NB = (len(moleculas_1G)) - NA


while(afinidade < 1 and ciclo < limite ):
    #Para replicação
    m_duplicadas = moleculas.PCR(m_gerais ,alfa)
     
    #Para Constant Population
    m_ordenadas = moleculas.CP(m_duplicadas,popMax,alvo)

    #Para Filtragem das moleculas
    m_filtrada, afinidade, TAM=filtro.seleção(m_ordenadas, alvo, beta)

    #Para Entropia de Shannon
    bits = entropia.Shannon(m_filtrada)

    #Para Equação de Crescimento
    QTD_C , AFF_C, NA, NB = calculado.Crescimento( NA, NB, alfa, beta, popMax)

    QTD = len(m_filtrada)
    m_gerais = m_filtrada
    ciclo+= 1

    #Para exibição de cada ciclo
    print('\nCiclo: %d'%ciclo)
    print('Simulado :     QTD=%d       AFF:%.4f'%(QTD, afinidade))
    print('Calculado:     QTD=%d       AFF:%.4f'%(QTD_C, AFF_C))
    print('Entropia: %f'%bits)


 #Para construção de graficos                                                       <-- Lista de dados
    lista_ciclo.append(ciclo)
    lista_afinidade.append(afinidade)
    lista_QTD.append(QTD)
    lista_QTD_C.append(QTD_C)
    lista_AFF_C.append(AFF_C)

#1--------------------

# Gerando grafico
#Primeiro (Afinidade X Round) 
#Simulado
grafico1_x = lista_ciclo
grafico1_y = lista_afinidade
#Calculado
grafico2_x = lista_ciclo
grafico2_y = lista_AFF_C

plt.rcParams['figure.figsize'] = (8,12)
plt.title('TAXA DE MUTAÇÃO %d --> CALCULADO X SIMULADO'%alfa)
plt.subplot(1,2,1)
plt.plot( grafico1_x , grafico1_y )
plt.plot( grafico2_x , grafico2_y )
plt.xlabel('ROUND')
plt.ylabel('AFINIDADE')
plt.grid(True)

plt.show()

#2--------------------

#Segundo (Qtd_mol X Round) 
#Simulado
grafico3_x = lista_ciclo
grafico3_y = lista_QTD
#Calculado  
grafico4_x = lista_ciclo
grafico4_y = lista_QTD_C

plt.title('TAXA DE MUTAÇÃO %d --> CALCULADO X SIMULADO'%alfa)
plt.subplot(1,2,2)
plt.plot( grafico3_x , grafico3_y )
plt.plot( grafico4_x , grafico4_y )
plt.xlabel('ROUND')
plt.ylabel('QUANTIDADE DE MOLECULAS')
plt.grid(True)

plt.show()


    
