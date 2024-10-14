numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))

soma = numero1 + numero2
multiplicacao = numero1 * numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2 if numero2 != 0 else 'Divisão por zero não permitida'
media = (numero1 + numero2) / 2

print(f'Soma: {soma}')
print(f'Multiplicação: {multiplicacao}')
print(f'Subtração: {subtracao}')
print(f'Divisão: {divisao}')
print(f'Média: {media}')
