entrada = int(input())


def lines(entrada):
    elementos = [] # Vai receber todos os números, inclusive a palavra PUM.
    lista_quatro = [] # Recebe a palavra PUM
    count = 1
    # 1 --------------------------------
    for i in range(entrada * 4): # É vezes quatro porque temos quatro elementos por linha apresentada.: "1 2 3 PUM"
        elementos.append(i + 1) # Elementos vai recebera a variável "i" do FOR mais para que a contagem não comece em 0.
    # 2 --------------------------------
    for x in elementos:
        count += 1
        if count == 4:
            elementos[x] = "PUM" # Aqui, "x" tem o valor de quatro.
            count = 0 # Recebe zero porque é na quarta posição que PUM aparece
        lista_quatro.append(x) # Vai receber todos os elementos conforme o range de "elementos", inclusive PUM.
    # 3 --------------------------------
        if len(lista_quatro) == 4:
            print(lista_quatro[0], lista_quatro[1], lista_quatro[2], lista_quatro[3])
            lista_quatro = []


lines(entrada)

# 1 - INSERINDO ELEMENTOS NA LISTA PRINCIPAL(ELEMENTOS) - Isso foi feito provavelmente porque não é possível usar uma
# lista vazia. A lista "elementos" irá ser usada no segundo laço FOR. Ela iria ser usada como base do range.

# 2 - ORDENANDO ELEMENTOS - Este segundo FOR serve para realizar a contagem em si e inserir no índice quatro da lista
# "elementos" a palavra PUM. Por que no quarto? Porque a Palavra PUM aparece exatamente no quarto índice.

# 3 - FAZENDO OS PRINTS FINAIS - Agora que já colocamos os valores nos índices de lista_quatro, basta apresentar estes
# valores na ordem correta. Cada linha apresentada contém quatro valores, como já dito. Então precisamos mostrar sempre
# os valores dos índices de 0 a 3 dessa lista, já que o python desconsidera o último. No final, esvaziamos a lista com
# "lista_quatro = []" porque precisamos mostrar outra sequância nova de elementos.
# Apresentei dificuldades em imprimir os valores da lista_quatro sem as chaves e aspas. Ora, bastava retirar o format do
# print para poder fazer isso. Passei o dia quebrando a cabeça e tentando entender como fazer kkkkkkkkkkk