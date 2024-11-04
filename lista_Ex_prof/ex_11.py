numeros = [12, 23, 45, 32, 5, 87, 41, 98, 56, 39, 23, 75, 79, 99, 103,
           42, 36, 68, 19, 28, 6, 32, 45, 12, 9, 10, 17, 28, 53, 18, 7, 26]

pares = []
impares = []
soma_total = 0
qtd_pares = 0
qtd_impares = 0

for num in numeros:

    soma_total += num

    if num % 2 == 0:
        pares.append(num)
        qtd_pares += 1
    else:
        impares.append(num)
        qtd_impares += 1

media = soma_total / len(numeros)

print("Números pares:", pares)
print("Números ímpares:", impares)
print("Quantidade de números pares:", qtd_pares)
print("Quantidade de números ímpares:", qtd_impares)
print("Soma de todos os números:", soma_total)
print("Média de todos os números:", media)
