def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None

def jogo_tictactoe():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    for turnos in range(9):  # Máximo de 9 jogadas
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez!")

        while True:
            try:
                linha = int(input("Escolha a linha (0, 1 ou 2): "))
                coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual
                    break
                else:
                    print("Essa posição já está ocupada. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Certifique-se de escolher números entre 0 e 2.")

        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {vencedor} venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    exibir_tabuleiro(tabuleiro)
    print("Empate! O jogo terminou sem vencedor.")

if __name__ == "__main__":
    jogo_tictactoe()
