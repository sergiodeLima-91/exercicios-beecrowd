# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

# Obs(Sérgio): A leitura dos passos é de cima para baixo.
# 1 - Variável que recebe o número com o qual iremos dividir os números do intervalo entre 1 e 10.000.
numero = int(input())
# 2 - Variável para receber os números que fazem parte do interválo entre 1 e 10.000.
cont = 1
# 3 - Laço infinito para avaliar, através de uma estrutura condicional, qual dos números entre 1 e 10.000 dividos por
# "numero" tem resto igual a 2. Como sempre, temos o incremento no laço while para que o valor de "c" mude e, assim,
# possamos avaliar o próximo número do intervalo.
while True:
    if cont % numero == 2:
        print(cont)
    cont += 1
    if cont == 10000:
        break