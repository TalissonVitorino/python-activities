import os

# Função para limpar a tela
def limpa():
    os.system('cls')

# Função principal do caixa eletrônico
def caixa_eletronico():
    saldo = 0  # Saldo inicial
    lancamentos = []  # Histórico de transações

    # Função para mostrar o saldo
    def mostrar_saldo():
        print(f'Saldo atual: R$ {saldo:.2f}')

    # Função para depositar um valor
    def depositar(valor):
        nonlocal saldo  # Permite modificar o saldo da função externa
        if valor > 0:
            saldo += valor
            lancamentos.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    # Função para imprimir o extrato
    def imprimir_extrato():
        print("\n=== Extrato ===")
        if lancamentos:
            for item in lancamentos:
                print(item)
        else:
            print("Nenhuma transação realizada.")
        print(f"Saldo final: R$ {saldo:.2f}")
        print("================\n")

    # Loop do menu
    while True:
        limpa()
        print('---------- Menu -----------')
        print('1 - Depositar')
        print('2 - Mostrar saldo')
        print('3 - Imprimir extrato')
        print('4 - Sair')

        op = input('Escolha uma opção: ')

        if op == '1':
            try:
                valor = float(input('Qual o valor do depósito: R$ '))
                depositar(valor)
            except ValueError:
                print("Valor inválido. Digite um número.")
        elif op == '2':
            mostrar_saldo()
        elif op == '3':
            imprimir_extrato()
        elif op == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")

        input("Pressione Enter para continuar...")

# Executa o caixa eletrônico
caixa_eletronico()
