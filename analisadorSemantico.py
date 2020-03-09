global tabelaDeSimbolos
tabelaDeSimbolos = {}

global listaSoma
listaSoma = []

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
    global listaSoma
    global tabelaDeSimbolos
    
    for i in listaSoma:
        if tabelaDeSimbolos[i] == tabelaDeSimbolos[listaSoma[0]]:
            pass
        elif chave == 'soma':
            raise EnvironmentError("Erro Semantico, soma entre real e integer.")
        elif chave == 'atribuicao':
            raise EnvironmentError("Erro Semantico, atribuição entre real e integer.")

    #Gerador de Código
    if chave == 'atribuicao':
        aux = listaSoma[0]
        listaSoma.pop(0)

    while len(listaSoma) > 1:
        listaSoma.insert(2, 't1')
        print(str(linha)+':', '[+', listaSoma[0], listaSoma[1], listaSoma[2] + ']')
        linha += 1
        listaSoma.pop(0)
        listaSoma.pop(0) 
        
    if chave == 'soma':
        print(str(linha)+':', '[JF', 't1', linha+2, '-]')
        linha += 1  
    elif chave == 'atribuicao':
        print(str(linha)+':', '[:=', aux, listaSoma[0], '-]')
        linha += 1 
        print(str(linha)+':', '[...]')
    
    #Gerador de Código
    listaSoma = []

def inserir_soma(id):
    global listaSoma
    listaSoma.append(id)