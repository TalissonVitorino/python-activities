class CaixaEletronico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.historico = []

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. Insira um valor positivo.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return

        # Cédulas disponíveis
        cedulas = [100, 50, 20, 10, 5, 2, 1]
        quantidade_cedulas = {}

        valor_restante = valor
        for cedula in cedulas:
            quantidade = valor_restante // cedula
            if quantidade > 0:
                quantidade_cedulas[cedula] = quantidade
                valor_restante %= cedula

        # Realiza o saque se for possível com as cédulas disponíveis
        self.saldo -= valor
        self.historico.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        print("Cédulas entregues:")
        for cedula, quantidade in quantidade_cedulas.items():
            print(f"Cédulas de R$ {cedula}: {quantidade}")

    def exibir_historico(self):
        print("\nHistórico de transações:")
        if not self.historico:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.historico:
                print(transacao)

    def extrato(self):
        print("\n=== Extrato ===")
        self.exibir_saldo()
        self.exibir_historico()
        print("================")

    def menu(self):
        while True:
            print("\n=== Caixa Eletrônico ===")
            print("1. Exibir saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Histórico de transações")
            print("5. Extrato")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.exibir_saldo()
            elif opcao == "2":
                try:
                    valor = float(input("Digite o valor para depósito: R$ "))
                    self.depositar(valor)
                except ValueError:
                    print("Valor inválido. Digite um número.")
            elif opcao == "3":
                try:
                    valor = float(input("Digite o valor para saque: R$ "))
                    self.sacar(valor)
                except ValueError:
                    print("Valor inválido. Digite um número.")
            elif opcao == "4":
                self.exibir_historico()
            elif opcao == "5":
                self.extrato()
            elif opcao == "6":
                print("Obrigado por utilizar o caixa eletrônico!")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Inicializa o caixa eletrônico com um saldo inicial de R$1000,00
caixa = CaixaEletronico(saldo_inicial=1000.0)
caixa.menu()
