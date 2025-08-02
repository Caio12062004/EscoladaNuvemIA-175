import requests
import json
import datetime

def cotacao_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    print(f"Buscando cotação para {moeda}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        cotacao_data = response.json()
        chave_cotacao = f"{moeda}BRL"
        
        if chave_cotacao in cotacao_data:
            dados_moeda = cotacao_data[chave_cotacao]
            return dados_moeda
        else:
            print(f"Não foi possível encontrar a cotação para a moeda {moeda}.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None
        
def exibir_cotacao(dados_moeda):

    nome_moeda = dados_moeda.get("name")
    valor_atual = float(dados_moeda.get("ask"))
    valor_maximo = float(dados_moeda.get("high"))
    valor_minimo = float(dados_moeda.get("low"))
    timestamp = int(dados_moeda.get("timestamp"))
    
    # Converte o timestamp para uma data e hora legível
    data_atualizacao = datetime.datetime.fromtimestamp(timestamp)
    
    # Formata a data para um formato mais amigável
    data_formatada = data_atualizacao.strftime("%d/%m/%Y %H:%M:%S")
    
    print("\n--- Cotação da Moeda ---")
    print(f"Moeda: {nome_moeda}")
    print(f"Valor Atual (Compra): R$ {valor_atual:.2f}")
    print(f"Valor Máximo (Dia): R$ {valor_maximo:.2f}")
    print(f"Valor Mínimo (Dia): R$ {valor_minimo:.2f}")
    print(f"Última Atualização: {data_formatada}")
    print("------------------------")


if __name__ == "__main__":

    codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ").upper().strip()
    
    if len(codigo_moeda) == 3:
        cotacao = cotacao_moeda(codigo_moeda)
        
        if cotacao:
            exibir_cotacao(cotacao)
        
    else:
        print("Código de moeda inválido. O código deve ter 3 letras (ex: USD).")