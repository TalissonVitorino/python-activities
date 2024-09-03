# Definindo variáveis
is_admin = False
tem_codigo_acesso = True
# Usando o operador lógico 'or' para verificar se o usuário
#pode acessar o recurso
if is_admin or tem_codigo_acesso:
    print("Acesso concedido.")
else:
    print("Acesso negado.")