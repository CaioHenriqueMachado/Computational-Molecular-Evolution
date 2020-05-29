#nesse codigo tentei deixar o mais proximo do real possivel (formula feita por mim)

class Equação:
    def Crescimento(self , na , nb , alfa, beta, popMax ):
        erroQ = alfa
        alfa = ( alfa / 100 ) *5          #Eficiência de filtro( Chance de uma molecula afin passar)
        beta = ( beta / 100 )
        
        #Replicação:
        repli = 2*( ((1 - alfa )*na) + (alfa*na) + (nb))                                           #Q(t+ 1/2 )
    
       
        #Fator de diminuição de população:(DIFF)
        if ( popMax  < repli ):
            diff = (( repli - popMax  ) / repli)
        else:
            diff = (0)

        #Fator de equilibrio:
        CP = (1 - diff)
        RCP = 2

        #Afins:
        Afins =  na 
        Afins+= ((1- alfa)*na)
        Afins+= (alfa*nb)#
        Afins*= CP

        #Não Afins:
        Nao_Afins =  ( beta * nb ) 
        Nao_Afins+=  ( beta * (1-alfa) *nb )#
        Nao_Afins+=  ( alfa * na * beta )  
        Nao_Afins*= CP
    
        Qtd = ( Afins + Nao_Afins )
        Afinidade = (Afins/(Qtd))

        #Para formular o erro.(Apagar. Código errado)
        if ( erroQ > 5 ):
            erroA = ((erroQ-5)*1) / 100
            erroQ =( erroQ-5 )*3
            Qtd-= erroQ
            Afinidade-= erroA
    
        return(Qtd , Afinidade, Afins, Nao_Afins)
