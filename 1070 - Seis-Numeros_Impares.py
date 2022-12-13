impares = 0
entrada = int(input())
for c in range(1,13):
    if not entrada % 2 == 0:
        impares = entrada
        print(impares)
    entrada += 1