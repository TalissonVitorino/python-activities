numeros = [5, 32, 45, 12, 9, 10, 17, 28, 53, 18, 7, 26]

for item in numeros:
    if (item >= 10):
        print(item)

for item in numeros:
    if (item == 10):
        print(item)

i = 0
for item in numeros:
    print(' item: ', item, ' indice ', i)


# Listas para armazenar os números pares e ímpares
pares = []
impares = []

# Percorre a lista original e separa os números
for item in numeros:
    if item % 2 == 0:  # Se o número for divisível por 2, é par
        pares.append(item)
    else:  # Caso contrário, é ímpar
        impares.append(item)

# Exibe os resultados
print("Números pares:", pares)
print("Números ímpares:", impares)