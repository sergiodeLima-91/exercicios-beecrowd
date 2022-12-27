def media(nota1,nota2):
    nota1 = n1 * 0.35
    nota2 = n2 * 0.75
    media = (nota1 + nota2) / 1.1
    return f'MEDIA = {media:.5f}'


# Main Part
n1 = float(input())
n2 = float(input())
print(media(n1,n2))