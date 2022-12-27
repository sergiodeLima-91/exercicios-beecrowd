# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
# Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas
# coordenadas for NULA (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.


# 1 --------------------------------
while True:
    coordenada_X, coordenada_Y = map(int, input().split()) # 2 --------------------------------
    # 3 --------------------------------
    if coordenada_X == 0 or coordenada_Y == 0:
        break
    else:
        if coordenada_X > 0 and coordenada_Y > 0:
            print('primeiro')
        elif coordenada_X < 0 and coordenada_Y > 0:
            print('segundo')
        elif coordenada_X < 0 and coordenada_Y < 0:
            print('terceiro')
        elif coordenada_X > 0 and coordenada_Y < 0:
            print('quarto')

# 1 - CONSTRUINDO "LOOP" DE ENTRADAS - Como sempre, neste problema não sabemos a quantidade de vezes que o
# procedimento será executado.
# 2 - COORDENADAS DO PLANO - Recebemos aqui as coordenadas para determinarmos a qual quadrante as coordenadas perntencem.
# 3 - CADEIA DE IFs - Esta cadeia de condicionais contém a condição de parada do "loop" infinito while True logo no início.
# Depois temos o caso contrário que trata dos quadrantes. A partir daí será determinado a qual quadrante as coordenadas
# fornecidas pertencem. Isso é feito conforme o caráter do número: positivo ou negativo. Como assim? Basta observar que,
# no quadrante um, x é positivo e y também. No quadrante dois, x é negativo e y positivo. No três, x é negativo e y também.
# Por fim, no quarto x é positivo e y negativo. Logo, podemos deixar as condicionais alinhadas com estas caracterísitcas.
