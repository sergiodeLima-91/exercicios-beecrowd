# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os
# experimentos de um laboratório o qual ela é responsável. (todo)Ela quer saber no final do ano, quantas cobaias foram
# (todo)utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela
# sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias
# utilizadas em cada experimento.

# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso
# de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere
# Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).
#
# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em
# relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

quantidade = int(input())
total_animais = 0
numero_testes = 0
coelhos = 0
ratos = 0
sapos = 0
for c in range(1, quantidade + 1):
    lista1 = input().upper()
    lista2 = lista1.split()
    numero_testes += int(lista2[0])
    total_animais = numero_testes
0
    if 'C' in lista2[1]:
        coelhos += int(lista2[0])
    elif 'S' in lista2[1]:
        sapos += int(lista2[0])
    elif 'R' in lista2[1]:
        ratos += int(lista2[0])

print(f'Total: {total_animais} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')

print(f'Percentual de coelhos: {(coelhos * 100) / total_animais:.2f} %')
print(f'Percentual de ratos: {(ratos * 100) / total_animais:.2f} %')
print(f'Percentual de sapos: {(sapos * 100) / total_animais:.2f} %')
