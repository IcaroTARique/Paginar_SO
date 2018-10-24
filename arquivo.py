#!/usr/bin/python3.6
#coding: utf-8

class leArquivo():
    def __init__ (self,nome, quadros, memoria):
        #ATRIBUTO É O CAMINHO DO ARQUIVO LIDO
        self.nome = nome
        self.quadros = quadros
        self.memoria = memoria

    def le(self):

        arq = open(self.nome, 'r')
        i = 0
        for line in arq:
            convertido = int(line)
            if i == 0:
                self.quadros = convertido
            else:
                self.memoria.append(convertido)
            i = i + 1
        arq.close()

