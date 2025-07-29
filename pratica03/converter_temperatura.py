temperatura = float(input("Digite a temperatura a ser convertida: "))
origem = input("Digite a escala de origem (C, F, K): ").upper()
destino = input("Digite a escala de destino (C, F, K): ").upper()

if origem == destino:
    resultado = temperatura

elif origem == "C":
    if destino == "F": #Origem C e destino F
        resultado = (temperatura * 9/5) + 32
    else:
        resultado = temperatura + 273.15

elif origem == "F":
    if destino == "C":#Origem F e destino C
        resultado = (temperatura - 32) * 5/9
    else:
        resultado = (temperatura - 32) * 5/9 + 273.15

else:
    if destino == "C": #Origem K e destino C
        resultado = temperatura - 273.15
    else: # Origem K e destino F
        resultado = (temperatura - 273.15) * 9/5 +32



print(f"{temperatura}{origem} é igual a {resultado}{destino}")