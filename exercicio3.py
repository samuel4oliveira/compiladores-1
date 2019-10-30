codigo = open("/mnt/c/Users/samuel/Documents/ufmt/compiladores1/entradaExercicio3.txt", "r").read()
codigo = codigo.replace("(", "( ")
codigo = codigo.replace(")", " )")
tokens = codigo.split()

palavraReservada = ['if']
operadorRelacional = ['<']
operadorAtribuição = ['=']
operadorAritmetico = ['+', '-', '*', '/']

aux = 0
variavil = " "
for token in tokens:
    if token in palavraReservada:
        print(token, ", palavra reservada")
    elif token  == '(':
        print(token + ", abre parenteses")
    elif token in operadorRelacional:
        print(token + ", operador relacional")
    elif token == ')':
        print(token + ", fecha parenteses")
    elif token == '{':
        print(token + ", abre chaves")
    elif token == '}':
        print(token + ", fecha chaves")
    elif token in operadorAtribuição:
        print(token + ", operador de atribuição")
    elif token in operadorAritmetico:
        print(token + ", operador aritimético")
    elif token == "/*":
        variavil = "/* "
        aux = 1
    elif aux == 1 and token != "*/":
        variavil += token
    elif aux == 1 and token == "*/":
        variavil += " */"
        aux = 0
        print(variavil + ", comentário")
    
    try:
        int(token)
        print(token + ", numero inteiro")
    except ValueError:
        try:
            float(token)
            print(token + ", numero real")
        except ValueError:
            pass
