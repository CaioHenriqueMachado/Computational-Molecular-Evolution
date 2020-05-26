import random

class RNA:
    def Gerar ( self, molecula, tamanho, alvo ):
        geradas = []
        for i in range( molecula ) :
            bases = [ "A", "T", "C", "G" ]
            sequencia = ""
            k = 0
            while k < tamanho:
                sequencia+= bases[ random.randint(0, 3) ]
                k+= 1                
            geradas.append( sequencia )
#Para achar a afinidade do primeiro ciclo:
        NA = 0
        for gene in geradas:
            QTD = len( gene )
            i = 0
            afins = 0  
            while ( ( i + len( alvo ) -1 ) != QTD ):
                condição = True
                j = 0
                while ( j < len( alvo ) ):
                    condição = gene[ i + j ] == alvo[ j ]
                    j+= 1
                    if ( condição == False ):
                        j = 0
                        break
                if ( j == len( alvo ) ):
                    afins+= 1   
                
                i+= 1
            if ( afins > 0 ):                                          
                NA+= 1

        afinidade = NA / ( len( geradas ) )
        return geradas, afinidade
#REAÇÃO EM CADEIA DA POLIMERASE(duplicação de molecula com erro/mutação)-----------------------------------------------------------
    def PCR( self , moleculas, alfa ):
        bases = [ "A", "T", "C", "G" ]
        mutação = alfa                                                                                                                                 
        moleculas_duplicatas = []
        
        for j in moleculas:
            duplicação=''
            for i in j:
                duplicada = ''
                x = random.randint( 1,100 )
                if ( x > mutação ):
                     duplicação+= i
                else:
                    duplicada = bases[ random.randint( 0, 3 ) ]
                    while( i == duplicada ):                                                 #Se deixar tirar o comentario dessas linhas, admite que  quando sofre... 
                      duplicada = bases[ random.randint( 0, 3 ) ]                 #...mutação a base não tem chance de ser o que era.
                    duplicação+= duplicada          
            moleculas_duplicatas.append( duplicação )
        todas_moleculas = moleculas + moleculas_duplicatas
        return todas_moleculas
#CONSTANT POPULATION-----------------------------------------------------------------------------------------------------------------
    def CP( self , moleculas , popMax , alvo ):                                                   # entrando moleculas  + mol - filhas
        qtd_mol = len( moleculas )
        CP = []
        
        #Para Localizar Moléculas com gene Alvo
        NA = []
        QTD_NA = 0
        for gene in moleculas:
            QTD = len( gene )
            i = 0
            afins = 0  
            while ( ( i + len( alvo ) -1 ) < QTD ):
                condição = True
                j = 0
                while ( j < len( alvo ) ):
                    condição = gene[ i + j ] == alvo[ j ]
                    j+= 1
                    if (condição == False):
                        j = 0
                        break
                if ( j == len( alvo ) ):
                    afins+= 1
                    break
                i+= 1
            if ( afins > 0 ):                                          
                NA.append( 1 )
                QTD_NA+= 1
            else:
                NA.append( 0 )
                

        QTD_NB = ( qtd_mol ) - ( QTD_NA )

        while ( qtd_mol > popMax ):
            i = random.randint( 0, ( len( moleculas ) ) -1 )
            if ( NA[i] == 1 and QTD_NA > 0 ):
                del( NA[ i ] )
                del( moleculas[ i ] )
                QTD_NA -= 1
            elif(NA[i] == 0 and QTD_NB > 0):
                del( NA[ i ] )
                del( moleculas[ i ] )
                QTD_NB -= 1
            qtd_mol = len( moleculas )
                                
        return moleculas
