peso = float(input("Digite seu peso por KG: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/ (altura**2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"seu IMC é {imc:.2f}.")
print(f"classificação: {classificacao}")