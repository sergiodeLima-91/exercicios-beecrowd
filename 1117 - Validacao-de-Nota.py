# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça
# com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser
# validada separadamente.

# Entrada
# A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas
# notas válidas.

# Saída
# Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
# Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor
# deve ser apresentado com duas casas após o ponto decimal.

while True:
    nota1 = 0
    nota2 = 0
    while True:
        nota1 = float(input())
        if nota1 < 0 or nota1 > 10:
            print('nota invalida')
        else:
            nota1 = nota1
            break
    while True:
        nota2 = float(input())
        if nota2 < 0 or nota2 > 10:
            print('nota invalida')
        else:
            nota2 = nota2
            break

    if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
        print(f'media = {(nota1 + nota2) / 2:.2f} ')
        break

# EXPLICAÇÃO DA LÓGICA INTERNA: A questão principal para resolver este problema foi entender que as notas válidas poderim
# ser pegas fora de ordem. Por exemplo, suponha que a primeira nota seja -1 e a segunda 5. Até agora temos somente uma nota
# válida por estar dentro do interválo de 0 a 10 (5), incluindo o próprio zero e dez, vale lembrar. Em seguida temos a
# entrada de 7. Ora, 7 é um número válido neste caso. Então, a média será feita com base em 5 e 7.