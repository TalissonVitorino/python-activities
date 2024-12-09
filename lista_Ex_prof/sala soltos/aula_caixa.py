import os


def limpa():
    os.system('cls')


def depositar(saldo, lancamento, valor):
    saldo += valor
    lancamento.append(f'Depósito: {saldo:.2f}')
    return saldo, lancamento


def sacar(saldo, lancamento, valor):
    saldo -= valor
    lancamento.append(f'Saldo: {saldo:.2f}')
    return saldo, lancamento


def mostrar_saldo(saldo):
    return f'saldo atual é {saldo:.2f}'


def imprimir_extrato(lancamento, saldo, numero_conta, nome):
    extrato = '\n---------------- extrato ---------------'
    extrato += f"\n conta num: {numero_conta}------ Cliente: {nome}"
    extrato += f"\n"
    extrato += f'\n------------------------------------------------\n'
    extrato += f"\n".join(lancamento) #.join e igaul o foreach
    extrato += f'\n------------------------------------------------'
    extrato += f"\n--------------------------Saldo fina R$: {saldo:.2f}"
    return extrato


def caixa_eletronico():
    limpa()
    saldo = 0.0
    lancamento = []

    nome = input('Digite o seu nome: ')
    numero_conta = input("digite o numero da sua conta!")

    while True:
        print('----------menu-----------')
        print('1 - Depositar')
        print('2 - sacar')
        print('3 - Mostrar saldo')
        print('4 - Imprimir extrato')
        print('5 - Sair')

        op = input('Escolha uma opção: ')

        if op == '1':
            valor = float(input('Informe o valor do depósito: '))
            saldo, lancamento = depositar(saldo, lancamento, valor)
            print(f'O deposioto foi depositado com sucesso{saldo}')

        elif op == '2':
            valor = float(input('Informe o valor do saque: '))
            saldo, lancamento = sacar(saldo, lancamento, valor)
        elif op == '3':
            print("Opção 3 selecionada.")
        elif op == '4':
            print(imprimir_extrato(lancamento, saldo, numero_conta, nome))
        elif op == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")


caixa_eletronico()
