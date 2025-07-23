# Definir Variaveis
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calcular Desconto
calcular_desconto = preco_original * (porcentagem_desconto / 100)

# Preço total
preco_total = preco_original - calcular_desconto

print(f"O produto {nome_produto} é R${preco_original:.2f}")
print(f"E o Produto {nome_produto} tem {calcular_desconto}% de desconto.")
print(f"E está por apenas R${preco_total:.2f}")