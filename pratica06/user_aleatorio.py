import requests

def gerar_usuario():
    url = 'https://randomuser.me/api/'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Programa de Usuário Aleatório ===")
        print(f"Nome: {nome}\nE-mail: {email}\nPaís: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

if __name__ == "__main__":
    gerar_usuario()