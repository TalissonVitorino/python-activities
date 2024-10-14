def calculadora_simples():
    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))
    operacao = input('Escolha a operação (+, -, *, /): ')

    if operacao == '+':
        print(f'Resultado: {num1 + num2}')
    elif operacao == '-':
        print(f'Resultado: {num1 - num2}')
    elif operacao == '*':
        print(f'Resultado: {num1 * num2}')
    elif operacao == '/':
        if num2 != 0:
            print(f'Resultado: {num1 / num2}')
        else:
            print('Erro: Divisão por zero não permitida.')
    else:
        print('Operação inválida.')


calculadora_simples()
