# Criando o array inicial
numeros = [23, 45, 67, 12, 89, 34, 78, 56, 90, 11, 5, 99, 120, 37, 44, 66, 73, 88, 101, 15, 2, 54, 29, 77, 39, 65, 82, 91, 33, 18]

# Array de ordem decrescente
num_decrescente = []

while numeros:
    maior = numeros[0]

    for num in numeros:
        if num > maior:
            maior = num

    numeros.remove(maior)
    num_decrescente.append(maior)

print("Números em ordem decrescente:", num_decrescente)