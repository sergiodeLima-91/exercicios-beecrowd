pares = 0
ímpares = 0
positivos = 0
negativos = 0
for c in range(0,5):
    entrada = int(input())
    if entrada % 2 == 0:
        pares += 1
    else:
        ímpares += 1
    if entrada > 0:
        positivos += 1
    elif entrada < 0:
        negativos += 1

print(f'{pares} valor(es) par(es)')
print(f'{ímpares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
