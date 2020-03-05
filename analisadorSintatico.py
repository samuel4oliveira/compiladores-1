import analisadorLexico

def analisador_sintatico(tokens):

    global posicao 
    posicao = 0

    def r(tokens):
        global posicao
        try:
            if tokens[posicao][1] == 'soma':
                posicao += 1
                t(tokens)
                r(tokens)
        except IndexError:
            return

    def t(tokens):
        global posicao
        if tokens[posicao][1] == 'identificador':
            posicao += 1
        else:
            raise ValueError("Erro de Sintaxe, '" + tokens[posicao][0] + "' não é um identificador válido." )

    def e(tokens):
        global posicao
        t(tokens)
        r(tokens)

    def s(tokens):
        global posicao
        if tokens[posicao][1] == 'identificador' and tokens[posicao+1][1] == 'atribuicao':
            posicao += 2
            e(tokens)
            if posicao > len(tokens):
                return
        try:
            if tokens[posicao][1] == 'condicional':
                posicao += 1
                e(tokens)
                if tokens[posicao][1] == 'acao condicional':
                    posicao += 1 
                    s(tokens)
                else:
                    raise ValueError("Erro de Sintaxe, '" + tokens[posicao][0] + "' não é um operador de ação condicional." )
            else:
                raise ValueError("Erro de Sintaxe, '" + tokens[posicao][0] + "' não é um operador condicional.")
        except IndexError:
            return

    def o(tokens):
        global posicao
        if tokens[posicao][1] == 'ponto e virgula':
            posicao += 1
            d(tokens)

    def k(tokens):
        global posicao
        if tokens[posicao][1] == 'tipo':
            posicao += 1
        else:
            raise ValueError("Erro de Sintaxe, '" + tokens[posicao][0] + "' não é um tipo suportado.")

    def x(tokens):
        global posicao
        if tokens[posicao][1] == 'virgula':
            posicao += 1
            l(tokens)

    def l(tokens):
        global posicao
        if tokens[posicao][1] == 'identificador':
            posicao += 1
            x(tokens)
        else:
            raise ValueError("Erro de Sintaxe, '" + tokens[posicao][0] + "' não é um identificador válido.")
    
    def d(tokens):
        global posicao
        l(tokens)
        if  tokens[posicao][1] == 'dois pontos':
            posicao += 1
            k(tokens)
            o(tokens)
        else:
            raise ValueError("Erro de Sintaxe, era esperado ':', " + tokens[posicao][0] + " não é válido.")
        
    def i(tokens):
        global posicao
        if tokens[posicao][1] == 'declaracao':
            posicao += 1
            d(tokens)
        else:
            raise ValueError("Erro de Sintaxe, era esperado 'var', " + tokens[posicao][0] + " não é válido.")

    def z(tokens):
        i(tokens)
        s(tokens)
   
    z(tokens)