import math
class Entropia:
    def Shannon( self, moleculas ):
        self.moleculas = moleculas
        b = [ 'A','C','T','G' ]
        entropia = []
        entropia_media = 0
        
        for i in range( len( self.moleculas[ 0 ] ) ):
            a = 0
            c = 0
            t = 0
            g = 0
            
            for sequencia in self.moleculas:
                if (sequencia[ i ] == b[ 0 ] ):
                    a+= 1
                elif(sequencia[ i ] == b[ 1 ] ):
                    c+= 1
                elif(sequencia[ i ] == b[ 2 ] ):
                    t+= 1
                elif(sequencia[ i ] == b[ 3 ]):
                    g+= 1

            a = a / ( len( self.moleculas ) )
            c = c / ( len( self.moleculas ) )
            t = t / ( len( self.moleculas ) )
            g = g / ( len( self.moleculas ) )
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
        return entropia_media
