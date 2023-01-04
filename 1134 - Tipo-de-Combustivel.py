# Variáveis:
gasolina = 0
alcool = 0
diesel = 0
parada = False # Condição de parada do laço infinito principal.

#Laço infinito principal:
while True:
    while True: # Laço infinito criado para repetir o processo de captação da opção escolhida pelo cliente.
        codigo = int(input())
        if codigo < 1 and codigo > 4:
            break
        else:
            if codigo == 1:
                alcool += 1
            elif codigo == 2:
                gasolina += 1
            elif codigo == 3:
                diesel += 1
            elif codigo == 4:
                parada = True
                break
    if parada == True:
        print('MUITO OBRIGADO')
        print(f'Alcool: {alcool}')
        print(f'Gasolina: {gasolina}')
        print(f'Diesel: {diesel}')
        break


