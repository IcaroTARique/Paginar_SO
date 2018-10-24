
#!/usr/bin/python3.6
#coding: utf-8
import copy

class LRU():
    def __init__ (self, quadros, memoria):
        self.quadros = quadros
        self.memoria = memoria


    def LRUexec(self):
        fila = []
        counter = 0
        confere = []
        posicao = []
        pos = 0
        lis = []
        print('****************** LRU ******************')
        for i in range(len(self.memoria)):
            flag_1 = True
            flag_2 = True
            flag_3 = True
            #SE A LISTA FOR VAZIA - ACRESCENTA VALOR
            if not len(fila):
                print("FILA VAZIA")
                fila.append(self.memoria[i])
                print(fila)
                counter += 1
            else:
                #SE A FILA FOR MENOR QUE O TAMANHO DEFINIDO
                if (len(fila) < self.quadros):
                    for l in range(len(fila)):
                        #SE A FILA TEM NENHUM VALOR IGUAL, FLAG FALSE
                        if self.memoria[i] == fila[l]:
                            print("REPETIDO - ACRESÇÃO")
                            flag_1 = False
                    #ACRESCENTA VALOR
                    if flag_1:
                        fila.append(self.memoria[i])
                        counter += 1
                    print(fila)
                else:
                    #SE JÁ ESTIVER NA FILA, NÃO PRECISA TROCAR
                    for k in range(len(fila)):
                        if self.memoria[i] == fila[k]:
                            print("\nREPETIDO NÃO FAZ NADA")
                            flag_2 = False

                    if flag_2:
                        print("SEGUNDA PARTE",fila)
                        copia = copy.deepcopy(fila)
                        for ii in range(i, -1, -1):
                            for iii in range(len(fila)):
                                if self.memoria[ii] == fila[iii]:
                                    print(self.memoria[ii], " é igual a ", fila[iii])
                                    if not (fila[iii] in confere):
                                        confere.append(fila[iii])
                                        posicao.append(iii)
                            lis.append(self.memoria[ii])
                        print(lis)
                        lis = []

                        if len(confere) == len(fila):
                            fila[posicao[len(posicao)-1]] = self.memoria[i]
                            counter += 1
                        else:
                            for jj in range(len(fila)):
                                if not fila[jj] in confere:
                                    if flag_3:
                                        print (fila[jj])
                                        pos = jj
                                        fila[jj] = self.memoria[i]
                                        counter += 1
                                        flag_3 = False
                            flag_3 = True
                        print("FILA === > ",fila)

                        print(confere)
                        print(posicao)
                        confere = []
                        posicao = []
        print("COUNTER = ", counter)
        return counter