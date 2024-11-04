def mensagem(nome, msg):
    print(f'{nome}, {msg}')


# Exibindo mensagens de boas-vindas para Pedro e Maria
#mensagem('Pedro', 'seja bem-vindo')
#mensagem('Maria', 'seja bem-vinda')

# Solicitando o nome do usuário
nome = input('Qual o seu nome? ')

while True:
    print("........ Menu ........")
    print("1. Entrada")
    
    print("2. Encerramento")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mensagem(nome, 'seja bem-vindo')  # Passa o nome e a mensagem para a função
    elif opcao == "2":
        print('Até mais')
    elif opcao == "3":
        print('Bye')
        break  # Sai do loop
    else:
        print("Opção inválida! Tente novamente.")