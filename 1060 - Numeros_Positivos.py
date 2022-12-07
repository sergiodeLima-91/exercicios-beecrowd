positivos = 0
for c in range(0, 6):
  entrada = float(input())
  if entrada > 0:
    positivos += 1
print(f'{positivos:.0f} valores positivos')