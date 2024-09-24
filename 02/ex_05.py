numeros = [5, 32, 45, 12, 9, 10, 17, 28, 53, 18, 7, 26]

# 1. Encontrar o maior número do array
maior_numero = numeros[0]
for item in numeros:
    if item > maior_numero:
        maior_numero = item
print("1. O maior número do array é:", maior_numero)

# 2. Encontrar o menor número do array
menor_numero = numeros[0]
for item in numeros:
    if item < menor_numero:
        menor_numero = item
print("2. O menor número do array é:", menor_numero)

# 3. Encontrar um número no array e dizer qual é a sua posição no índice
numero_procurado = 10  # Você pode alterar esse valor para o número que quer procurar
if numero_procurado in numeros:
    posicao = numeros.index(numero_procurado)
    print(f"3. O número {numero_procurado} está na posição {posicao} do array.")
else:
    print(f"3. O número {numero_procurado} não está presente no array.")

# 4. Somar os números do array
soma_total = sum(numeros)
print("4. A soma dos números do array é:", soma_total)

# 5. Encontrar a média entre os números do array
media = soma_total / len(numeros)
print("A média dos números do array é: {:.2f}".format(media))

# 6. Mostrar apenas os números pares do array
pares = [item for item in numeros if item % 2 == 0]
print("6. Números pares do array:", pares)

# 7. Mostrar apenas os números ímpares do array
impares = [item for item in numeros if item % 2 != 0]
print("7. Números ímpares do array:", impares)
