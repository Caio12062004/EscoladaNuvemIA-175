import requests
import json

def valida_cep(cep):
    return cep.isdigit() and len(cep) == 8

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        dados_cep = response.json()
        
        if 'erro' in dados_cep and dados_cep['erro']:
            print("CEP não encontrado.")
            return None
        
        return dados_cep
        
    except requests.exceptions.HTTPError as erro: # Erro HTTP
        print(f"Erro HTTP: {erro}")
        return None
    except requests.exceptions.RequestException as erro: # Erro de conexão
        print(f"Erro de conexão: {erro}")
        return None
    except json.JSONDecodeError:
        print("Erro ao decodificar a resposta da API.")
        return None

def exibir_endereco(dados):
    if dados:
        print("\n--- Informações do Endereço ---")
        print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
        print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
        print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
        print(f"Estado: {dados.get('uf', 'Não disponível')}")
        print("-------------------------------")
    else:
        print("Não foi possível obter os dados do endereço.")

def main():

    print("Bem-vindo ao Consultor de CEP!")
    
    while True:
        cep = input("Digite um CEP (apenas números) ou 'sair' para encerrar: ")
        
        if cep.lower() == 'sair':
            print("Programa encerrado.")
            break
            
        if not valida_cep(cep):
            print("CEP inválido. Por favor, digite 8 dígitos numéricos.")
            continue
            
        dados = consultar_cep(cep)
        exibir_endereco(dados)
        print("-" * 30)

if __name__ == "__main__":
    main()