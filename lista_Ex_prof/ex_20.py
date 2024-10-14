import time


def caixa_eletronico():
    print('Bem-vindo ao Caixa Eletrônico Virtual!')
    nome = input('Por favor, informe o seu nome: ')
    print(f'Olá, {nome}! Vamos começar.\n')

    while True:
        try:
            saldo = float(input(f'{nome}, informe o saldo inicial: R$ '))
            if saldo < 0:
                print('O saldo inicial não pode ser negativo. Tente novamente.')
            else:
                break
        except ValueError:
            print('Entrada inválida. Por favor, insira um valor numérico.')

    while True:
        print('\nMenu de Operações:')
        print('[ 1 ]: Depositar')
        print('[ 2 ]: Sacar')
        print('[ 3 ]: Consultar Saldo')
        print('[ 4 ]: Sair')

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
            continue

        if opcao == 1:
            try:
                valor_deposito = float(input("Informe o valor do depósito: R$ "))
                if valor_deposito > 0:
                    saldo += valor_deposito
                    print(f"Processando depósito...")
                    time.sleep(1)
                    print(f"Depósito realizado com sucesso. Saldo atual: R$ {saldo:.2f}")
                else:
                    print("O valor do depósito deve ser positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.")

        elif opcao == 2:
            try:
                valor_saque = float(input("Informe o valor do saque: R$ "))
                if valor_saque > 0:
                    if valor_saque > saldo:
                        print("Saldo insuficiente para realizar o saque.")
                    else:
                        saldo -= valor_saque
                        print("Processando saque...")
                        time.sleep(1)
                        print(f"Saque realizado com sucesso. Saldo atual: R$ {saldo:.2f}")
                else:
                    print("O valor do saque deve ser positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.")

        elif opcao == 3:
            print("Verificando saldo...")
            time.sleep(1)
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == 4:
            print(f"\nObrigado por usar o Caixa Eletrônico, {nome}.")
            print(f"Seu saldo final é: R$ {saldo:.2f}. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


caixa_eletronico()
