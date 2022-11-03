#Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

#No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

# PASS A PASSO:
# 1 - Criar variáveis de entrada;
# 2 - Calcule a média com base nas notas dadas pelo enunciado do problema;

lista_1 = str(input())
lista_2 = lista_1.split()
N1 = float(lista_2[0])
N2 = float(lista_2[1])
N3 = float(lista_2[2])
N4 = float(lista_2[3])
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / (1 + 2 + 3 + 4)
print('Media: {:.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')
if media < 5:
    print('Aluno reprovado.')
if media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print(f'Nota do exame: {y}')
    if (media + y) / 2 >= 5:
        mf = (media + y) / 2
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mf))
    else:
        mf = (media + y) / 2
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(mf))

# O beecrowd em muitos casos de teste estava retornando o wrong answer(100%) ou runtime error. Era reportado que o erro era o "EOFErro: eof when reading a line". A função input que eu havia criado estava chegando no final do arquivo sem uma entrada. o código anterior ao de cima é este:

'''lista_1 = str(input())
lista_2 = lista_1.split()
N1 = float(lista_2[0])
N2 = float(lista_2[1])
N3 = float(lista_2[2])
N4 = float(lista_2[3])
media = ((N1 * 1) + (N2 * 2) + (N3 * 3) + (N4 * 4)) / (1 + 2 + 3 + 4)
print('Media: {:.1f}'.format(media))
if media >= 7:
  print('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
  print('Aluno em exame.')
  ne = float(input('Nota do exame: '))
  if (media + ne) / 2 >= 5:
    mf = (media + ne) / 2
    print('Aluno aprovado.')
    print('Media final: {:.1f}'.format(mf))
  else:
    mf = (media + ne) / 2
    print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(mf))
else:
  print('Aluno reprovado.')'''

# A parte que estava apresentando o EOFError era esta:

'''ne = float(input('Nota do exame: '))'''

# Então encontrei em um site um código que foi aprovado em resposta ao mesmo problema 1040 do beecrowd. Eis qual era o código:

'''x = input().split()
n1, n2, n3, n4 = x
m = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
if m < 5.0:
    print('Aluno reprovado.')
if 5.0 <= m <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    m2 = (y + m) / 2
    if m2 >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(m2))'''

# É um pouco diferente do meu e mais enxuto. Fui, verificar justamente a parte do código que correspondia ao meu e que estava dando o EOFError. Notei que o autor do código, ao contrário de mim, não criou uma variável com uma função imput() para armazenar de forma direta a Nota do exame solicitada pelo beecrowd como leitura. Ele criou outra variável (y, no caso) para armazenar esse dado e na linha seguinte fez referência a esta variável. Adaptei ao meu código e deu certo. Eis abaixo a parte da qual falo:

'''y = float(input())
    print('Nota do exame: {}'.format(y))'''

# Tudo foi resolvido e o código foi aprovado pelo beecrowd. Vivendo e aprendendo.

# VERSÃO FINAL APROVADA PELO SITE:

n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (1 + 2 + 3 + 4)
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
if media < 5:
    print('Aluno reprovado.')
if media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame}')
    if (media + exame) / 2 >= 5:
        mf = (media + exame) / 2
        print('Aluno aprovado.')
        print(f'Media final: {mf:.1f}')
    else:
        mf = (media + exame) / 2
        print('Aluno reprovado.')
        print(f'Media final: {mf:.1f}')