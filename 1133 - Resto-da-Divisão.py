entrada_x = int(input())
entrada_y = int(input())
soma = list()
contador = 0
maior = entrada_x if entrada_x > entrada_y else entrada_y
menor = entrada_y if entrada_y < entrada_x else entrada_x
menor += 1

# Laço infinito para cálculo:
while True:
    if menor %5 == 2 or menor %5 == 3:
        soma.append(menor)
        contador += 1
    menor += 1
    if menor == maior:
        for cont in range(contador):
            print(f'{soma[cont]}')
        break

# 🎉🎉🎉 Aceito de PRIMEIRA! 🎉🎉🎉