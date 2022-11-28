# Retirado de: http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1051-imposto-de-renda-em.html


# PASSO 1 - ENTRADAS
# Variável que recebe o salário do cara.
salario = float(input())

# PASSO 2 - CASO DE ISENÇÃO DE IMPOSTO:
# Basta colocar na condicional que o salário precisa ser menor que 2000.00 para haver isenção, pois subentende-se
# que o interválo inicial é 0:
if salario <= 2000.00:
    imposto = 0
    print('Isento')

# PASSO 3 - CASO DE COBRANÇA DE 8% DE IMPOSTO:
# Se dois mil for menor que salário "e" salário for menor ou igual a três mil, a variável salario8 vai receber o salário
# menos dois mil. O cálculo para a retirada do imposto é feito pelo excesso do limite estabelecido. Por exemplo, se
# o indivíduo tem um salário de dois mil e cem, será retirado 8% de cem que é o excesso dp limite de dois mil.
if salario>= 2000.00 and salario <= 3000.00:
    salario8 = salario - 2000.00
    imposto = salario8 * (8 / 100)

# PASSO 4 - CASO DE COBRANÇA DE 18% DE IMPOSTO:
# Aqui precisamos somar 8% de 1000.00 com 18% do excesso do salário. Então, o imposto final vai ser o excesso do limite
# multiplicado por 18 vezes 100 (para retirar a porcentagem do excesso presente em "salario18") somado a 8% de 1000
if salario >= 3000.00 and salario <= 4500.00:
    imposto8 = (8 / 100) * (1000.00)
    salario18 = salario - 3000.00
    imposto = salario18 * (18 / 100) + imposto8

# PASSO 5 - CASO DE COBRANÇA DE 28% DE IMPOSTO:
# Aqui, o imposto final será a soma de 18% do escesso de 3000 mais 8% de mil mais 28% do escesso de 4500.
if salario > 4500.00:
    imposto8 = (8 / 100) * 1000.00
    imposto18 = (18 / 100) * (1500.00)
    salario28 = salario - 4500.00
    imposto = imposto18 + imposto8 + salario28 * (28 / 100)

# PASSO 6 - PRINTAR O RESULTADO:
# Por que usamos um IF para poder printar os resultados? É somente para que, caso o resultado seja isento o número
# presente na variável "imposto" não seja apresentado junto com "Isento" e acarrete uma desaprovação do Beecrowd.
if salario > 2000.00:
    imposto = float(imposto)
    print(f'R$ {imposto:.2f}')