# Declarar Variaveis
valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_dolar_arredondado = round(valor_dolar, 2)

valor_euro = valor_reais / taxa_euro
valor_euro_arredondado = round(valor_euro, 2)

print(f"Valor em Real: R${valor_reais}")
print(f"Valor em Dólar: USD ${valor_dolar_arredondado}")
print(f"Valor em Euro: EUR €{valor_euro_arredondado}")