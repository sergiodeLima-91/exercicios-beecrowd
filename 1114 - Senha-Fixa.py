while True: # 1
    senha = int(input()) # 2
    if senha == 2002: # 3
        print('Acesso Permitido')
        break
    else: # 4
        print('Senha Invalida')

# 1 - Laço infinito porque não sabemos a quantidade de entradas que o utilizador irá digitar
# 2 - Variável que vai receber a senha
# 3 - Condicional que analisa se a senha digitada corresponde a 2002, que é a senha correta. Em caso positivo, a mensagem
# a seguir é apresentada e o programa é parado pelo comando break.
# Em caso contrário, a mensagem de senha inválida será apresentada e o programa, por meio do laço infinito, irá reiniciar
# o procedimento de entrada de dados e a verificação dos mesmos até que a senha digitada seja a correta.

