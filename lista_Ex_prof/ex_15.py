def calcular_imc():
    print('Calculadora de Índice de Massa Corporal (IMC)')

    try:
        peso = float(input('Informe o seu peso em kg(exemplo: 76): '))
        altura = float(input('Informe a sua altura em metros (exemplo: 1.75): '))

        if peso <= 0 or altura <= 0:
            print('Peso e altura devem ser valores positivos.')
            return

        imc = peso / (altura ** 2)

        print(f'Seu IMC é: {imc:.2f}')
        if imc < 18.5:
            print('Classificação: Abaixo do peso')
        elif 18.5 <= imc < 24.9:
            print('Classificação: Peso normal')
        elif 25 <= imc < 29.9:
            print('Classificação: Sobrepeso')
        elif 30 <= imc < 34.9:
            print('Classificação: Obesidade Grau I')
        elif 35 <= imc < 39.9:
            print('Classificação: Obesidade Grau II')
        else:
            print('Classificação: Obesidade Grau III ou Mórbida')

    except ValueError:
        print('Entrada inválida. Por favor, insira valores numéricos para peso e altura.')


calcular_imc()
