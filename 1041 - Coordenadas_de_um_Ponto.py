# 1 - Leia 2 valores com uma casa decimal (x e y);
# 2 - Estes valores devem representar as coordenadas de um ponto em um plano.
# 3 - Determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

# Criando duas variáveis de entrada para ler os dois valores.

lista1 = str(input())
lista2 = lista1.split()
x = float(lista2[0])
y = float(lista2[1])

# Como representar os quadrantes dos eixos x e y? Ambos são compostos por números de natureza positiva e negativa. Então basta colocá-los nesta ordem em cada eixo dentro de uma variável. Necessário entender o seguinte, seguindo um raciocínio lógico:

# Quadrante 1: X - POSITIVO e Y - POSITIVO
# Quadrante 2: X - NEGATIVO e Y - POSITIVO
# Quadrante 3: X - NEGATIVO e Y - NEGATIVO
# Quadrante 4: X - POSITIVO e Y - NEGATIVO

# Portanto, para determinar em qual quadrante as coordenadas estarão:

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')

# Caso as coordenadas mostrem que um dos pontos está sobre um dos eixos:

if x == 0 and y > 0:
    print('Eixo X')
elif x == 0 and y < 0:
    print('Eixo X')
elif y == 0 and x > 0:
    print('Eixo Y')
elif y == 0 and x < 0:
    print('Eixo Y')
elif x == 0 and y == 0:
    print('Origem')

# Outro código retirado de http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1041-coordenadas-de-um.html para verificar porque eu estou errando.

'''p = input().split()
x, y = p

x = float(x)
y = float(y)

if x == 0:
    if y == 0:
        print('Origem')
    if y != 0:
        print('Eixo Y')
if y == 0:
    if x != 0:
        print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
if x < 0:
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')'''