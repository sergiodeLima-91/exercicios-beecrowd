
# Código retirado de:http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1047-tempo-de-jogo-com.html

# PASSO 1 - CRIAR VARIÁVEIS DE ENTRADA COM SPLIT():
entradas = input().split()
hi, mi, hf, mf = entradas

hi = int(entradas[0])
mi = int(entradas[1])
hf = int(entradas[2])
mf = int(entradas[3])

# PASSO 2 - CRIAR CADEIA DE IFs PARA DETERMINAR QUANTIDADE DE HORAS E MINUTOS:

# Primeiro fazemos para caso a hora inicial seja menor do que a final. Podemos já deixar a dentro da mesma estrutura
# a que irá avaliar quantos minutos se passaram.
if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        # Se o minuto inicial for maior do que o final quer dizer que não passou uma hora ainda! Por isso devemos
        # subtrair um da variável "h" que armazena as horas totais.
        h = h - 1
        m = (60 - mi) + mf
        # Se o minuto incial for igual ao final quer dizer que não houve minutos, mas uma hora completada (60 minutos).
    if mi == mf:
        m = 0

# Cadeia de IFs para caso a hora inicial for MAIOR do que a FINAL. É segue quase a mesma lógica da estrutura anterior,
# só que a condicional é hi ser maior do que hf.
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
    if mi == mf:
        h = 24
        m = 0

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')