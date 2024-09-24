credencial_valida = input("A credencial do funcionário é válida? (sim/não): ").strip().lower() == "sim"
autorizacao_supervisor = input("A autorização do supervisor foi concedida? (sim/não): ").strip().lower() == "sim"

pode_acessar = credencial_valida and autorizacao_supervisor or autorizacao_supervisor

if pode_acessar:
    print("Acesso concedido.")
else:
    print("Acesso negado.")
