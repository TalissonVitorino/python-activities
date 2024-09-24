numeros = [5, 32, 45, 12, 9, 10, 17, 28, 53, 18, 7, 26]

# Listas vazias!
pares = []
impares = []

# Percorre as listas e separa os números impares e pares..
for item in numeros:
    if item % 2 == 0:  # Se o número for divisível por 2, r resto é par..
        pares.append(item)
    else:  # Caso contrário, é ímpar.
        impares.append(item)

# Encontra o menor número da lista e sua posição.
menor_numero = min(numeros)
posicao_menor = numeros.index(menor_numero)

# Encontra o maior número da lista e sua posição.
maior_numero = max(numeros)
posicao_maior = numeros.index(maior_numero)

# Exibe os resultados tanto dos pares e impares tanto quanto da posição.
print("Números pares:", pares)
print()  # Pula a linha
print("Números ímpares:", impares, "\n")  # Maneira mais comun de se fazer
print("O menor número é:", menor_numero, "e está na posição:", posicao_menor, "\n")
print("O maior número é:", maior_numero, "e está na posição:", posicao_maior, "\n")