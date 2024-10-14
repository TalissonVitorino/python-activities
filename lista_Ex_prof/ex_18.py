def calcular_juros_simples():
    capital_inicial = float(input('Informe o capital inicial (R$): '))
    taxa_juros = float(input('Informe a taxa de juros (% ao ano): '))
    tempo = float(input('Informe o tempo do investimento (em anos): '))
    juros = capital_inicial * (taxa_juros / 100) * tempo
    valor_final = capital_inicial + juros

    print(f'Rendimento dos juros: R$ {juros:.2f}')
    print(f'Valor final do investimento: R$ {valor_final:.2f}')


calcular_juros_simples()
