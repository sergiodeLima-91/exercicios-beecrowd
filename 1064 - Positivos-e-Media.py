positivos = 0
soma = 0
for c in range (0, 6):
  entrada = float(input())
  if entrada > 0:
    positivos += 1
    soma += entrada
print(f'{positivos} valores positivos')
print(f'{soma / positivos:.1f}')