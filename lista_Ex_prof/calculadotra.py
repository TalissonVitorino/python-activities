def soma(s, m):
    return s + m

def subtracao(s, m):
    return s - m

def multiplicacao(s, m):
    return s * m

def divisao(s, m):
    if m == 0:
        return "Erro: divisão por zero!"
    return s / m

def mensagem(nome, msg):
    print(f'{nome}, {msg}')

def cria_linhas():
    print(30* "-")

# Solicitando o nome do usuário
nome = input('Qual o seu nome? ')
mensagem(nome, 'seja bem-vindo à calculadora!')

while True:
    print("\n........... Menu ............")
    print()
    print("1. Entrada - Operações matemáticas")
    print("2. Encerramento")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    cria_linhas()
    if opcao == "1":
        print("\nEscolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        operacao = input("Digite o número da operação: ")
        cria_linhas()

        try:
            s = float(input("Digite o primeiro número: "))
            m = float(input("Digite o segundo número: "))

            if operacao == "1":
                resultado = soma(s, m)
                print(f"Resultado da soma: {resultado}")
            elif operacao == "2":
                resultado = subtracao(s, m)
                print(f"Resultado da subtração: {resultado}")
            elif operacao == "3":
                resultado = multiplicacao(s, m)
                print(f"Resultado da multiplicação: {resultado}")
            elif operacao == "4":
                resultado = divisao(s, m)
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Operação inválida! Tente novamente.")
        except ValueError:
            print("Erro: por favor, insira números válidos.")

    elif opcao == "2":
        print('Até mais')
    elif opcao == "3":
        print('Bye')
        break  # Sai do loop
    else:
        print("Opção inválida! Tente novamente.")
