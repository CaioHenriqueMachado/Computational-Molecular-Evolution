import random
class RNA:
    def Gerar (self, molecula, tamanho, alvo):
        geradas=[]
        for i in range(molecula) :
            bases=["A","T","C","G"]
            sequencia=""
            k=0
            while k<tamanho:
                sequencia+=bases[random.randint(0,3)]
                k+=1                
            geradas.append(sequencia)
#Para achar a afinidade do primeiro ciclo:
        NA=0
        for gene in geradas:
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
                NA+=1

        afinidade=NA/(len(geradas))
        return geradas, afinidade
#REAÇÃO EM CADEIA DA POLIMERASE(duplicação de molecula com erro/mutação)-----------------------------------------------------------
    def PCR(self , moleculas, alfa):
        bases=["A","T","C","G"]
        mutação=alfa                                                                                                                                 
        moleculas_duplicatas=[]
        
        for j in moleculas:
            
            duplicação=''
            for i in j:
                duplicada=''
                x=random.randint(1,100)
                if (x > mutação):
                     duplicação+= i
                else:
                    duplicada=bases[random.randint(0,3)]
                    while( i == duplicada):                                                 #Se tirar o comentario dessas linhas, admite que  quando sofre... 
                      duplicada=bases[random.randint(0,3)]                 #...mutação a base não tem chance de ser o que era.
                    duplicação+=duplicada          
            moleculas_duplicatas.append(duplicação)
        todas_moleculas= moleculas + moleculas_duplicatas
        return todas_moleculas
#QUEBRA DE MOLÉCULAS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Quebra(self, moleculas):
        mol=[]
        seq_q='TTT'
        erro='--'
        prob_q=10
        
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
            while ((i+len(quebra)-1) < QTD):
                condição=True
                j=0
                while (j < len(quebra) ):
                    condição= gene[i+j] == quebra[j]
                    j+=1
                    if (condição == False):
                        j=0
                        break
                if (j==len(quebra)):
                    stopcodon=i+j#-(len(quebra)) #aqui
                    for x in range(stopcodon):
                        aux_mol+=gene[x]
                    mol.append(aux_mol)
                    original=False
                    break
                i+=1
            if(original==True):
                mol.append(gene)
        return mol
    
#JUNÇÃO DE MOLÉCULAS---------(Usando a junção 2)--------------------------------------------------------------------------------------------------------
    def Junção(self, moleculas, alvo, inverso):
        if (inverso == ''):
            for base in alvo:
                if (base == 'A'):
                    inverso+='T'
                if (base == 'T'):
                    inverso+='A'
                if (base == 'C'):
                    inverso+='G'
                if (base == 'G'):
                    inverso+='C'
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
            while ((i+len(inverso)-1) < QTD):
                condição=True
                j=0
                while (j < len(inverso)):
                    condição= gene[i+j] == inverso[j]
                    j+=1
                    if (condição == False):
                        j=0
                        break
                if (j == len(inverso)):
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
                NA[i]=1                             #Se uma molécula tem os 2 genes,se (NA[i]=1  E  NI[i]=0) ela se juntará com uma não afim.
                NI[i]=0                             #Se uma molécula tem os 2 genes,se (NA[i]=0  E  NI[i]=1) ela se juntará com uma afim.
                QTD_NA-=0                           #Se (NA[i]=0) colocar   (QTD_NA-= 1)
                QTD_NI-=1                           #Se (NI[i]=0) colocar   (QTD_NI-= 1)

        x=5                                        #Probabilidade de haver junção.
        for i in range(len(moleculas)):
            if (NA[i] == 1 and x < (random.randint(1,100))):
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

            aux=moleculas[j]
            moleculas[i]+=aux
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
                

        return moleculas
    

#CONSTANT POPULATION-----------------------------------------------------------------------------------------------------------------
    def CP(self , moleculas , popMax , alvo):                                                   # entrando moleculas  + mol - filhas
        qtd_mol=len(moleculas)
        CP=[]
        
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

            QTD_NB= (qtd_mol) - (QTD_NA)

        while (qtd_mol > popMax):
            i=random.randint(0,(len(moleculas))-1)
            if (NA[i] == 1 and QTD_NA > 0):
                del(NA[i])
                del(moleculas[i])
                QTD_NA -= 1
            elif(NA[i] == 0 and QTD_NB > 0):
                del(NA[i])
                del(moleculas[i])
                QTD_NB -= 1
            qtd_mol=len(moleculas)

        return moleculas


