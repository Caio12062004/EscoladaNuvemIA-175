numero_funcionario = int(input("Insira o número do funcionário: "))
horas_trabalhada = int(input("Insira a quantidade de horas trabalhadas: "))
valor_hora = float(input("Insira o valor por hora trabalhada: "))

salario = horas_trabalhada * valor_hora

print(f"número do funcionário: {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")