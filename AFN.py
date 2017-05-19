#-*- coding: utf-8 -*-
#!/usr/bin/env python

from AFD import AFD

class AFN():
    def __init__(self, delta, q0, l_qf, t_e):
        self.delta = delta
        self.q0 = q0
        self.l_qf = l_qf
        self.t_e = t_e

    # TODOS OS ESTADOS ALCAÇÁVEIS A PARTIR DE state consumindo c    
    def edge(self, state, c):
        try:
            return self.delta[state][c]
        except KeyError:
            return set([])

    # TODOS OS ESTADOS ALCANÇÁVEIS A PARTIR DE states CONSUMINDO c.   
#    def AFDedge(self, states, str):
#        T = []
#        for state in states:
#            T = T.union(self.edge(state, str))
#        T_ = []
#        for state in T:
#            T_ = T_ .union(self.closure(state))
#        return T_

    # TODOS OS ESTADOS ALCANÇÁVEIS A PARTIR DO CONJUNTO state, sem consumir caractere de entrada.        
    def closure(self, state):
        T = set([state])
        T_ = set([])
        while True:
            for state in T:
                T_ = T
                try:
                    T = T_ .union(self.edge(state, self.t_e))
                except KeyError:
                    pass
            if T_ == T:
                    break
        return T
    # TODOS OS ESTADOS ALCANÇÁVEIS A PARTIR DE states CONSUMINDO c.   
    def AFDedge2(self, state, str):
        str = str.replace(self.t_e, '')
        states = self.closure(state)
        for c in str:
            nStates = set([])
            for state in states:
                for state_ in self.closure(state):
                    try:
                        nStates = nStates.union(self.delta[state_][c]) # PEGANDO O SÍMBOLOS DE CADA ESTADO CONSOME COM O CHAR c
                    except KeyError: pass
            states = nStates # ESTADOS ALCANÇADOS COM O SÍMBOLO
        return states

# INTERSEÇÃO DO AFDedge2(ESTADO INICIAL COM O STR) E O CONJUNTO DE ESTADOS FINAIS    
    def pertence(self, str):
        return len(self.AFDedge2(self.q0, str) & set(self.l_qf)) > 0

    def AFNtoAFD(self):
        #inicia o automato sem transicoes apenas com os estados iniciais
        #estado único frozenset, ele pode ser usado como chave de dicionario
        e_inicial = frozenset(self.closure(self.q0))
        automato = AFD({}, e_inicial, [])
        #conjunto de estados do novo automato
        Q = set([automato.q0])
        #conjunto de estados nao processados
        nQ = Q.copy()
        Sigma = self.alfabeto()
        Sigma.remove(self.t_e)
        while len(nQ) > 0:
            qSet = nQ.pop()
         #   print qSet
            #o dicionario é iniciado na posicao qSet
            automato.delta[qSet] = {}
            for c in Sigma:
          #      print ("c, qSet", c, qSet)
                #proximos estados apartir de c que serao um unico estado
                nextStates = set([])
                for state in qSet:
                    nextStates = nextStates.union(self.AFDedge2(state, c))
                nextStates = frozenset(nextStates)
                #nao sendo conjunto vazio é adicionado a transicao
                if nextStates != set([]):
                    automato.delta[qSet][c] = nextStates
                    #é adicionado o novo estado no conjunto de estados no novo automato
                    if not nextStates in Q:
                        Q.add(nextStates)
                        nQ.add(nextStates)  # VERIFICANDO O QUE FAZ PARTE DOS TOKENS
#            print "qSet agora : ", qSet # Passa por todos os estados
#            print "Finais : ",self.l_qf # somente o estado final INICIAL            
            # para calcular os estados finais            
            for qSet in Q: # não pode ser o automato adicional uQ
                if len(qSet & set(self.l_qf)) > 0: # O & FAZ A UNIÃO, SE EXISTIR ALGUM ESTADO FINAL.
                    if not qSet in automato.l_qf: # NÃO REPETIR ESTADOS FINAIS
                        automato.l_qf.append(qSet)
        return automato
    # ver http://stackoverflow.com/questions/19580944/python-set-union-and-set-intersection-operate-differently para o operador    
    def alfabeto(self):
        Sigma = reduce(lambda a,b:set(a).union(set(b)), [x.keys() for x in self.delta.values()])
        # convertendo para lista
        Sigma2 = [list (c) for c in Sigma]
   #     print "Alfabeto: ",Sigma2        
        return Sigma

# DESCOMENTE ESSA PARTE DO CÓDIGO E TESTE O ARQUIVO: python2 afn.py 
'''
afn3 =   {
            1:{'b':set([2]), 'epsilon':set([3])},
            2:{'a':set([2,3]), 'b':set([3])},
            3:{'a':set([1])},
        }
finais3 = [1]   
n = AFN(afn3, 1, finais3, 'epsilon')
res = n.AFNtoAFD()
print "\n"
print "Delta \n",res.delta
print "\n"
print "Q0 \n",res.q0
print "\n"
print "Finais \n",res.l_qf
'''