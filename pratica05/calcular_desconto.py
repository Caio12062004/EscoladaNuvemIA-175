# Função para calcular o desconto.
def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

# Definir que são float e o input para o usuario.
preco_original = float(input("Digite o preço do produto (exemplo: 250.75): "))
desconto = float(input("Digite o percentual de desconto (exemplo: 10): "))

preco_com_desconto = calcular_desconto(preco_original, desconto)
print(f"O preço final com {desconto}% de desconto é: R$ {preco_com_desconto:.2f}")