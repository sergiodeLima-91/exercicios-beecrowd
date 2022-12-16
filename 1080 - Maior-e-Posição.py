# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

cont = 1 # Variável para contar os passos. Vamos começar em um porque o enunciado nos transmite que tudo começa por ele.
posição = 1 # Posição do maior número digitado dentre os 100.
maior = 0 # Variável que recebe o maior número entre os 100 digitados.
# VERIFICAÇÃO DO MAIOR NÚMERO ATRAVÉS DE UM LAÇO FOR:
#LÓGICA INTERNA: Primeiro criamos o laço de repetição para receber todas as cem entradas digitadas pelo usuário.
# Coloquei de 0 até 102 somente por questões de lógica interna mesmo, não tem tanta relevância. Eu poderia ter colocado
# também de 1 até 103, daria no mesmo. Em seguida criamos a variável de entrada chamada "número". Em seguida pegamos
# esta mesma variável e fazemos a verificação se o valor digitado nela é maior do que o valor presente na variável "maior".
# Caso isso ocorra, a própria variável "maior", que tem valor zero, valor de "numero". Dentro deste primeiro IF também
# colovamos um incremento para a variável "posição", porque, já que encontramos um número que é maior do que os outros
# digitados até agora, temos que especificar a posição dele. Ora, a posição começa em um e isso porque o primeiro valor
# digitado sempre é o maior de todos, visto que só tem ele. É impossível dizer que uma pessoa é feia sem que haja outro
# padrão de beleza para poder comparar, concorda? Caso o número seguinte não seja maior do que o anterior, o programa
# passa direto por este IF e o incremento não é realizado, o que significa que o número anterior ainda continua sendo
# o maior de todos.
# Em seguida temos o incremento da variável "cont", que evidentemente, só foi criada para compor a segunda condicional.
# A segunda condicional foi criada somente para mostrar o maior número na tela e a posição na qual ele se encontra,
# conforme o enunciado pede. A primeira vista, eu concordo que essa condicional ai parece redundante, na realidade,
# visto que já temos o laço FOR que nesse caso não é infinito e já tem limite de parada que é o número 102 (na verdade
# 101, porque o Python exclui sempre um número). O "break" no final também está um pouco redundante, aparentemente, mas
# isso nunca é demais quando queremos evitar erros em nossos códigos,né? kkkkk
for c in range(0, 102):
    numero = int(input())
    if numero > maior:
        maior = numero
        posição = cont
    cont += 1
    if cont == 101:
        print(maior)
        print(posição)
        break