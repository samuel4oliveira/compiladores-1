import analisadorLexico

global posicao, token
posicao = 0
token = analisadorLexico.analisador_lexico('/home/samuel/Documents/ufmt/compiladores1/entrada.txt')
for i in range(len(token)):
    print(i, token[i])
def analisador_sintatico():

    def z():
        i()
        s()
    
    def i():
        global posicao, token
        print(posicao, 'i')
        if token[posicao][1] == 'declaracao':
            posicao += 1
            d()
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'var', '" + token[posicao][0] + "' não é válido.")
    
    def d():
        global posicao, token
        print(posicao, 'd')
        l()
        if token[posicao][1] == 'dois pontos':
            posicao += 1
            k()
            o()
        
    def l():
        global posicao, token
        print(posicao, 'l')
        if token[posicao][1] == 'identificador':
            posicao += 1
            x()
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'identificador', '" + token[posicao][0] + "' não é válido.")
    
    def x():
        global posicao, token
        print(posicao, 'x')
        if token[posicao][1] == 'virgula':
            posicao += 1
            l()
    
    def k():
        global posicao, token
        print(posicao, 'k')
        if token[posicao][1] == 'tipo':
            posicao += 1
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'integer' ou 'real', '" + token[posicao][0] + "' não é válido.")

    def o():
        global posicao, token
        print(posicao, 'o')
        if token[posicao][1] == 'ponto e virgula':
            posicao += 1
            d()
    
    def s():
        global posicao, token
        print(posicao, 's')
        if token[posicao][1] == 'identificador':
            print(posicao, 'identificador')
            posicao += 1
            if token[posicao][1] == 'atribuicao':
                print(posicao, 'atribuicao')
                posicao += 1
                e()
                if posicao < len(token):
                    raise EnvironmentError("Erro Sintático, declaração após atribuição.")
            else:
                raise EnvironmentError("Erro Sintático, é esperado 'var', '" + token[posicao][0] + "' não é válido.")
        elif token[posicao][1] == 'condicional':
            posicao += 1
            print(posicao, 'condicional')
            e()
            if token[posicao][1] == 'acao condicional':
                posicao += 1
                print(posicao, 'acao condicional')
                s()
            else:
                raise EnvironmentError("Erro Sintático, é esperado 'then', '" + token[posicao][0] + "' não é válido.")
        else:
            raise EnvironmentError("Erro Sintático, é esperado 'identificador' ou 'if', '" + token[posicao][0] + "' não é válido.")
    
    def e():
        global posicao, token
        print(posicao, 'e')
        t()
        r()
    
    def r():
        global posicao, token
        print(posicao, 'r')
        try:
            if token[posicao][1] == 'soma':
                posicao += 1
                t()
                r()
        except IndexError:
            return
    
    def t():
        global posicao, token
        print(posicao, 't') 
        if token[posicao][1] == 'identificador':
            posicao += 1

    z() 
analisador_sintatico()