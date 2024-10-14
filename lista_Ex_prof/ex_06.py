numero = int(input('Digite um número menor que 100: '))

if numero >= 100:
    print('O número deve ser menor que 100.')
else:
    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')