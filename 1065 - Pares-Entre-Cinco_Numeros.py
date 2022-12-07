pares = 0
for c in range (0, 5):
  entrada = float(input())
  if entrada % 2 == 0:
    pares += 1
print(f'{pares} valores pares')