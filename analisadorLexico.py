codigo = open("/mnt/c/Users/samuel/Documents/ufmt/compiladores1/entradaAnalisadorLexico.txt", "r").read()
codigo = codigo.replace("(", "( ")
codigo = codigo.replace(")", " )")
codigo = codigo.replace("\n", " quebraDeLinha ")
tokens = codigo.split()

palavraReservada = ['if']
operadorRelacional = ['<']
operadorAtribuição = ['=']
operadorAritmetico = ['+', '-', '*', '/']

aux1 = 0
aux2 = 0
comentario = " "
for token in tokens:
    if token in palavraReservada:
        print(token + ", palavra reservada")
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
        comentario = "/* "
        aux1 = 1
    elif aux1 == 1 and token != "*/":
        comentario += token
    elif aux1 == 1 and token == "*/":
        comentario += " */"
        aux1 = 0
        print(comentario + ", comentário")
    elif token == "//":
        comentario = "//"
        aux2 = 1
    elif aux2 == 1 and token != "quebraDeLinha":
        comentario += token
    elif aux2 == 1 and token == "quebraDeLinha":
        aux2 = 0
        print(comentario + ", comentário")
    elif not token[0].isdigit() and token != "quebraDeLinha":
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