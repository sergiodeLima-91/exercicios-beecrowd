# Retirado de: http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1099-soma-de-impares.html

# 1
quantidade = int(input())
d = 0 # Variável que vai servir de contador no ranges a seguir. Teve que ser declarada aqui por causa do escopo.
# 2
for c in range(1 , quantidade + 1):
    a, b = map(int, input().split())
    s=0

    # 3
    if a > b:
        for d in range(int(b)+1, int(a)):
            if d % 2 != 0:
                s = s + d
    if a < b:
        for d in range(int(a)+1, int(b)):
            if d % 2 != 0:
                s = s + d
    if a == b:
        s = 0
    # 4
    print(s)

# 1 - Entrada da quantidade de vezes que a operação será realizada
# 2 - Laço FOR para pegar as variáveis de entrada para o interválo.
# 3 - Em seguida temos três conjuntos de condicionais. As duas primeiras fazem a mesma coisa: verificam se o número é
# ímpar e, em caso positivo, incrementam este valor na variável "s" com "d". A tereceira serve para atribuir
# zero à variável "soma" no caso de A e B serem iguais. Isso ocorre porque significa não haver há intervalo entre a e b
# para ser analisado. Essas duas variáveis servem para colocar os números em ordem crescente, visto que as
# duas primeiras condicionais servem para determinar qual é o maior dos dois valores.
# 4 - No final temos o print da variável "s" que contém a soma dos números ímpares de cada interválo.

# CONSIDERAÇÕES FINAIS:
# No final das contas, acredito que minha solução não deu certo porque pensei demais. A solução poderia ser extremamente
# simples. Porém, isso não é regra. Nem sempre a solução de um problema será simples em relação ao tamanho de código,
# porque, em resumo, a questão foi resolvida com três laços FOR, três IFs e um print! Tem que estudar mais mesmo.