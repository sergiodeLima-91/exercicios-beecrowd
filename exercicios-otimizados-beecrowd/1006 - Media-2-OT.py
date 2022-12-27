def media(nota1,nota2,nota3):
    nota1 = n1 * 2
    nota2 = n2 * 3
    nota3 = n3 * 5
    media = (nota1 + nota2+ nota3) / (3 + 2 + 5)
    return f'MEDIA = {media:.1f}'


# Main Part
n1 = float(input())
n2 = float(input())
n3 = float(input())
print(media(n1,n2,n3))