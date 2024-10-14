# Solicitar as notas ao usuário
portugues = float(input('Digite a nota de português: '))
historia = float(input('Digite a nota de história: '))
ciencias = float(input('Digite a nota de ciências: '))
matematica = float(input('Digite a nota de matemática: '))

media = (portugues + historia + ciencias + matematica) / 4

if media >= 7.0:
    print(f'Parabéns! Você foi aprovado com média {media:.2f}.')
elif 5.0 <= media < 7.0:
    if portugues < 5 or matematica < 5:
        print(f'Você foi reprovado pois sua nota em português ou matemática é menor que 5. Sua média foi {media:.2f}.')
    else:
        print(f'Você está em recuperação com média {media:.2f}.')
else:
    print(f'Você foi reprovado com média {media:.2f}.')
