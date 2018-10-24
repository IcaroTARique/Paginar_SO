#!/usr/bin/python3.6
#coding: utf-8

class FIFO():
    def __init__ (self, quadros, memoria):
        self.quadros = quadros
        self.memoria = memoria

    def FIFOexec(self):
        hits = 0
        j = 0
        fila = [-1]*self.quadros
        print('****************** FIFO ******************')
        for i in range(len(self.memoria)):
            if fila[j%self.quadros] != self.memoria[i] and not self.memoria[i] in fila:
                fila[j%self.quadros] = self.memoria[i]
                print(fila,"\n")
                hits += 1
                j += 1
            else:
                pass
        return hits
