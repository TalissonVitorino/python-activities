numeros = [6, 23, 35, 96, 14, 9, 10, 17, 28, 58, 18, 3, 68, 87, 29, 6]
maior_numero = numeros[0]
menor_numero = numeros[0]
indice_maior = 0
indice_menor = 0

for i in range(1, len(numeros)):
    if numeros[i] > maior_numero:
        maior_numero = numeros[i]
        indice_maior = i
    if numeros[i] < menor_numero:
        menor_numero = numeros[i]
        indice_menor = i

print(f'Maior número: {maior_numero}, Índice: {indice_maior}')
print(f'Menor número: {menor_numero}, Índice: {indice_menor}')
