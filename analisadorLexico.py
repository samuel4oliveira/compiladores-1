def analisadorLexico(pathEntrada):
    palavrasReservadas = {
        'var':'declaracao',
        ':' : 'dois pontos',
        ',':'virgula',
        'integer':'tipo',
        ';':'ponto e virgula',
        ':=':'atribuicao',
        'if':'condicional',
        'then':'acao condicional',
        '+':'soma'
    }

    arquivo = open(pathEntrada).read()
    for x in palavrasReservadas:
        arquivo = arquivo.replace(x, " " + x + " ")
    arquivo = arquivo.replace(': =', ':=')
    tokens = arquivo.split()

    resultado = {}
    for token in tokens:
        if token in palavrasReservadas:
            resultado.update({token:palavrasReservadas[token]})
        elif token.isalpha():
            resultado.update({token:'identificador'})
        else:
            return ('Erro') 
    return resultado