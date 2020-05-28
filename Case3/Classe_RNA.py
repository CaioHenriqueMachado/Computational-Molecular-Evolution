import random
class RNA:
    def gerar_e_mutar(self , molecula, tamanho, alfa, alvo):
# PRIMEIRAS MOLECULAS SENDO CRIADAS
        geradas=[]
        for i in range(molecula) :
            bases=["A","T","C","G"]
            sequencia=""
            k=0
            while k<tamanho:
                sequencia+=bases[random.randint(0,3)]
                k+=1                
            geradas.append(sequencia)
#PRIMEIRAS MOLECULAS PASSANDO POR MUTAÇÃO
        taxa_mutação=alfa                                                                 #mutação(%)
        mutaçoes=[]
        
        for j in geradas:
            mutação=''
            for i in j:
                mutada=''
                x=random.randint(1,101)
                if (x >= taxa_mutação):
                    mutação+= i
                else:
                    mutada=bases[random.randint(0,3)]
                    while( i == mutada):
                        mutada=bases[random.randint(0,3)]
                    mutação+=mutada     
            mutaçoes.append(mutação)
        
#ACHANDO DISTANCIA DAS PRIMEIRAS MOLECULAS
        distancia=[]
        for gene1 , gene2 in zip (geradas , mutaçoes) :
            cont=sum(ch1 != ch2 for ch1, ch2 in zip(gene1, gene2))
            distancia.append(cont)   

#Para achar a afinidade do primeiro ciclo:
        NA=0
        for gene in mutaçoes:
            QTD=len(gene)
            i=0
            afins=0  
            while ((i+len(alvo)-1) != QTD):
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
                i+=1
            if (afins > 0):                                          
                NA+=1
        
        return geradas , mutaçoes, distancia ,NA 

#REAÇÃO EM CADEIA DA POLIMERASE(duplicação de molecula com erro/mutação)-----------------------------------------------------------
    def PCR(self , moleculas, alfa, Reservatório):
        bases=["A","T","C","G"]
        replicas=0
        erro=alfa                                                                      #TAXA DE ERRO 
        moleculas_duplicatas=[]
        for j in moleculas:
            if ( Reservatório >=len (j)):
                Reservatório-=len(j)
                replicas+=1
                duplicação=''
                for i in j:
                    duplicada=''
                    x=random.randint(1,100)
                    if (x >= erro):
                         duplicação+= i
                    else:
                        duplicada=bases[random.randint(0,3)]
                        while( i == duplicada):                                                 #Se deixar tirar o comentario dessas linhas, admite que  quando sofre... 
                            duplicada=bases[random.randint(0,3)]                 #...mutação a base não tem chance de ser o que era.
                        duplicação+=duplicada          
                moleculas_duplicatas.append(duplicação)
            else:
                break
        todas_moleculas= moleculas + moleculas_duplicatas
        return todas_moleculas, Reservatório, replicas


#QUEBRA DE MOLÉCULAS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Quebra(self,moleculas, distancias, Reservatório,seq_q,prob_q):
        mol=[]
        erro='--'
        NA=0
        for gene in moleculas:
            if (prob_q < random.randint(1,100)):
                quebra=erro
            else:
                quebra=seq_q
            QTD=len(gene)
            i=0
            afins=0
            aux_mol=''
            original=True
            while ((i+len(quebra)-1) != QTD):
                condição=True
                j=0
                while (j < len(quebra) ):
                    condição= gene[i+j] == quebra[j]
                    j+=1
                    if (condição == False):
                        j=0
                        break
                if (j==len(quebra)):
                    stopcodon=i+j#-(len(quebra))#-(len(quebra))#STOP CONDON
                    for x in range(stopcodon):
                        aux_mol+=gene[x]
                    mol.append(aux_mol)
                    original=False
                    break
                i+=1
            if(original==True):
                mol.append(gene)
    #JOGANDO A PARTE QUEBRADA NO RESERVATÓRIO
        for original, quebrada in zip (moleculas, mol):
            if (len(original) != len(quebrada)):
                Reservatório+=(len(original) - len(quebrada))
            
    #ACHANDO DISTANCIA DAS MOLECULAS
        def lev(a, b):
            if not a: return len(b)
            if not b: return len(a)
            dis=0
            for i in range(max(len(a),len(b))):
                if (i == min(len(a),len(b))):
                    break
                if (a[i] != b[i]):
                    dis+=1
            dis+=((max(len(a),len(b))) - (min(len(a),len(b))))
            return dis

        for i in range(len(mol)):
            distancias[i]=lev(mol[i],moleculas[i])

    #FOI CONSIDERADO TAMANHO MINIMO DE UMA MOLÉCULA = 10 
        deletar=[]
        for i in range(len(mol)):
            if (len(mol[i]) <10):
                deletar.append(i)

        deletar.sort(reverse=True)

        for i in deletar:
            Reservatório+=len(mol[i])
            del(mol[i])
            del(distancias[i])
        
        return mol, distancias, Reservatório

#JUNÇÃO DE MOLÉCULAS-----------------------------------------------------------------------------------------------------------------
    def Junção(self, moleculas, distancias, alvo, seq_j, prob_j):

        #Para Localizar Moléculas com gene Alvo
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
            while ((i+len(seq_j)-1) < QTD):
                condição=True
                j=0
                while (j < len(seq_j)):
                    condição= gene[i+j] == seq_j[j]
                    j+=1
                    if (condição == False):
                        j=0
                        break
                if (j == len(seq_j)):
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
                NA[i]=0                             #Se uma molécula tem os 2 genes,se (NA[i]=1  E  NI[i]=0) ela se juntará com uma não afim.
                NI[i]=0                             #Se uma molécula tem os 2 genes,se (NA[i]=0  E  NI[i]=1) ela se juntará com uma afim.
                QTD_NA-=1                           #Se (NA[i]=0) colocar   (QTD_NA-= 1)
                QTD_NI-=1                           #Se (NI[i]=0) colocar   (QTD_NI-= 1)

                                       
        for i in range(len(moleculas)):
            if (NA[i] == 1 and prob_j < (random.randint(1,101))):   #Probabilidade de haver junção.
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

            moleculas[i]+=moleculas[j]
            distancias[i]+=len(moleculas[j])
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
            del(distancias[i])
                

        return moleculas,distancias
     

