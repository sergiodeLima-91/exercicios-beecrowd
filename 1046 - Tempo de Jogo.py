# PASSO 1 - CRIAÇÃO DAS VARIÁVEIS DE ENTRADA MEDIANTE SPLIT():
inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)

# PASSO 2 - VERIFICANDO O TEMPO DE JOGO:
# Vamos fazer isso através de uma estrutura condicional.
# Neste primeiro IF vamos verificar caso o número de início do jogo seja menor que o número de fim dele:
if inicio < fim:
    tempo = fim - inicio

# No ELSE é se o fim do jogo FOR MAIOR DO QUE O INÍCIO. Nesse caso precisamos fazer um cálculo com subtração e soma.
# Primeiro faremos a subtração 24 menos a hora de início do jogo, isso porque o enunciado diz que o formato de horas
# abordado é 24.
# Por que temos que fazer isso? Porque precisamos saber QUANTAS HORAS PASSARAM-SE DENTRO DO MESMO DIA EM QUE O JOGO
# OCORREU. Dizer que o número de início é maior do que o do fim significa que o jogo durou até o dia seguinte, além
# das fronteiras de 24 horas do dia em que começou.

# Suponha que um jogo entre Flamengo e Fluminente começou às 22 horas de uma quarta-feira e terminou às 2 da madrugada
# de uma quinta. Ora, o número de início é menor do que o do fim. Precisamos ver quanto tempo passou na quarta e somar
# com o que passou na quinta, sabendo que a quinta é um novo dia. É isso o que fazemos abaixo:

else:
    tempo = (24 - inicio) + fim
print(f'O JOGO DUROU {tempo} HORA(S)')