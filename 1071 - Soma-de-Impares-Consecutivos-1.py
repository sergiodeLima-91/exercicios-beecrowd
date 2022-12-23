entrada1 = int(input())
entrada2 = int(input())

maior = entrada1 if entrada1 > entrada2 else entrada2 # > A variável "maior" vai receber o valor de "entrada1" caso a mesma variável "entrada1" seja maior que "entrada2". O contrário vai significar que o valor de "entrada2" é maior e ele será atribuído a variável "maior".
menor = entrada2 if entrada2 < entrada1 else entrada1 # A lógica da estrutura anterior aplica-se aqui, sendo que
# queremos saber qual é o número menor.
menor += 1 # Variável que soma um à menor porque precisamos chegar até o segundo número maior.
soma = 0 # Variável que irá somar os números ímpares

while menor < maior: # Laço de repetição que começa em ordem crescente conforme o valor das variáveis.
    if menor % 2 != 0: # Verificação se o número é ímpar
        soma += menor # Variável "soma" recebe o número ímpar presente em "menor"
    menor += 1 # "Menor" recebe mais um para que passe ao número seguinte.
    print(menor)
print(soma)

# Uma coisa que o enunciado do problema não diz é que as extremidades não são verificadas para que saibamos se são
# ímpares ou não. No exemplo de saída cujo primeiro número é 15 e o outro é 12, nenhum deles é avaliado e sim aqueles
# que estão no intervalo entre eles (13, 14).