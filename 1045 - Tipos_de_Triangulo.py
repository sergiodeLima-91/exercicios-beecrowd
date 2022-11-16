#PASSO 1 - CRIAÇÃO DAS VARIÁVEIS DE ENTRADA:
# Faremos isso usando a função split()
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

# Praticamente a totalidade deste código foi retirado de: http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1045-tipos-de-triangulos.html


# PASSO 2 - VERIFICAR QUAL DAS ENTRADAS É A MAIOR:

# Variáveis para verificar qual das entradas é a maior para poder colocar em A. O enunciado diz que devemos fazer com
# que A seja sempre o maior dos lados do triângulo.
n1 = float(0)
n2 = float(0)
n3 = float(0)

# Variáveis que recebem as entradas do PASSO 1
A = float(A)
B = float(B)
C = float(C)

# Estruturas condicionais para verificar qual das entradas é a maior:
if A >= B and A >= C:
    n1 = A
    if B >= C:
        n2 = B
        n3 = C
    else:
        n2 = C
        n3 = B
if B >= A and B >= C:
    n1 = B
    if A >= C:
        n2 = A
        n3 = C
    else:
        n2 = C
        n3 = A

if C >= A and C >= B:
    n1 = C
    if A >= B:
        n2 = A
        n3 = B
    else:
        n2 = B
        n3 = A

if A == B and B == C:
    n1=A
    n2=B
    n3=C

A = n1
B = n2
C = n3

# PASSO 3 - CALCULAR QUE TIPO DE TRIÂNGULO OS NÚMEROS FORMAM:

# Caso A seja maior ou igual a soma de B e C é impossível formar um triângulo.
if A >= (B + C):
    print('NAO FORMA TRIANGULO')
# Caso isso acima não ocorra, significa que tem como formar um triângulo com estes números, mas precisamos ver que
# tipo de triângulo é esse!
else:
    if (A ** 2) == (B ** 2 + C ** 2):
        print('TRIANGULO RETANGULO')
    if (A ** 2) > (B ** 2 + C ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (A ** 2) < (B ** 2 + C ** 2):
        print('TRIANGULO ACUTANGULO')
    if (A == B == C):
        print('TRIANGULO EQUILATERO')
    if A == B != C or B == C != A or A == C != B:
        print('TRIANGULO ISOSCELES')