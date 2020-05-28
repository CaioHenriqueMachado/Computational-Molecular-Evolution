#Calculando a entropia
import math
class Entropia:
    def Shannon(self , moleculas):
        new_moleculas=moleculas
        b=['A','C','T','G']
        entropia=[]
        entropia_media=0
        mol=[]
        tam_padrão= 50 #COLOQUE para (max(map(len,new_moleculas))) [sendo max ou min] para a entropia ser calculada com base na menor/maior molécula 
        for i in range(len(new_moleculas)):
            while (len(new_moleculas[i]) < tam_padrão):
                new_moleculas[i]+=' '
          
        for i in range(tam_padrão):
            a=0
            c=0
            t=0
            g=0
            
            for sequencia in new_moleculas:
                if (sequencia[i] ==b[0]):
                    a+=1
                elif(sequencia[i] ==b[1]):
                    c+=1
                elif(sequencia[i] ==b[2]):
                    t+=1
                elif(sequencia[i] ==b[3]):
                    g+=1
                elif(sequencia[i] == chr(32)):
                    pass

            a=a/(len(new_moleculas))
            c=c/(len(new_moleculas))
            t= t/(len(new_moleculas))
            g=g/(len(new_moleculas))
            if(a==0):                                            #Caso alguma das letras der 0, colocar 1 pois se nao da erro(nao faz diferença pois log2(1)=0)
                a=1
            if(c==0):
                c=1
            if(t==0):
                t=1
            if(g==0):
                g=1
            
            H=-(((a)*math.log2(a))+((c)*math.log2(c))+((t)*math.log2(t))+((g)*math.log2(g)))      # H representa a entropia na coluna
            entropia.append(H)

        z=0
        for gene in new_moleculas:
            aux=''
            for base in gene:
                if (base == chr(32)):
                    break
                aux+=base
            new_moleculas[z]=aux
            z+=1


        entropia_media=sum(entropia)/len(entropia)
        return entropia_media
