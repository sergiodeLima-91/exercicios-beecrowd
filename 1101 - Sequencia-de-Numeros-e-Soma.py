#Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).

# Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo
# o N e M).

#Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número
# nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

# 1 ---------------------------------------------------------
while True:
    soma = 0
    valor1, valor2 = map(int, input().split())
# 2 ---------------------------------------------------------
    if valor1 == 0 or valor1 < 0 or valor2 == 0 or valor2 < 0:
        if valor1 == 0:
            break
        elif valor1 < 0:
            break
        elif valor2 == 0:
            break
        elif valor2 < 0:
            break
# 3 ---------------------------------------------------------
    if valor1 > valor2: # 3.1
        for c in range(1, valor1 + 1): # 3.2
            print(f'{valor2} ',end='') # 3.3
            soma += valor2 # 3.4
            valor2 += 1 # 3.5
            if valor2 > valor1: # 3.6
                print(f'Sum={soma}')
                valor1 = valor2 = 0 # 3.7
                break # 3.8
# 4 ---------------------------------------------------------
    if valor2 > valor1:
        for c in range(1, valor2 + 1):
            print(f'{valor1} ',end='')
            soma += valor1
            valor1 += 1
            if valor1 > valor2:
                print(f'Sum={soma}')
                valor1 = valor2 = 0
                break

# 1 - Criando laço infinito para pegar os valores, já que eu não sei quantas vezes o procedimento será realizado.
# 2 - Este laço IF é para caso quaisquer das entradas sejam iguais ou menores que zero (o que significa, neste último
# caso, que o número é negativo). Ocorrerá a pausa total do programa caso isso ocorra.
# 3 - Em seguida eu criei dois IFs para realizar tanto o procedimento de colocar os valores em ordem crescente quanto
# apresentar a contagem do menor para o maior e somar os valores deste interválo no final.
# 3.1 - Primeiro, temos o caso em que valor1 será que valor2.
# 3.2 - Este laço FOR com range vai servir para realizar o procedimento de apresentação do interválo que parte de valor2
# até valor1 (lembrando que a contagem começa em valor2 porque, nesse IF, o valor dele é menor e queremos começar a
# contagem do menor para o maior.
# 3.3 - Impressão formatada com a variável valor2 referenciada entre as chaves. Fazemos isso para apresentar a
# sequência de números conforme a contagem do FOR. Como sabemos, o "end=''" serve para trazer para a linha atual o que
# está na linha de baixo. Fazemos isso porque queremos apresentar os números do interválo na mesma linha de forma
# hrizontal e não um abaixo do outro, no sentido vertical.
# 3.4 - A variável "soma" recebe um incremento de todos os números do interválo.
# 3.5 - A variável valor 2 recebe esse incremento porque temos que apresentar o restante dos números do interválo. Se
# este incremento não fosse colocado haveria a repetição de um número só, que no caso foi o primeiro que o utilizador
# inseriu.
# 3.6 - Bem, eu precisava apresentar, conforme o exemplo de saída da questão, a sequência dos números partindo do menor
# para o maior e, no final, a soma dos valores desse interválo. Então criei este IF cuja condicional é: Se o valor em
# "valor2" for maior que "valor1" (isto é, se ele ultrapassar o limite da contagem do interválo), mostre a variável
# "soma".
# 3.7 - O que significa está expressão e por que eu coloquei ela aqui? Ora, lembre-se de que, no escopo geral, estamos
# executando um laço infinito "while True" porque iremos executar o procedimento narrado até agora numa quantidade de
# vezes inderteminada. Precisamos deixar as variáveis valor1 e valor2 vazias para receber novos valores.
# 3.8 - O fim de tudo é parar o laço FOR e recomeçar o processo do laço while True novamente.
# 4 - Toda a lógica elencada no ponto 3 vale para cá, com a única diferença da condicional que, neste caso, é se a
# variável valor2 for maior que a valor1

