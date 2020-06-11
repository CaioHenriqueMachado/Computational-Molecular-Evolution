
class Calculation:
    def __init__(self, alpha, beta, pop_max):
        self.all_results = [0]
        self.alpha = alpha
        self.beta = beta
        self.pop_max = pop_max

    def GrowthEquation(self, affinity, molecules):
        NA = affinity * len(molecules)
        NB = len(molecules) - NA
        self.alpha = ( self.alpha / 100 )
        self.beta = ( self.beta / 100 )

        #REPLICAÇÃO
        replication = 2 * ( NA + NB)

        #CP
        if ( replication > self.pop_max ):
            diff = (( replication - self.pop_max  ) / replication)
        else:
            diff = 0

        
        #Fator de equilibrio:
        CP = (1 - diff)
        RCP = 2


        #Afins:
        Afins =  NA * RCP
        Afins+= ((1- self.alpha)*NA)
        Afins+= (self.alpha*NB) #Chance de não afim virar afim
        Afins*= CP

        #Não Afins:
        Nao_Afins =  NB * RCP 
        Nao_Afins+=  ( self.beta * (1-self.alpha) *NB )# Chance de afim virar não afim
        Nao_Afins+=  ( self.alpha * NA * self.beta )  
        Nao_Afins*= CP
    
        Qtd = ( Afins + Nao_Afins )
        Afinidade = (Afins/(Qtd))

        self.all_results.append(Afinidade)
        return Afinidade

'''
NOTA
 - Nesse codigo tentei deixar o mais proximo do real possivel (formula feita por mim)
 - Aqui está fazendo se baseando em cada ciclo. Mas o correto é passar o parâmetro do cliclo inicial e ele fazer o resto só.
 - Fazer retornar também a quantidade das moléculas.
'''