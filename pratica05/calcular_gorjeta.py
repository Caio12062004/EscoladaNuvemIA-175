def calcular_desconto(preco_original, percentual_desconto):

    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final

def main():

    print("Bem-vindo ao Calculador de Descontos!")
    print("Digite 'sair' a qualquer momento para fechar o programa.")

while True:
    try:
      # Pede o preço do produto
      preco_input = input("Digite o preço original do produto: ")
      if preco_input.lower() == 'sair':
        break
      preco_original = float(preco_input)

      # Pede o percentual de desconto
      desconto_input = input("Digite o percentual de desconto (ex: 10): ")
      if desconto_input.lower() == 'sair':
        break
      percentual_desconto = float(desconto_input)

      # Chama a função para calcular o preço final
      preco_final = calcular_desconto(preco_original, percentual_desconto)

      # Exibe o resultado
      print(f"O preço final com desconto é: R$ {preco_final:.2f}\n")
    
    except ValueError:
      print("Entrada inválida. Por favor, digite apenas números.\n")

# Bloco principal para iniciar o programa
if __name__ == "__main__":
  main()