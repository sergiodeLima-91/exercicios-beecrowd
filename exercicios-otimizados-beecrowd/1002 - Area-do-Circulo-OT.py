# Area = n.raio²
# n = 3.14159

def area(raio):
    n = 3.14159
    calculo = (raio ** 2) * n
    return f'A={calculo:.4f}'


# Main Part
entrada = float(input())
print(area(entrada))