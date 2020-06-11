from pylab              import *   
from Classe_RNA         import RNA
from Classe_Filtro      import Filtro
from Classe_Entropia    import Entropia


# NESSE CÓDIGO A INTENÇÃO FOI GERAR 4 VEZES PARA VER AS 4 LINHAS EM CADA GRAFICOS
#int(input('Quantidade de molécula:'))
mol = 500
#int(input('Tamanho da molécula:'))
tam = 50
#Taxa de mutação (%):
alfa = 10
#Eficiência de filtro(%):
beta = 85
#Gene Alvo:        (não é necessario ser 5 bases) Escolher entre {A-T-C-G}
alvo = 'AAAAA'
#Limite de Rounds:
limite = 1000
#Limite de moléculas:
popMax = 500

#Aplicando classes e funçoes...
moleculas   = RNA()
filtro      = Filtro()
entropia    = Entropia()
ciclo       = 0
afinidade   = 0

lista_afinidade  = [ 0 ]
lista_afinidade2 = [ 0 ]
lista_afinidade3 = [ 0 ]
lista_afinidade1 = [ 0 ]

lista_ciclo     =[ 0 ]
lista_tamanho   =[ 50 ]

lista_QTD  = [ 0 ]
lista_QTD2 = [ 0 ]
lista_QTD3 = [ 0 ]
lista_QTD1 = [ 0 ]


lista_entropia  = [ 2 ]
lista_entropia2 = [ 2 ]
lista_entropia3 = [ 2 ]
lista_entropia1 = [ 2 ]

for i in range(1,5):
    ciclo = 0
    afinidade = 0
    
    #Gerando as primeiras moleculas:
    moleculas_1G , afinidade_1G = moleculas.Gerar(mol, tam, alvo)
    m_gerais = moleculas_1G
    NA = afinidade_1G*(len(moleculas_1G))
    NB =(len(moleculas_1G)) - NA

    while(afinidade < 1 and ciclo < limite ):
        #Para replicação
        m_duplicadas = moleculas.PCR(m_gerais ,alfa)
         
        #Para Constant Population
        m_ordenadas = moleculas.CP(m_duplicadas,popMax,alvo)
        m_filtrada = m_ordenadas
        #Para Filtragem das moleculas
        for xz in range(i): 
            m_filtrada, afinidade, TAM = filtro.seleção(m_filtrada, alvo, beta)
    
        #Para Entropia de Shannon
        bits = entropia.Shannon(m_filtrada)

    
        QTD = len(m_filtrada)
        m_gerais = m_filtrada
        ciclo+= 1
    
        #Para exibição de cada ciclo
        print('\nCiclo: %d'%ciclo)
        print('Simulado:     QTD=%d       AFF:%.4f'%(QTD, afinidade))
        print('Entropia: %f'%bits)


        #Para construção de graficos                                                       <-- Lista de dados
        if (i == 1):
            lista_ciclo.append(ciclo)
            lista_afinidade.append(afinidade*100)
            lista_entropia.append(bits)
            lista_tamanho.append(TAM)                                                                                                                     
            lista_QTD.append(QTD)
        if (i == 2):
            lista_afinidade1.append(afinidade*100)
            lista_entropia1.append(bits)                                                                                                                   
            lista_QTD1.append(QTD)
        if (i == 3):
            lista_afinidade2.append(afinidade*100)
            lista_entropia2.append(bits)                                                                                                    
            lista_QTD2.append(QTD)
        if (i == 4):
            lista_afinidade3.append(afinidade*100)
            lista_entropia3.append(bits)
            lista_QTD3.append(QTD)
            
 


# Gerando 4 graficos 
    
#Primeiro (Afinidade X Ciclo) 
    
grafico1_x = lista_ciclo

grafico1_y = lista_afinidade

grafico1_1_y = lista_afinidade1 
grafico1_2_y = lista_afinidade2 
grafico1_3_y = lista_afinidade3 
   

plt.rcParams['figure.figsize'] = (12,8)

plt.subplot(2,2,1)
plt.title('AFINIDADE (mol. afins)')
plt.plot( grafico1_x , grafico1_y, c='b',lw=3)
plt.plot( grafico1_x , grafico1_1_y, c='g',lw=3)
plt.plot( grafico1_x , grafico1_2_y, c='r',lw=3)
plt.plot( grafico1_x , grafico1_3_y, c='y',lw=3)
plt.xlabel('Ciclo/Round')
plt.ylabel('Afinidade(%)')

plt.grid(True)

#Segundo (QTD_moleculas X Ciclo)   
grafico2_x = lista_ciclo

grafico2_y = lista_QTD
grafico2_1_y = lista_QTD1
grafico2_2_y = lista_QTD2
grafico2_3_y = lista_QTD3

plt.subplot(2,2,2)
plt.title('QUANTIDADE DE MOLÉCULAS')
plt.plot( grafico2_x , grafico2_y, c='b',lw=3)
plt.plot( grafico2_x , grafico2_1_y, c='g',lw=3)
plt.plot( grafico2_x , grafico2_2_y, c='r',lw=3)
plt.plot( grafico2_x , grafico2_3_y, c='y',lw=3)
plt.xlabel('Ciclo/Round')
plt.ylabel('QTD_moléculas')
plt.grid(True)

#Terceiro (Entropia X Ciclo)   
grafico3_x = lista_ciclo

grafico3_y = lista_entropia 
grafico3_1_y = lista_entropia1 
grafico3_2_y = lista_entropia2
grafico3_3_y = lista_entropia3 

plt.subplot(2,2,3)
plt.title('ENTROPIA MÉDIA DAS MOLÉCULAS (Bits)')
plt.plot( grafico3_x , grafico3_y, c='b',lw=3 )
plt.plot( grafico3_x , grafico3_1_y, c='g',lw=3 )
plt.plot( grafico3_x , grafico3_2_y, c='r',lw=3 )
plt.plot( grafico3_x , grafico3_3_y, c='y',lw=3 )         
plt.xlabel('Ciclo/Round')
plt.ylabel('Entropia')
plt.grid(True)

#Quarto (Tamanho medio X Ciclo)   
grafico4_x = lista_ciclo
grafico4_y = lista_tamanho
grafico4_1_y = lista_tamanho
grafico4_2_y = lista_tamanho
grafico4_3_y = lista_tamanho

plt.subplot(2,2,4)
plt.title('TAMANHO MÉDIO DAS MOLÉCULAS (Base)')
plt.plot( grafico4_x , grafico4_y, c='b',lw=3 )
plt.plot( grafico4_x , grafico4_1_y, c='g',lw=3 )
plt.plot( grafico4_x , grafico4_2_y, c='r',lw=3 )
plt.plot( grafico4_x , grafico4_3_y, c='y',lw=3 )
plt.xlabel('Ciclo/Round')
plt.ylabel('Tamanho Médio')
plt.grid(True)

plt.show()
