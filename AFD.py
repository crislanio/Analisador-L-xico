#-*- coding: utf-8 -*-
#!/usr/bin/env python

class AFD:  
    def __init__(self, delta, q0, l_qf):
        self.delta = delta
        self.q0 = q0
        self.l_qf = l_qf

    def recuperarTokens(self, str, mapTokens):
        i = 0
        str += " "
        j = len(str)
#        print "# número de tokens", j # número de tokens
        tokens = ""
        state = 0
        for c in str:
            i += 1
   #         print "ESTADO-TOKEN ",state, c  # ESTADO, TOKEN
   #         print "\n"
            if self.delta[state].has_key(c):
                state = self.delta[state][c]
    #            print "Com o símbolo ",c, " vou pro ESTADO:", state
                if i == j:
     #               print "LI TODOS OS TOKENS"
                    tokens += mapTokens[state]
            else: # JÁ LI O SÍMBOLO, AGORA LEIO ESPAÇO
            #    if self.delta[0].has_key(c): # pode comentar-PARA PEGAR O ESPAÇO
                    tokens += mapTokens[state] + " "
                    state = self.delta[0][c]
      #              print "SIMBOLO",c, "  ESTADO:", state
              #  else: # pode comentar
              #      tokens += "ERROR " # pode comentar
        return tokens 
        
    def percorrer(self, state, str):
        for c in str:
            try:
                state = self.delta[state][c]
            except KeyError:
                return None
        return state
    

    def pertence(self, str):
        return self.percorrer(self.q0, str) in self.l_qf

        
    # reduce python-    https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
    # Lambda and List Comprehensions Python: http://www.secnetix.de/olli/Python/lambda_functions.hawk and http://www.secnetix.de/olli/Python/list_comprehensions.hawk
    def alfabeto(self):
        # Usando a função reduce para receber os elementos do alfabeto, invés de criar uma função é usado o lambda
        # 1° parâmetro a, b escolhe a or b
        Sigma = reduce(lambda a,b:set(a).union(set(b)), [x.keys() for x in self.delta.values()])
        return Sigma

