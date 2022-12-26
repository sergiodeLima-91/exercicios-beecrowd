# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que
# indique se estes valores foram digitados em ordem crescente ou decrescente.

# Entrada
# A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao
# ser fornecido valores iguais para X e Y.

# Saída
# Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário
# imprima a mensagem “Decrescente”.

# 1 ------------------------------------
ordem_geral = list()
# 2 ------------------------------------
while True:
    valor1,valor2 = map(int, input().split()) # 2.1
    if valor1 < valor2: # 2.2
        ordem_geral.append('Crescente')
    if valor1 > valor2: # 2.3
        ordem_geral.append('Decrescente')
    if valor1 == valor2: # 2.4
        for c in range(len(ordem_geral)):
            print(*ordem_geral[c],sep='')
        break

# 1 - LISTA QUE RECEBE RESULTADOS - No problema é pedido que os impressões sejam exibidos somente no final do processo,
# então resolvi criar uma lista para poder exibir os resultados no final
# 2 - CRIAÇÃO DE UM LAÇO INFINITO - A quantidade de vezes que o procedimento será realizado é incerta. Por isso é bom
# usar um laço infinito. Dentro deles executamos o procedimento completo de verificar se os valores digitados estão em
# ordem crescente ou decrescente e imprimira os valores no final.
# 2.1 - ENTRADAS - Variáveis valor1 e valor2 recebem as entradas por meio da função split() e a map() que automaticamente
# já converte o tipo primitivo texto para inteiro.
# 2.2 - CASO ORDEM SEJA CRESCENTE - Em seguida temos a primeira estrutura condicional para caso os valores estejam em
# ordem crescente. Nesse caso, a lista ordem_geral vai receber no último índice, pela função.append (que, no caso, é
# zero) o nome 'Crescente'. Isso ocorrerá todas as vezes em que a ordem for crescente. Assim, a lista sempre aumentará
# de tamanho conforme o número de casos caírem nesta condicional.
# 2.3 - CASO ORDEM SEJA DECRESCENTE - Esta estrutura condicional é ativada pelo caso oposto ao anterior. Se os valores
# estiverem em ordem decrescente a lista ordem_geral irá receber pela função.append a cadeia de caracteres "Decrescente".
# O processo se repete em todos os casos que couberem nesta estrutura.
# 2.4 - CONDIÇÃO DE PARADA DO LAÇO INFINITO - Aqui estabelecemos a condição de parada do laço infinito lá de cima. Caso
# as duas entradas sejam iguais, entraremos num laço de repetição FOR cujo tamanho é equivalente ao da lista ordem_geral.
# Fazemo isso por meio da função len(), que nos retorna o número equivalente a quantidade de índices presente nessa lista.
# O que o laço FOR vai repetir? ele vai printar cada um dos valores presentes na lista ordem_geral e isso é possível
# porque colocamos como referância do índice em "[]" o "c", que é a variável que percorre em ordem progressiva, começando
# do zero, nesse caso, todos os números dentro do limite do len() de ordem_crescente. Ora, precisamos começar do zero
# porque os índices da lista ordem_geral começam deste número. Porém, precisamos encontrar uma maneira de mostrar o
# conteúdo de cada índice sem os colchetes e aspas ('[Crescente') para que o código seja aceito pelo Beecrowd. Para isso
# é que usamos a função sep='' para que retiremos tanto as aspas quanto os colchetes.