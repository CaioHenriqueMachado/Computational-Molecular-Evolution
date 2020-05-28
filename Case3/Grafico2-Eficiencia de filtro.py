#Importando classes...
from pylab import *   
from Classe_RNA import RNA
from Classe_Filtro import Filtro
from Classe_Entropia import Entropia
from Classe_Equação import Equação
from Classe_Distancia import Distancia

#Entrada de dados...
mol=int(input('Quantidade de molécula:'))
tam=int(input('Tamanho da molécula:'))

#Taxa de mutação (%):
alfa=10
#Eficiência de filtro(%):
beta=60
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-T-C-G}
alvo= 'AAAAA'
#Limite de Rounds:
limite=100
#Limite de moléculas:
popMax=500

#Aplicando classes e funçoes...
moleculas=RNA()
distancia=Distancia()
filtro=Filtro()
entropia=Entropia()
calculado=Equação()
ciclo=0
afinidade=0

lista_afinidade=[0]
lista_ciclo=[0]
lista_entropia=[2]
lista_tamanho=[50]
lista_QTD=[0]



#Para as primeiras moleculas
moleculas_1G , mutaçoes_1G , distancia_1G,  NA= moleculas.gerar_e_mutar(mol, tam, alfa, alvo)
m_gerais=mutaçoes_1G
d_gerais=distancia_1G
NB=(len(mutaçoes_1G)) - NA


#Inicio do ciclo...

while( afinidade <1 and ciclo< limite ):
    #Para replicação:
    m_duplicadas=moleculas.PCR(m_gerais, alfa)
    d_duplicadas=distancia.D_Hamming(m_duplicadas , d_gerais)

    #Para Constant Population
    m_ordenadas , d_ordenadas= moleculas.CP(m_duplicadas , d_duplicadas ,popMax)

    #Para Filtragem das moleculas
    m_filtrada , d_filtrada, afinidade, TAM=filtro.seleção(m_ordenadas, d_ordenadas, alvo, beta)

    #Para entropia de Shannon
    bits=entropia.Shannon(m_filtrada)

    #Para Equação de Crescimento
    QTD_C , AFF_C, NA, NB=calculado.Crescimento( NA, NB, alfa, beta, popMax)
    

    m_gerais = m_filtrada
    d_gerais = d_filtrada
    QTD= len(m_filtrada)
    m_gerais = m_filtrada
    ciclo+=1

    
    #Para exibição de cada ciclo
    print('\nCiclo: %d'%ciclo)
    print('Simulado :     QTD=%d       AFF:%.4f'%(QTD, afinidade))
    print('Calculado:     QTD=%.1f    AFF:%.4f'%(QTD_C , AFF_C)  )
    print('Entropia: %f'%bits)

 #Para construção de graficos                                                       <-- Lista de dados
    lista_ciclo.append(ciclo)
    lista_afinidade.append(afinidade)
    lista_entropia.append(bits)
    lista_tamanho.append(TAM)                                                                                                                  
    lista_QTD.append(QTD)
 
    
# Gerando 4 graficos 
    
#Primeiro (Afinidade X Ciclo) 
    
grafico1_x = lista_ciclo
grafico1_y = lista_afinidade 

plt.rcParams['figure.figsize'] = (12,8)
plt.title('Eficiencia do Filtro %d'%beta)
plt.subplot(2,2,1)
plt.plot( grafico1_x , grafico1_y )
plt.xlabel('Ciclo/Round')
plt.ylabel('Afinidade')
plt.grid(True)

#Segundo (QTD_moleculas X Ciclo)   
grafico2_x = lista_ciclo
grafico2_y = lista_QTD

plt.title('Eficiencia do Filtro %d'%beta)
plt.subplot(2,2,2)
plt.plot( grafico2_x , grafico2_y )
plt.xlabel('Ciclo/Round')
plt.ylabel('QTD_moleculas')
plt.grid(True)

#Terceiro (Entropia X Ciclo)   
grafico3_x = lista_ciclo
grafico3_y = lista_entropia 

plt.title('Eficiencia do Filtro %d'%beta)
plt.subplot(2,2,3)
plt.plot( grafico3_x , grafico3_y )
plt.xlabel('Ciclo/Round')
plt.ylabel('Entropia')
plt.grid(True)

#Quarto (Tamanho medio X Ciclo)   
grafico4_x = lista_ciclo
grafico4_y = lista_tamanho

plt.title('Eficiencia do Filtro %d'%beta)
plt.subplot(2,2,4)
plt.plot( grafico4_x , grafico4_y )
plt.xlabel('Ciclo/Round')
plt.ylabel('Tamanho Médio')
plt.grid(True)


plt.show()

