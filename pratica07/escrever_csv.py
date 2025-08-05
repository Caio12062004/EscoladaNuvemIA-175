import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", newline="") as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Nome", "Idade", "Cidade"])
            for linha in dados:
                escritor.writerow(linha)
        print(f"Dados salvos com sucesso em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

dados = [
    ["Mario", 28, "Rio de Janeiro"],
    ["Caio", 22, "São Paulo"],
    ["Laura", 25, "Salvador"]
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ")
    escrever_csv(nome_arquivo, dados)