# Retirado de: http://muitomaiscodigoss.blogspot.com/2018/05/uri-problema-1118-varias-notas-com.html

# 1 -------------------------------
nota_soma = 0
cont = 0
continuar = True
# 2 -------------------------------
while continuar == True:
    nota = float(input())
# 3 -------------------------------
    if nota >= 0.0 and nota <= 10:
        nota_soma += nota
        cont += 1
# 4 -------------------------------
        if cont == 2:

            print("media = %.2f" % (nota_soma / 2))
            cont = 0
            nota_soma = 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                novo = int(input())
                if novo == 2:
                    continuar = False
                    break
                elif novo == 1:
                    continuar = True
                    break

    else:
        print("nota invalida")



# 1 - CRIAÇÃO DE VARIÁVEIS -  A variável "nota_soma" vai servir para somar as notas a para depois realizarmos o cálculo
# da média. A variável "cont" vai servir para entrarmos no "if cont == 2:". O procedimento realizado nele são dois: o
# cálculo da média já com a apresentação da impressão dela e a apresentação do menu de repetição ou encerramento do
# programa. A variável "continuar" serve como condição de parada ou perpetuação do laço principal "while continuar == True:"

# 2 - LAÇO INFINITO PRINCIPAL - Executa todos os procedimentos completamente: recebe condicionais e laços de repetição
# para captação de informações por árte do utilizador para que o cálculo seja efetuado.

# 3 - CONDICIONAL PARA VALIDAÇÃO DAS NOTAS - Aqui, o construtor do código simplesmente colocou está condicional cuja
# ativação depende se as notas fornecidas estão no interválo entre 0 e 10. O ELSE no final do código é para caso isso não
# seja satisfeito e a mensagem "nota invalida" seja exibida. Quando isso ocorrer o laço while principal será reinicializado,
# já que a variável "continuar" ainda tem valor booleano False e esta mesma condicional da qual estamos falando aqui também
# será ativada de novo. Vale descatacar que foi usada somente uma variável (nota) para entrada das notas. Quando este
# primeiro valor for digitado pelo utilizador, dentro do IF será feito um incremento a variável "cont" e ela receberá um.
# Também será somada a variável "nota_soma" o valor de "nota".
# O laço será repetido completamente depois disso porque a condição de ativação do IF seguinte é que a variável "cont"
# tenha valor dois e não um.

# 4 - CONDICIONAL PARA CÁLCULO DA MÉDIA E MENU DO CÓDIGO - Na segunda vez que o laço "while continuar == True:" for
# percorrido, a variável "cont" já vai ter valor dois e esta condicional aqui será ativada. O que ocorrerá dentro dela?
# Primeiro, será realizado o cálculo da média usando somente a variável "nota_soma" dividida por dois. Dentro da impressão
# temos a referenciação a esta mesma variável. Em seguida, já que fizemos a execução da essância do algorítmo (apresentar
# o cálculo da média), vamos para a apresentação do menu de repetição ou encerramento de nosso programa. Como não temos
# certeza de quantas vezes o utilizador poderá inserir valores inválidos, usamos aqui um laço infinito. Dentro desse laço
# é apresentada a mesagem como menu "novo calculo (1-sim 2-nao)". Em seguida temos a variáveç "novo" para servir de forma
# de ativação da condicional seguinte. Este IF seguinte é para parar o código caso o valor de "novo" seja dois. Isso é
# feito pela atribuição do booleano False a "continuar" e, como já dito, a condição para que o laço principal continue
# rodando é que esta variável tenha valor True. O brake que se segue é para parar o laço infinito local no qual esta
# condicional que tratamos está inserida. Logo em seguida, temos um ELSE e ele serve para conrinuar o processo do laço
# principal e o brake serve para parar o laço infinito local.

# CONSIDERAÇÕES FINAIS: Faltou clareza do enunciado em dizer que a entrada de seleção do menu era colocada na linha
# seguinte. Eu estava colocando na mesma linha e o erro era esse. Tanto é que testei novamente somente colocando
# a variável "validação" do meu código como input() na linha seguinte depois da impressão do menu "novo calculo (1-sim 2-nao)"
# Eis meu código abaixo:

while True:
    nota1 = 0
    nota2 = 0
    validador = 0
    nao = False

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
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        print(f'media = {(nota1 + nota2) / 2:.2f}')

    while nao == False:
        print('novo calculo (1-sim 2-nao)') # Esta é a parte que foi alterada.
        validação = int(input())
        if validação == 1:
            break
        if validação == 2:
            nao = True
    if nao == True:
        break
