numeros = [5, 32, 45, 12, 9, 10, 17, 28, 53, 18, 7, 26]

# Inicializa o maior número com o primeiro elemento da lista
maior_numero = numeros[0]

# Percorre a lista para encontrar o maior número
for item in numeros:
    if item > maior_numero:
        maior_numero = item

# Exibe o maior número
print("O maior número é:", maior_numero)
print(f'O maior numero é: {max(numeros)}')