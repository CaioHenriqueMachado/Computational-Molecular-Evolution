import math

class ShannonEntropy:
    def __init__(self):
        self.result_entropy = [2]
        self.b = [ 'A','C','T','G' ]
    def Result(self, molecules):
        molecules
        entropia = []
        entropia_media = 0
        
        for i in range( len( molecules[ 0 ] ) ):
            a = 0
            c = 0
            t = 0
            g = 0
            
            for sequencia in molecules:
                if (sequencia[ i ] == self.b[ 0 ] ):
                    a+= 1
                elif(sequencia[ i ] == self.b[ 1 ] ):
                    c+= 1
                elif(sequencia[ i ] == self.b[ 2 ] ):
                    t+= 1
                elif(sequencia[ i ] == self.b[ 3 ]):
                    g+= 1

            a = a / ( len( molecules ) )
            c = c / ( len( molecules ) )
            t = t / ( len( molecules ) )
            g = g / ( len( molecules ) )
            if( a == 0 ):                                            #Caso alguma das letras der 0, colocar 1 pois se nao da erro(nao faz diferença pois log2(1)=0)
                a = 1
            if( c == 0 ):
                c = 1
            if( t == 0 ):
                t = 1
            if( g == 0 ):
                g = 1

            H =-( ( (a)*math.log2(a) ) + ( (c)*math.log2(c) ) + ( (t)*math.log2(t) ) + ( (g)*math.log2(g) ) )      # H representa a entropia na coluna
            entropia.append( H )


        entropia_media = sum( entropia ) / len( entropia )
        self.result_entropy.append(entropia_media)
        return entropia_media


'''
NOTA
Função faz entropia, retorna a entropia do clico atual e armazena um array de entropia para cada ciclo
'''