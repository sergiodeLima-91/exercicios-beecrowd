#Leia um valor inteiro N.
# Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
# mostrando essas informações.

dentro = 0
fora = 0
numero = 0
quantidade = int(input())
for c in range(1, quantidade + 1):
    numero = int(input())
    if numero >= 10 and numero <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')

# Acertei de PRIMEIRA!!!