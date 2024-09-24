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

# 3. Encontrar um número no array e dizer sua posição
numero_procurado = 10  # Você pode alterar esse valor para o número que quer procurar
posicao = -1
for index in range(len(numeros)):
    if numeros[index] == numero_procurado:
        posicao = index
        break
if posicao != -1:
    print(f"3. O número {numero_procurado} está na posição {posicao} do array.")
else:
    print(f"3. O número {numero_procurado} não está presente no array.")

# 4. Somar os números do array
soma_total = 0
for item in numeros:
    soma_total += item
print("4. A soma dos números do array é:", soma_total)

# 5. Encontrar a média entre os números do array
media = soma_total / len(numeros)
print(f"5. A média dos números do array é: {media:.2f}")

# 6. Mostrar apenas os números pares do array
pares = []
for item in numeros:
    if item % 2 == 0:
        pares.append(item)
print("6. Números pares do array:", pares)

# 7. Mostrar apenas os números ímpares do array
impares = []
for item in numeros:
    if item % 2 != 0:
        impares.append(item)
print("7. Números ímpares do array:", impares)
