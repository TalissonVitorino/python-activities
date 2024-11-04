setor_financeiro =\
    input('Você trabalha no setor financeiro?' ' (sim/não): ').lower() == 'sim'
nivel_senior = (
     input('Seu nível de operação é sênior? (sim/não):' ' ').lower() == 'sim')
administrador = input("Você é administrador do setor? (sim/não):"
                      " ").lower() == 'sim'

if (setor_financeiro and nivel_senior) or administrador:
    print('Você pode acessar a tela de aplicações financeiras.')
else:
    print('Você não tem permissão para acessar a tela de aplicações financeiras.')
