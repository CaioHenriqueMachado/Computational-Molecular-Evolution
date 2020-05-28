from pylab import *   
from Classe_RNA import RNA
from Classe_Filtro import Filtro
from Classe_Equação import Equação
from Classe_Entropia import Entropia
#Entrada de dados...
mol=500#int(input('Quantidade de molécula:'))
tam=50#int(input('Tamanho da molécula:'))
#Taxa de mutação (%):
alfa=5
#Eficiência de filtro(%):
beta=90
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-T-C-G}
alvo= 'ACTGA'
#Gene Inverso:        (não é necessario por nada, a nao ser que queira escolher uma seq. para o gene de ligação
inverso= ''
#Limite de Rounds:
limite=1000
#Limite de moléculas:
popMax=500

#Aplicando classes e funçoes...
moleculas=RNA()
filtro=Filtro()
calculado=Equação()
entropia=Entropia()
ciclo=0
afinidade=0

lista_afinidade=[0]
lista_ciclo=[0]
lista_tamanho=[50]
lista_QTD=[0]
lista_entropia=[2]

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
    m_ordenadas = moleculas.CP(m_juntadas,popMax, alvo)

    #Para Filtragem das moleculas
    m_filtrada, afinidade,TAM=filtro.seleção(m_ordenadas, alvo, beta)

    #Para Entropia de Shannon
    bits=entropia.Shannon(m_filtrada)

    #Para Equação de Crescimento
    QTD_C , AFF_C, NA, NB=calculado.Crescimento( NA, NB, alfa, beta, popMax)

    QTD=len(m_filtrada)
    m_gerais = m_filtrada
    ciclo+=1

    #Para exibição de cada ciclo
    print('\nCiclo: %d'%ciclo)
    print('Simulado :     QTD=%d       AFF:%.4f'%(QTD, afinidade))
    print('Entropia: %.4f              TAM: %.1f'%(bits,TAM))


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

