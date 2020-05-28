#Importando classes...
from pylab import *   
from Classe_RNA import RNA
from Classe_Filtro import Filtro
from Classe_Entropia import Entropia
from Classe_Distancia import Distancia

#Entrada de dados...
mol=500#int(input('Quantidade de molécula:'))
tam=100#int(input('Tamanho da molécula:'))

#Taxa de mutação (%):
alfa=10
#Eficiência de filtro(%):
beta=90
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-T-C-G}
alvo= 'AAAAA' 
#GENE DE JUNÇÃO
seq_j='TCTCT'
#GENE DE JUNÇÃO
prob_j=10
#GENE DE QUEBRA:
seq_q='GG'
#PROBABILIDADE DE QUEBRA:
prob_q=10
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

lista_afinidade=[0]
lista_ciclo=[0]
lista_tamanho=[100]
lista_QTD=[500]
lista_entropia=[2]


#Para as primeiras moleculas
moleculas_1G , mutaçoes_1G , distancia_1G,  NA= moleculas.gerar_e_mutar(mol, tam, alfa, alvo)
m_gerais=mutaçoes_1G
d_gerais=distancia_1G


#Inicio do ciclo...
betax=beta
beta= 80
while(afinidade <1 and   ciclo< limite ):
    
    if ciclo%10 == 0 and beta < betax:
        beta+=1
    
    #Para replicação:
    m_duplicadas, Reservatório , replicas=moleculas.PCR(m_gerais, alfa,Reservatório)
    d_duplicadas=distancia.D_Hamming(m_duplicadas , d_gerais, replicas)

    #Para quebra de molécula                                                       
    m_quebradas , d_quebradas, Reservatório=moleculas.Quebra(m_duplicadas, d_duplicadas, Reservatório,seq_q,prob_q)

    #Para junção de molécula
    m_juntadas, d_juntadas=moleculas.Junção(m_quebradas,d_quebradas , alvo , seq_j,prob_j)
    
    #Para Filtragem das moleculas
    m_filtrada , d_filtrada, afinidade, TAM,Reservatório=filtro.seleção(m_juntadas, d_juntadas, alvo,alfa, beta, Reservatório,tam)

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
    print('QTD=%d               AFF:%.4f'%(QTD, afinidade))
    print('Entropia: %.4f       TAM: %.1f'%(bits,TAM))
    print('Bases: %d            Resevatório:%d'%(qtd_por_ciclo, Reservatório))
    print('BETA: %d'%beta)


#Para construção de graficos                                                       <-- Lista de dados
    lista_ciclo.append(ciclo)
    lista_afinidade.append(afinidade*100)
    lista_entropia.append(bits)
    lista_tamanho.append(TAM)                                                                                                                      #Tamanho fixo da molecula
    lista_QTD.append(QTD)
    
# Gerando 4 graficos 
    
#Primeiro (Afinidade X Ciclo) 
    
grafico1_x = lista_ciclo
grafico1_y = lista_afinidade 

plt.rcParams['figure.figsize'] = (12,8)

plt.subplot(2,2,1)
plt.title('AFINIDADE (mol. afins)')
plt.plot( grafico1_x , grafico1_y, c='#ff0000',lw=3)
plt.xlabel('Ciclo/Round')
plt.ylabel('Afinidade(%)')

plt.grid(True)

#Segundo (QTD_moleculas X Ciclo)   
grafico2_x = lista_ciclo
grafico2_y = lista_QTD

plt.subplot(2,2,2)
plt.title('QUANTIDADE DE MOLÉCULAS')
plt.plot( grafico2_x , grafico2_y, c='#ff0000',lw=3)
plt.xlabel('Ciclo/Round')
plt.ylabel('QTD_moléculas')
plt.grid(True)

#Terceiro (Entropia X Ciclo)   
grafico3_x = lista_ciclo
grafico3_y = lista_entropia 

plt.subplot(2,2,3)
plt.title('ENTROPIA MÉDIA DAS MOLÉCULAS (Bits)')
plt.plot( grafico3_x , grafico3_y, c='#ff0000',lw=3 )
plt.xlabel('Ciclo/Round')
plt.ylabel('Entropia')
plt.grid(True)

#Quarto (Tamanho medio X Ciclo)   
grafico4_x = lista_ciclo
grafico4_y = lista_tamanho

plt.subplot(2,2,4)
plt.title('TAMANHO MÉDIO DAS MOLÉCULAS (Base)')
plt.plot( grafico4_x , grafico4_y, c='#ff0000',lw=3 )
plt.xlabel('Ciclo/Round')
plt.ylabel('Tamanho Médio')
plt.grid(True)


plt.show()
