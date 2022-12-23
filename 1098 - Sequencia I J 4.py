
# Retirado de: http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1098-sequencia-ij-4-solucao.html

i = 0
j = 1
acrescimo = (0.2) # 1
n = 0
while i <= 2: # 2
    for c in range(1,4): # 3
        if i > 2.19: # 4
            print('I={:.0f} J={:.0f}'.format(2,j))
        if i == 1.0 or i == 0.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i,j))
        elif i < 2:
            print('I={:.1f} J={:.1f}'.format(i,j))
        j = j + 1
    i = i + acrescimo
    j = 1 + i

# Lógica interna:
# 1 - Variável que recebe o acréscimo flutuante, que no caso dessa sequênci lógica, é 0.2.
# 2 - Laço while para realizar o procedimento completo até que "i" tenha valor dois. Inclusive o que limita a execução
# deste código é justamente esta variável.
# 3 - Se pararmos para analisar, veremos que a quantidade em que os números se repetem em sequência de linhas diferentes
# são três. É por isso que este FOR tem range de tamanho três (já que o python exclui sempre o último 'loop').
# 4 - Irei continuar o raciocínio depois rsrsrsr