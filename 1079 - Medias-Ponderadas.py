# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3
# valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3
# valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.


# 1 - Entrada da quantidade de vezes que o programa vai receber o conjunto de três notas:
quantidade = int(input())
lista_menor = list()
lista_geral = list()
# 2 - Entrada e Separação das Notas:
for c in range(1, quantidade + 1):
    lista_menor = list(map(float, input().split()))
    lista_geral.append(lista_menor)




# 3 - Calculando a Media Ponderada:
contador1 = 0
contador2 = 0
medias = list()
while True:
    if contador1 != quantidade:
        media = ((lista_geral[contador1][0] * 2) + (lista_geral[contador1][1] * 3) + (lista_geral[contador1][2] * 5)) / (2 + 3 + 5)
        medias.append(media)
        contador1 += 1
        print(f'{medias[contador2]:.1f}')
        contador2 += 1
    if contador1 == quantidade:
        break
# Problema central: Como pegar cada uma das notas para fazer o cálculo?