#!/usr/bin/python3.6
#coding: utf-8
import sys
import webbrowser
from arquivo import leArquivo
from FIFO import FIFO
from OTM import OTM
from LRU import LRU

quadros = 0
memoria = []

instancia = leArquivo(sys.argv[1],quadros, memoria)
instancia.le()
print(instancia.quadros)
print(instancia.memoria)

arquivo = open("SO_saida_arquivo.txt", 'w')

paginaFIFO = FIFO(instancia.quadros, instancia.memoria)
arquivo.write("FIFO - " + str(paginaFIFO.FIFOexec()) + '\n')

paginaOTM = OTM(instancia.quadros, instancia.memoria)
arquivo.write("OTM - "+ str(paginaOTM.OTMexec()) + '\n')

paginaLRU = LRU(instancia.quadros, instancia.memoria)
arquivo.write("LRU - " + str(paginaLRU.LRUexec()) + '\n')

arquivo.close()
webbrowser.open("SO_saida_arquivo.txt")
