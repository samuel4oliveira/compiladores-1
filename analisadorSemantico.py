global tabelaDeSimbolos
tabelaDeSimbolos = {}

global listaSoma
listaSoma = []

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

def verificar_tipo():
    global listaSoma
    global tabelaDeSimbolos
    for i in listaSoma:
        if tabelaDeSimbolos[i] == tabelaDeSimbolos[listaSoma[0]]:
            pass
        else:
            raise EnvironmentError("Erro Semantico, soma ou atribuição entre real e integer.")
    listaSoma = []

def inserir_soma(id):
    global listaSoma
    listaSoma.append(id)