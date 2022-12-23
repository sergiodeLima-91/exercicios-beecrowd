#Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).

# Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo
# o N e M).

#Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número
# nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

# 1 - Criando laço infinito para pegar os valores, já que eu não sei quantas vezes o procedimento será realizado.
while True:
    soma = 0
    valor1, valor2 = map(int, input().split())
    if valor1 == 0 or valor1 < 0 or valor2 == 0 or valor2 < 0:
        if valor1 == 0:
            print()
            break
        elif valor1 < 0:
            print(valor1)
            break
        elif valor2 == 0:
            print()
            break
        elif valor2 < 0:
            print(valor2)
            break
    if valor1 > valor2:
        for c in range(1, valor1 + 1):
            print(f'{valor2} ',end='')
            soma += valor2
            valor2 += 1
            if valor2 > valor1:
                print(f'Sum={soma}')
                valor1 = valor2 = 0
                break
    if valor2 > valor1:
        for c in range(1, valor2 + 1):
            print(f'{valor1} ',end='')
            soma += valor1
            valor1 += 1
            if valor1 > valor2:
                print(f'Sum={soma}')
                valor1 = valor2 = 0
                break
