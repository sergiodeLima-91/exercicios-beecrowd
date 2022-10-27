a, b, c = map(int, input().split())
for cont in range(1, 4):
    if cont == 1:
        menor = medio = maior = a
    if a > b and a > c:
        maior = a
        if b > c:
            medio = b
            menor = c
        else:
            medio = c
            menor = b
    if b > a and b > c:
        maior = b
        if a > c:
            medio = a
            menor = c
        else:
            medio = c
            menor = a
    if c > a and c > b:
        maior = c
        if a > b:
            medio = a
            menor = b
        else:
            medio = b
            menor = a
print(menor)
print(medio)
print(maior)
print()
print(a)
print(b)
print(c)