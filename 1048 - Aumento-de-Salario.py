salario = float(input())
percentual = 0

if salario >= 0 and salario <= 400.00:
  reajuste = (15 * salario) / 100
  percentual = 15
elif salario >= 400.01 and salario <= 800.00:
  reajuste = (12 * salario) / 100
  percentual = 12
elif salario >= 800.01 and salario <= 1200.00:
  reajuste = (10 * salario) / 100
  percentual = 10
elif salario >= 1200.01 and salario <= 2000.00:
  reajuste = (7 * salario) / 100
  percentual = 7
else:
  reajuste = (4 * salario) / 100
  percentual = 4

print(f'Novo salario: {salario + reajuste:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')