import analisadorLexico
import analisadorSemantico

global posicao, token
posicao = 0
token = analisadorLexico.analisador_lexico('/home/samuel/Documents/ufmt/compiladores1/entrada.txt')

def analisador_sintatico():

    def z():
        #Declaração
        i()

        #Condicional e Atribuição
        s()
    
    def i():
        global posicao, token
        if token[posicao][1] == 'declaracao':
            posicao += 1
            d()
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'var', '" + token[posicao][0] + "' não é válido.")
    
    def d():
        global posicao, token
        l()
        if token[posicao][1] == 'dois pontos':
            posicao += 1
            k()
            o()
        
    def l():
        global posicao, token
        if token[posicao][1] == 'identificador':
            #Inicio Analisador Semantico
            analisadorSemantico.inserir_id(token[posicao][0])
            #Fim Analisador Semantico
            posicao += 1
            x()
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'identificador', '" + token[posicao][0] + "' não é válido.")
    
    def x():
        global posicao, token
        if token[posicao][1] == 'virgula':
            posicao += 1
            l()
    
    def k():
        global posicao, token
        if token[posicao][1] == 'tipo_integer' or token[posicao][1] == 'tipo_real':
            posicao += 1
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'integer' ou 'real', '" + token[posicao][0] + "' não é válido.")
        #Inicio Analisador Semantico
        analisadorSemantico.inserir_tipo(token[posicao-1][1])    
        #Fim Analisador Semantico

    def o():
        global posicao, token
        if token[posicao][1] == 'ponto e virgula':
            posicao += 1
            d()
    
    def s():
        global posicao, token
        if token[posicao][1] == 'identificador':
            #Inicio Analisador Semantico
            if not analisadorSemantico.buscar_id(token[posicao][0]):
                raise EnvironmentError("Erro Semantico, atribuição em identificador não declarada.")
            analisadorSemantico.inserir_soma(token[posicao][0])
            #Fim Analisador Semantico
            if len(token) > posicao+1:         
                posicao += 1
                if token[posicao][1] == 'atribuicao':
                    posicao += 1
                    e()
                    #Inicio Analisador Semantico
                    analisadorSemantico.verificar_tipo('atribuicao')
                    #Fim Analisador Semantico
                    if posicao < len(token):
                        raise EnvironmentError("Erro Sintático, declaração após atribuição.")
                else:
                    raise EnvironmentError("Erro Sintático, '" + token[posicao][0] + "' não é válido.")
            else:
                raise EnvironmentError("Erro Sintático, código inacabado.")
        elif token[posicao][1] == 'condicional':
            posicao += 1
            e()
            if len(token) > posicao+1:
                if token[posicao][1] == 'acao condicional':
                    posicao += 1
                    s()
                else:
                    raise EnvironmentError("Erro Sintático, é esperado 'then', '" + token[posicao][0] + "' não é válido.")
            else:
                raise EnvironmentError("Erro Sintático, código inacabado.")
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'identificador' ou 'if', '" + token[posicao][0] + "' não é válido.")
    
    def e():
        global posicao, token
        t()
        r()
    
    def r():
        global posicao, token
        try:
            if token[posicao][1] == 'soma':
                posicao += 1
                t()
                r()
                return
            #Inicio Analisador Semantico
            analisadorSemantico.verificar_tipo('soma')
            #Fim Analisador Semantico
        except IndexError:
            return
    
    def t():
        global posicao, token
        if token[posicao][1] == 'identificador':
            #Inicio Analisador Semantico
            analisadorSemantico.buscar_id(token[posicao][0])
            analisadorSemantico.inserir_soma(token[posicao][0])
            #Fim Analisador Semantico
            analisadorSemantico.inserir_id(token[posicao][0])
            posicao += 1
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'identificador', '" + token[posicao][0] + "' não é válido.")
    
    z()
analisador_sintatico()