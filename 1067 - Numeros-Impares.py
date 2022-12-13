entrada = int(input())
impares = 0
for c in range(1,entrada + 1):
    if not c % 2 == 0:
        impares = c
        print(impares)