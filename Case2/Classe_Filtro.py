import random
#FILTRO 
class Filtro:       
    def seleção(self , moleculas , alvo, beta):
        #PARA MOLECULAS AFINS--------------------------------------------------------
        selecionadas=[]
        NA=0
        i=-1

        for gene in moleculas:
            i+=1
            x=random.randint(1,100)
            afins=gene.count(alvo)          

            if (afins >0):                                            
                if (x <=100):                                             #Moléculas afins tem 100% de chance de ficar.
                    selecionadas.append(gene)
                    NA+=1

                
            #PARA MOLECULAS  NÃO AFINS--------------------------------------------------------
            if(afins == 0):
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
