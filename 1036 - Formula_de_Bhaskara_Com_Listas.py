#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada: Leia três valores de ponto flutuante (double) A, B e C .

# Saída: Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

import math
delta_raiz = 0
R1 = 0
R2 = 0
lista_1 = str(input())
lista_2 = lista_1.split()
a = float(lista_2[0])
b = float(lista_2[1])
c = float(lista_2[2])
delta = (b**2) - 4 * a * c
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    delta_raiz = math.sqrt(delta)
    R1 = (-b + delta_raiz) / (2 * a)
    R2 = (-b - delta_raiz) / (2 * a)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))

# CÓDIGO ACEITO UHU!!!

# Outra maneira de resolver usando while:

'''num = int(input())
lista = [0,0,0]
lista[0] = num
pos = 2
while pos == 2:
    num = int(input())
    lista[1] = num
    pos += 1
num = int(input())
lista[2] = num
print(lista)''' # depois daqui viria o mesmo que na linha 13 até a 24 com as respectivas variáveis.
