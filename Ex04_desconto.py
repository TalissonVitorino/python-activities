# Solicita ao usuário o preço original, a quantidade e se o cliente é VIP
preco_original = float(input("Digite o preço original do produto: "))
quantidade = int(input("Digite a quantidade de unidades compradas: "))
cliente_vip = input("O cliente é VIP? (sim/não): ").strip().lower() == "sim"

# Calcula o preço total sem desconto
preco_total = preco_original * quantidade

# Aplica o desconto baseado na quantidade
if quantidade >= 10:
    preco_total *= 0.85  # Aplica 15% de desconto
    desconto_aplicado = "15% de desconto por quantidade"
else:
    desconto_aplicado = "Nenhum desconto por quantidade"

# Aplica o desconto adicional se o cliente for VIP
if cliente_vip:
    preco_total *= 0.90  # Aplica 10% de desconto adicional
    desconto_aplicado += " e 10% de desconto adicional por ser VIP"

# Exibe o resultado
print(f"Preço total: R${preco_total:.2f}")
print(f"Desconto aplicado: {desconto_aplicado}")

#exibe resultado
print(f"Quantidade: R${preco_original: .2f}")
print(f"Quantidade: R${quantidade}")
print(f"Quantidade: R${desconto_aplicado}")
print(f"Quantidade: R${preco_total: .2f}")
