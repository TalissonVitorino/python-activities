# Solicitar a quantidade de estudantes
quantidade_estudantes = int(input("Digite a quantidade de estudantes: "))

# Lista para armazenar os dados dos estudantes
estudantes = []

# Entrada de dados
for i in range(quantidade_estudantes):
    nome = input(f"\nNome do estudante {i + 1}: ")
    nota = float(input("Nota (0 a 100): "))
    estudantes.append((nome, nota))


# Função para classificar o estudante
def classificar(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"


# Saída de dados com a classificação
print("\nRelatório de Classificação:")
for nome, nota in estudantes:
    print(f"Nome: {nome}, Nota: {nota:.2f}, Classificação: {classificar(nota)}")
