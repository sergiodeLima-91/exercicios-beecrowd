# Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X
# e Y, incluindo ambos.

# Entrada
# O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

# Saída
# Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se
# for o caso.

# 1 - Variáveis:
entrada_x = int(input()) # Primeira entrada
entrada_y = (int(input()))# Segunda entrada
maior = 0 # Recebe maior número dentre as entradas acima
menor = 0 # Recebe o menor número dentre as entradas acima
soma = 0 # Soma de todos os números que não são múltiplos de 13

# 2 - Colocando as entradas em ordem crescente. Fica mais fácil de fazer o cálculo se os números estiverem assim.
maior = entrada_x if entrada_x > entrada_y else entrada_y # 2.1
menor = entrada_y if entrada_y < entrada_x else entrada_x # 2.2

# 3 - Laço para calcular se os números entre menor e maior são multiplos de 13:
while True:
    if menor %13 != 0: # 3.1
        soma += menor
    menor += 1
    if menor > maior:
        print(soma)
        break

# 2.2 - Verbalização lógica da expressão: Maior vai receber entrada_x se entrada_x for maior que entrada_y. Caso contrário,
# Maior vai receber entrada_y (e será o maior número por consequência).
# 2.2 - A mesma lógica explicada acima vale para cá.
#3.1 - Um número só é múltiplo de outro caso a divisão do primeiro pelo segundo resulte em resto zero, isto é, o quociente
# precisa ser um número inteiro. Caso "menor" se encaixe nesse caso, "soma" irá receber um incremento de menor e, fora do IF,
# "menor" irá receber um incremento de 1 para que sigamos com a sequência de números no limite da variável "maior".
# O IF seguinte servirá para parar o laço while True com a imprssão da soma de todos os números não múltiplos de 13 presente
# em "soma" e por meio do break.