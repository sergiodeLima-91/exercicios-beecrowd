# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar. Ver a imagem nomeada de "exercicio-1038.png" para mais detalhes.

#Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima(exercicio-1038.png).

#Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

lista_1 = str(input())
lista_2 = lista_1.split()
cod = int(lista_2[0])
quant = int(lista_2[1])
calc = 0
if cod == 1:
    calc = quant * 4
elif cod == 2:
    calc = quant * 4.50
elif cod == 3:
    calc = quant * 5
elif cod == 4:
    calc = quant * 2
elif cod == 5:
    calc = quant * 1.50
print('Total: R$ {:.2f}'.format(calc))

# Aceito DE PRIMEIRA pelo beecrowd Uhu!!!
