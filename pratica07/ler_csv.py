import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo 'CSV': ").strip()
    ler_csv(nome_arquivo)