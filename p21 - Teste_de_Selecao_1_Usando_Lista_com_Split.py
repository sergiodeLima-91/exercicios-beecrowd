# Leia 4 valores inteiros A, B, C e D. A seguir:
# Escreva "Valores aceitos" SE:
    # B for maior do que C
    # D for maior do que A
    # a soma de C com D for maior que a soma de A e B
    # C e D, ambos, forem positivos
    # a variável A for par.
# Senão, escrever "Valores nao aceitos".

lista = str(input())
lista_2 = lista.split()
A = int(lista_2[0])
B = int(lista_2[1])
C = int(lista_2[2])
D = int(lista_2[3])
if B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and (A % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
