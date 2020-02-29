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

path = '/home/samuel/Documents/ufmt/entrada-parte2.txt'
arquivo = open(path).read()
for x in palavrasReservadas:
    arquivo = arquivo.replace(x, " " + x + " ")
arquivo = arquivo.replace(': =', ':=')
tokens = arquivo.split()

resultado = {}
for token in tokens:
    if token in palavrasReservadas:
        resultado.update({token:palavrasReservadas[token]})
    else:
        resultado.update({token:'identificador'})