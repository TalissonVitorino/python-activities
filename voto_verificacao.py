idade = int(input("Digite a idade do eleitor: "))
alfabetizado = input("O eleitor é alfabetizado? (sim/não): ") == "sim"

if idade < 16:
    print("O eleitor não pode votar.")
elif 18 <= idade < 70 and alfabetizado:
    print("O voto é obrigatório.")
else:
    print("O voto é facultativo.")