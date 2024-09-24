# Solicita ao usuário a informação sobre a disponibilidade do livro e a regularidade do sócio
livro_disponivel = input("O livro está disponível para empréstimo? (sim/não): ").strip().lower() == "sim"
socio_regular = input("O usuário é um sócio regular da biblioteca? (sim/não): ").strip().lower() == "sim"

# Verifica as condições para empréstimo
if (livro_disponivel and socio_regular) or socio_regular:
    emprestimo = "Permitido"
else:
    emprestimo = "Não permitido"

# Exibe o resultado
print(f"Empréstimo: {emprestimo}")