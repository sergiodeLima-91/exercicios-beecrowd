import math # Importar a biblioteca math para usar a funcionalidade "trunc" a fim de separa a parte inteira dos números de sua parte em decimal.
n = int(input()) # Variável de entrada de dados.
horas = n / 3600 # O resto que sobrar das divisões inteiras de "n" serão jogadas para as demais casas decimais do tempo (minutos e horas). É quase que literalmente "deixar o resto para o próximo" srsrs.
resto = n % 3600
minutos = resto / 60
segundos = resto % 60
print('{}:{}:{}'.format(math.trunc(horas),math.trunc(minutos),math.trunc(segundos)))

# Este código foi retirado do seguinte canal do You Tube:
# https://www.youtube.com/watch?v=mpOHIUNfLhc