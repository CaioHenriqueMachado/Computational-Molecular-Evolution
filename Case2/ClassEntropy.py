import math

class ShannonEntropy:
    def __init__(self):
        self.result_entropy = [2]
        self.b = [ 'A','C','T','G' ]
    def Result(self, molecules):
        molecules
        entropia = []
        entropia_media = 0

        new_molecules = molecules
        tam_padrão = 50 #COLOQUE para (max(map(len,new_molecules))) [sendo max ou min] para a entropia ser calculada com base na menor/maior molécula 
        for i in range(len( new_molecules )):
            while (len( new_molecules[i] ) < tam_padrão):
                new_molecules[i] += ' '
          
        for i in range( tam_padrão ):
            a = 0
            c = 0
            t = 0
            g = 0
            
            for sequencia in new_molecules:
                if (sequencia[i] == self.b[0]):
                    a += 1
                elif(sequencia[i] == self.b[1]):
                    c += 1
                elif(sequencia[i] == self.b[2]):
                    t += 1
                elif(sequencia[i] == self.b[3]):
                    g += 1
                elif(sequencia[i] == chr(32)):
                    pass

            a = a / (len(new_molecules))
            c = c / (len(new_molecules))
            t = t / (len(new_molecules))
            g = g / (len(new_molecules))
            if(a == 0):                                            #Caso alguma das letras der 0, colocar 1 pois se nao da erro(nao faz diferença pois log2(1)=0)
                a = 1
            if(c == 0):
                c = 1
            if(t == 0):
                t = 1
            if(g == 0):
                g = 1
            
            H=-(((a)*math.log2(a))+((c)*math.log2(c))+((t)*math.log2(t))+((g)*math.log2(g)))      # H representa a entropia na coluna
            entropia.append(H)

        z=0
        for gene in new_molecules:
            aux=''
            for base in gene:
                if (base == chr(32)):
                    break
                aux+=base
            new_molecules[z]=aux
            z+=1

        entropia_media = sum(entropia) / len(entropia)
        self.result_entropy.append(entropia_media)
        return entropia_media
'''
NOTA
Função faz entropia, retorna a entropia do clico atual e armazena um array de entropia para cada ciclo.
É feita a entropia de até 50 bases, mas pode ser facilmente alterado no código.
'''