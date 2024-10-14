idade = int(input('Informe a sua idade: '))
analfabeto = input('Você é analfabeto? (sim/não): ').lower() == 'sim'

if idade < 16:
    print('Você não pode votar.')
elif idade >= 18 and not analfabeto:
    print('O voto é obrigatório para você.')
elif (16
       <= idade < 18 or idade > 70 or analfabeto):
    print('O voto é facultativo para você.')
else:
    print('Você não pode votar.')
