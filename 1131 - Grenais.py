# Entrada com split() que recebe número de gols do Inter e do Grêmio
parar = False
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
while parar == False:
    quantidade_grenais = 1
    while True:
        inter, gremio = map(int, input().split())
        if inter > gremio:
            vitorias_inter += 1
        elif gremio > inter:
            vitorias_gremio += 1
        elif inter == gremio:
            empates += 1
        print('Novo grenal (1-sim 2-nao)')
        resposta_menu = int(input())
        if resposta_menu == 1:
            quantidade_grenais += 1
        elif resposta_menu == 2:
            parar = True
            break
    if parar == True:
        print(f'{quantidade_grenais} grenais')
        print(f'Inter:{vitorias_inter}')
        print(f'Gremio:{vitorias_gremio}')
        print(f'Empates:{empates}')
        if vitorias_inter > vitorias_gremio:
            print('Inter venceu mais')
        elif vitorias_gremio > vitorias_inter:
            print('Gremio venceu mais')
        else:
            print('Nao houve vencedor')
        break

# Aceito depois de três tentativas. Correção de erros ligados as impressões no final. Havia espaços desnecessários não
# solicitados pelo enunciado.