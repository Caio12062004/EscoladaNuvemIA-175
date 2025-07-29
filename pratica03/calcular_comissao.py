nome = str(input("Digite o seu nome: "))

salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas: "))

comissao = total_vendas * 0.15

salario_total = salario_fixo + comissao

print(f"Total = R$ {salario_total:.2f}")