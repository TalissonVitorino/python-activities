numeros = [23, 45, 67, 12, 89, 34, 78, 56, 90, 11, 5, 99, 120,
           37, 44, 66, 73, 88,101, 15, 2, 54, 29, 77, 39, 65, 82, 91, 33, 18]
numeros_crescente = []

while numeros:
    menor = numeros[0]
    for num in numeros:
        if num < menor:
            menor = num
    numeros.remove(menor)
    numeros_crescente.append(menor)

print('Números em ordem crescente:', numeros_crescente)

# print(sorted(numeros_crescente))
# print(sorted(numeros_crescente, reverse=True))
