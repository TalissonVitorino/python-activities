import os

def limpa():
    # Detecta se o sistema operacional e executa o comando correto!
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas operacionais (Linux, macOS, etc.)
        os.system('clear')

def desenhar_board(board):
    limpa()
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print()

def pos_valida(jogadas):
    while True:
        try:
            pos = int(input('Escolha uma posição (0-8): '))
            if pos in jogadas:
                return pos
            else:
                print("Posição inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 0 e 8.")

def jogar(board, marca, jogadas):
    pos = pos_valida(jogadas)
    board[pos] = marca
    jogadas.remove(pos)
    desenhar_board(board)

def ganhou(board):
    return ((board[0] == board[1] == board[2] != ' ') or
            (board[3] == board[4] == board[5] != ' ') or
            (board[6] == board[7] == board[8] != ' ') or
            (board[0] == board[3] == board[6] != ' ') or
            (board[1] == board[4] == board[7] != ' ') or
            (board[2] == board[5] == board[8] != ' ') or
            (board[0] == board[4] == board[8] != ' ') or
            (board[2] == board[4] == board[6] != ' '))

def game():
    nome1 = input("Digite o nome do jogador 1: ")
    nome2 = input("Digite o nome do jogador 2: ")

    board = [' '] * 9
    jogadas = list(range(9))
    desenhar_board(board)

    for i in range(9):
        # Alterna os jogadores
        if i % 2 == 0:
            marca = 'O'
            jogador_atual = nome1
        else:
            marca = 'X'
            jogador_atual = nome2

        print(f"Vez do jogador: {jogador_atual} ({marca})")
        jogar(board, marca, jogadas)

        if ganhou(board):
            print('Fim de jogo! O jogador', jogador_atual, 'venceu!')
            break
    else:
        print('Fim de jogo! Deu velha!')

# Inicia o jogo
game()
