def calcular_comissao_vendedor():
    valor_total = float(input('Informe o valor total das vendas: R$ '))
    desconto = valor_total * 0.05
    valor_liquido = valor_total - desconto
    comissao = valor_liquido * 0.10

    print(f'Valor total da compra: R$ {valor_total:.2f}')
    print(f'Valor do desconto: R$ {desconto:.2f}')
    print(f'Valor líquido a pagar: R$ {valor_liquido:.2f}')
    print(f'Comissão do vendedor: R$ {comissao:.2f}')


calcular_comissao_vendedor()
