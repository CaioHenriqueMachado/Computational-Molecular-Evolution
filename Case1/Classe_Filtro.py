import random
#FILTRO 
class Filtro:       
    def seleção(self , moleculas , alvo, beta):
    #PARA MOLECULAS AFINS--------------------------------------------------------
        selecionadas=[]
        NA=0
        for gene in moleculas:
            QTD=len(gene)
            i=0
            afins=0
            x=random.randint(1,100)
            if(len(gene) >= len(alvo)):
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
                        break
                    i+=1
                if (afins >0):                                            
                    if (x <=100):                                             #Moléculas afins tem 100% de chance de ficar.
                        selecionadas.append(gene)
                        NA+=1
                #PARA MOLECULAS  NÃO AFINS--------------------------------------------------------
                else:
                    if(x<=(beta)):                                                       # % de chance de ficar.
                        selecionadas.append(gene)
            else:
                if(x<=(beta)):                                                       # % de chance de ficar.
                    selecionadas.append(gene)
                    
        #Para Tamanho médio das moléculas
        soma=0
        qtd=len(selecionadas)
        for mol in selecionadas:
            soma+=(len(mol))

        TAM=soma/qtd
                    
        afinidade=NA /len(selecionadas)
        return selecionadas, afinidade,TAM
