codigo = open("/mnt/c/Users/samuel/Documents/ufmt/compiladores1/entradaExercicio3.txt", "r").read()
codigo = codigo.replace("(", "( ")
codigo = codigo.replace(")", " )")
codigo = codigo.replace("\n", " malandragi ")
tokens = codigo.split()

palavraReservada = ['if']
operadorRelacional = ['<']
operadorAtribuição = ['=']
operadorAritmetico = ['+', '-', '*', '/']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

aux1 = 0
aux2 = 0
variavil = " "
variavil2 = " "
for token in tokens:
    if token in palavraReservada:
        print(token, ", palavra reservada")
    elif token  == '(':
        print(token + ", abre parênteses")
    elif token in operadorRelacional:
        print(token + ", operador relacional")
    elif token == ')':
        print(token + ", fecha parênteses")
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
        aux1 = 1
    elif aux1 == 1 and token != "*/":
        variavil += token
    elif aux1 == 1 and token == "*/":
        variavil += " */"
        aux1 = 0
        print(variavil + ", comentário")
    elif token == "//":
        variavil2 = "//"
        aux2 = 1
    elif aux2 == 1 and token != "malandragi":
        variavil2 += token
    elif aux2 == 1 and token == "malandragi":
        aux2 = 0
        print(variavil2 + ", comentário")
    elif token[0] not in numeros and token != "malandragi":
        print(token + ", identificador")

    try:
        int(token)
        print(token + ", numero inteiro")
    except ValueError:
        try:
            float(token)
            print(token + ", numero real")
        except ValueError:
            pass