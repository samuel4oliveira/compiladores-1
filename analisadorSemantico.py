arquivo= open("saida.txt","w+")
global tabelaDeSimbolos
tabelaDeSimbolos = {}

global listaVerificacao
listaVerificacao = []

global linha
linha = 1

def inserir_id(id):
    global tabelaDeSimbolos
    tabelaDeSimbolos[id] = '' 

def inserir_tipo(tipo):
    global tabelaDeSimbolos
    for i in tabelaDeSimbolos:
        if tabelaDeSimbolos[i] == '':
            tabelaDeSimbolos[i] = tipo

def buscar_id(id):
    global tabelaDeSimbolos
    if id in tabelaDeSimbolos:
        return True
    else:
        return False

def verificar_tipo(chave):
    global linha
    global listaVerificacao
    global tabelaDeSimbolos
    
    for i in listaVerificacao:
        if tabelaDeSimbolos[i] == tabelaDeSimbolos[listaVerificacao[0]]:
            pass
        elif chave == 'soma':
            raise EnvironmentError("Erro Semantico, soma entre real e integer.")
        elif chave == 'atribuicao':
            raise EnvironmentError("Erro Semantico, atribuição entre real e integer.")

    #Inicio Gerador de Código
    if chave == 'atribuicao':
        aux = listaVerificacao[0]
        listaVerificacao.pop(0)

    while len(listaVerificacao) > 1:
        listaVerificacao.insert(2, 't1')
        arquivo.write(str(linha)+': ' + '[+ ' + listaVerificacao[0] + ' ' + listaVerificacao[1] +' ' + listaVerificacao[2] + ']\n')
        linha += 1
        listaVerificacao.pop(0)
        listaVerificacao.pop(0) 
    print(listaVerificacao)
    if chave == 'soma':
        arquivo.write(str(linha)+': ' +  '[JF ' + listaVerificacao[0] + ' ' + str(linha+2) + ' -]\n')
        linha += 1  
    elif chave == 'atribuicao':
        arquivo.write(str(linha)+':' + ' [:= ' + aux + ' ' + listaVerificacao[0] + ' -]\n')
        linha += 1 
        arquivo.write(str(linha)+': ' + '[...]')
        arquivo.close()
    #Fim Gerador de Código
    listaVerificacao = []

def inserir_soma(id):
    global listaVerificacao
    listaVerificacao.append(id)