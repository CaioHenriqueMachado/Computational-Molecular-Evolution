import random
class Filtro:       
    def seleção(self , moleculas, distancia , alvo,alfa, beta, Reservatório,tam):
        #PARA MOLECULAS AFINS--------------------------------------------------------
        selecionadas=[]
        new_distance=[]
        NA=0
        i=-1
        tam_padrão=tam * alfa * 0.01
        for gene in moleculas:
            i+=1
            x=random.randint(1,100)
            afins=gene.count(alvo)


                
            
            if (distancia[i] > tam_padrão and afins >0):        #SE  TEM DISTANCIA maior que a padrão TEM PROBABILIDADE DE SAIR. 
                afins=-1   
                
                

            if (afins >0):                                            
                if (x <=95):                                             #Moléculas afins tem 100% de chance de ficar.
                    selecionadas.append(gene)
                    new_distance.append(distancia[i])
                    NA+=1
                else:
                    Reservatório+=len(gene)
            if(afins == -1):
                if (x > (tam_padrão*10)):
                    selecionadas.append(gene)
                    new_distance.append(distancia[i])
                    NA+=1
                else:
                    Reservatório+=len(gene)
                
            #PARA MOLECULAS  NÃO AFINS--------------------------------------------------------
            if(afins == 0):
                if(x<=(beta)):                                                       # % de chance de ficar.
                    selecionadas.append(gene)
                    new_distance.append(distancia[i])   
                else:
                     Reservatório+=len(gene)

                        


        #Para Tamanho médio das moléculas
        soma=0
        qtd=len(selecionadas)
        for mol in selecionadas:
            soma+=(len(mol))

        TAM=soma/qtd

        afinidade=NA /len(selecionadas)
        return selecionadas,new_distance, afinidade , TAM, Reservatório
