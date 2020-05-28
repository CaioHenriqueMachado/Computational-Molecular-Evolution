import random
class Distancia:
    def D_Hamming(self , gerada,distancia_anterior,replicas):
        self.distancia_anterior=distancia_anterior
        self.gerada=gerada
        parte_gerada=[]
        parte_mutada=[]
        i=int(len(self.gerada)/2)                                       #Para a metade com mutação
        z=0
        while (z != i):
            if (replicas == 0):
                break
            replicas-=1
            parte_gerada.append(self.gerada[z])

            parte_mutada.append(self.gerada[i+z])
            z+=1
        
        distancia=[]
        for gene1 , gene2 in zip (parte_gerada , parte_mutada) :
            cont=sum(ch1 != ch2 for ch1, ch2 in zip(gene1, gene2))
            distancia.append(cont)
        return (self.distancia_anterior+distancia)

#POSTERIORMENTE ARRUMAR SCORE DISTANCE
    def ScoreDistance(self, D_hamming):
        self.D_hamming=D_hamming
    
        Score=[]
        for i in range(len(self.D_hamming)):
            x=random.randint(0,100)
            if (self.D_hamming[i] == 3 or self.D_hamming[i] == 4 ):
                if (x>=10):                                                                    #Se o numero for 4 ou 3 tem 10% de chance sair
                    Score.append(1)
                else:
                    Score.append(0)
            elif(self.D_hamming[i] < 3 ):
                if (x>=5):                                                                    #Se o numero for 4 ou 3 tem 5% de chance sair
                    Score.append(1)
                else:
                    Score.append(0)
            else:
                Score.append(0)
        return Score 
