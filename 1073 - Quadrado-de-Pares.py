entrada = int(input()) # Entrada do número final
pares = 0 # Variável que vai receber os números pares
contador = 1 # Para receber os números que serão avaliados como pares ou não.

for c in range(1, entrada + 1): # Laço de repetição partindo de 1 até o número fornecido na "entrada" que é o limite.
    if contador % 2 == 0: # Condicional para verificar se o número presente em "contador" é par.
        pares = contador # Recebe o valor presente em "contador" caso este seja par.
        print(f'{contador}^2 = {contador ** 2} ') # Para mostrar o quadrado do número presente em "contador"
    contador += 1 # Para somar 1 na variável "contador" a fim de que a contagem continue e ela possa ser avaliada
                  # novamente e saber se o novo número é par ou não.
