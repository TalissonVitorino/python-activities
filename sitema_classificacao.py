# Solicitar a quantidade de estudantes
quantidade_estudantes = int(input("Digite a quantidade de estudantes: "))

# Lista para armazenar os dados dos estudantes
estudantes = []

# Entrada de dados
for i in range(quantidade_estudantes):
    print(f"\nEstudante {i + 1}")
    nome = input("Nome: ")

    while True:
        try:
            nota = float(input("Nota (0 a 100): "))
            if 0 <= nota <= 100:
                break
            else:
                print("Nota inválida! A nota deve estar entre 0 e 100.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

    # Armazenar os dados do estudante
    estudantes.append({"nome": nome, "nota": nota})


# Função para classificar o estudante
def classificar_estudante(nota0):
    if 90 <= nota <= 100:
        return "A"
    elif 80 <= nota < 90:
        return "B"
    elif 70 <= nota < 80:
        return "C"
    elif 60 <= nota < 70:
        return "D"
    else:
        return "F"


# Saída de dados com a classificação
print("\nRelatório de Classificação:")
for estudante in estudantes:
    nome = estudante["nome"]
    nota = estudante["nota"]
    classificacao = classificar_estudante(nota)
    print(f"Nome: {nome}, Nota: {nota:.2f}, Classificação: {classificacao}")
