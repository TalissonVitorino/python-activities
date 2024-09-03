# Definindo variáveis fornecidas pelo usuário
usuario = "admin"
senha = "secreta123"
# Busca por credenciais corretas
usuario_correto = "admin"
senha_correta = "secreta123"
# Usando o operador lógico 'and' para verificar se as
#redenciais estão corretas
if usuario == usuario_correto and senha == senha_correta:
    print("Acesso concedido.")
else:
    print("Usuário ou senha incorretos.")