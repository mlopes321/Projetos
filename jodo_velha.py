"""
Esse código implementa um jogo da velha em que dois jogadores (representados por "X" e "O") podem jogar alternadamente até que 
alguém vença ou ocorra um empate. 
O tabuleiro é exibido após cada jogada e as posições são especificadas pelo número da linha e da coluna (0 a 2). 
O programa verifica se houve uma vitória ou empate a cada jogada.
"""
# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|", end=" ")
        for elemento in linha:
            print(elemento, end=" ")
        print("|")
    print()

# Função para verificar se alguém venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(elemento == jogador for elemento in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[i][coluna] == jogador for i in range(3)):
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

# Função para jogar
def jogar_jogo_da_velha():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Digite o número da linha (0 a 2): "))
        coluna = int(input("Digite o número da coluna (0 a 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print("Jogador", jogador_atual, "venceu!")
                break
            elif jogadas == 9:
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")

# Iniciar o jogo
jogar_jogo_da_velha()
