nota1 = float(input('Informe a primeira nota: '))
peso1 = float(input('Informe o peso da primeira nota: '))

nota2 = float(input("Informe a segunda nota: "))
peso2 = float(input('Informe o peso da segunda nota: '))

nota3 = float(input('Informe a terceira nota: '))
peso3 = float(input('Informe o peso da terceira nota: '))

soma_pesos = peso1 + peso2 + peso3
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_pesos

print(f'A média ponderada é: {media_ponderada:.2f}')
