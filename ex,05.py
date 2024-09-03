# Definir as variáveis
idade = int(input("Digite a idade: "))
completou_curso = input("Completou o curso? (s/n): ").lower() == 's'

# Verificar as condições
if not (idade >= 18 and completou_curso):
    print("Você não é elegível para o concurso.")
else:
    print("Você é elegível para o concurso.")
