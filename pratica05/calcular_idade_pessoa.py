import datetime

def calcular_idade_nascimento(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

# Loop principal do programa
print("--- Calculadora de Idade em Dias ---")
print("Digite 'sair' a qualquer momento para fechar o programa.")
while True:
    # Input do usuário
    entrada_usuario = input("\nDigite o ano do seu nascimento: ")

    # Verifica se o usuário quer sair
    if entrada_usuario.lower() == 'sair':
        print("Obrigado por usar a calculadora! Até mais.")
        break

    try:
        # Tenta converter a entrada para um número inteiro
        ano_nasc = int(entrada_usuario)
        
        # Chama a função e exibe o resultado
        idade_em_dias = calcular_idade_nascimento(ano_nasc)
        print(f"Sua idade aproximada em dias é: {idade_em_dias} dias.")
    
    except ValueError:
        # Captura o erro se a entrada não for um número válido
        print("Entrada inválida. Por favor, digite um ano (ex: 1990) ou 'sair'.")