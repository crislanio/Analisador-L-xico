#-*- coding: utf-8 -*-
#!/usr/bin/env python

import copy
import fileinput
import Automato as Aut
from Automato import* 
from AFN import AFN
from AFD import AFD
    
def main():
    arq = open('saida.txt', 'w')

    automato = ConstAutomato()
    str = ""
    for l in fileinput.input():  # http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python
								 # Ler entrada do arquivo 
        str += l
    str = Aut.removeComentario(copy.deepcopy(str))	
    if str != None:
        print automato.recuperarTokens(str, meuMapaAutomato)                
        tokens = []
        tokens.append(automato.recuperarTokens(str, meuMapaAutomato))
        arq.writelines(tokens)
        arq.close()

if __name__ == "__main__":
    main()

