A, B = map(int, input().split())
if B % A == 0 or A % B == 0: # Eu coloquei estes dois casos para que não haja divisor maior que dividendo.
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
