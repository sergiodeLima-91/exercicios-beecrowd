#Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada
# valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE)
# ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL),
# pois, por definição, zero é par, seu programa deverá imprimir apenas NULL.

# 1(abaixo) -  Reserva a quantidade de números que deverão ser lidos.
quantidade = int(input())
# 2(abaixo) - Lista que recebe cada um dos números que irão ser lidos em seguida para depois serem avaliados.
numeros = list()
# 3(abaixo) - Este laço foi criado somente para armazenar os números digitados pelo utilizador. A quantidade de entradas
# erá determinada pelo valor digitado em "quantidade". É por essa razão que o intervalo começa em 1 e termina no valor
# presente em "quantidade" mais 1, já que o Python exclui sempre o último valor do número.
for contador in range(1, quantidade + 1):
    numero = int(input())
    numeros.append(numero)
# 4(abaixo) - Variável criada somente para armazenar o número que irá representar o índice que queremos avaliar no laço
# de repetição while True em seguida.
c = 0
# 5(abaixo) - Este laço infinito serve para avaliar qual ou quais são as características dos números digitados um por
# um. Como, lá embaixo antes de "if c == quantidade:" temos o incremento "c += 1" inserido na variável "c", avaliamos
# cada valor presente nos índices da lista "numeros". Avaliamos, primeiro, o valor do índice 0 assim que entramos no
# laço, já que o valor de "c" é 0. Em seguida, após determinarmos nas estruturas condicionais seguintes qual ou quais
# são as características do valor presente no índice 0 de "numeros", o "c" recebe 1 e seu valor muda de 0 para 1. Isso
# é transferido para o valor presente nas chaves e agora o valor a ser avaliado será o do índice 1 da lista "numeros".
# Este processo ocorrerá até que o valor de "c" seja igual ao de "quantidade". Depois disso, o comando "break" será
# executado na condicional depois do incremento.
while True:
    if numeros[c] == 0:
        print('NULL')
    else:
        if numeros[c] % 2 == 0:
            print('EVEN ', end='')
            if numeros[c] > 0:
                print('POSITIVE')
            if numeros[c] < 0:
                print('NEGATIVE')
        if numeros[c] % 2 != 0:
            print('ODD ', end='')
            if numeros[c] > 0:
                print('POSITIVE')
            if numeros[c] < 0:
                print('NEGATIVE')
    c += 1
    if c == quantidade:
        break
