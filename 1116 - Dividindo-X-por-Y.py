# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível
# mostre a mensagem “divisao impossivel” para os valores em questão.

# Entrada
# A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em
# seguida.

# Saída
# Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja
# possível efetuar o cálculo.

# Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

# 1 ---------------------------
quantidade = int(input())

# 2 ---------------------------
for c in range(quantidade):
    dividendo_x, divisor_y = map(int, input().split())
    if divisor_y == 0:
        print('divisao impossivel')
    else:
        print(f'{dividendo_x / divisor_y}')

# 🎉🎉🎉🎉 ACEITO DE PRIMEIRA!!! 🎉🎉🎉🎉

# 1 - QUANTIDADE DE PROCEDIMENTOS A SEREM EXECUTADOS - O utilizador irá digitar a quantidade de vezes que a divisão será
# realizada.
# 2 - EXECUTANDO PROCEDIMENTO CONFORME A QUANTIDADE - Agora iremos realizar a divisão propriamente dita. Este é o
# coração do algorítmo. Fazemos isso através de um laço FOR com um range do tamanho de "quantidade". Depois criamos duas
# variáveis para o dividendo e para o divisor (dividendo_x e divisor_y) e recebemos as entradas por uma função map() e
# um split(). Em seguida usamos um IF e um ELSE. O primeiro é para apresentar a mensagem caso a divisão seja inpossível
# e a condição de ativação dessa condicional é se a variável divisor_y for igual a zero. Isso porque, matematicamente, é
# impossível dividir qualquer número por zero. O ELSE, no que lhe concerne, mostrará a divisão propriamente dita de
# dividendo_x por divisor_y através de uma impressão formatada.
