import unicodedata

def eh_palindromo(texto):
    # Normaliza o texto para remover acentos 'NFD' separa a letra do acento. Ex: 'é' vira 'e' e '´' vira ''.
    texto_normalizado = unicodedata.normalize('NFD', texto)
    
    # Converte para minúsculas e cria uma nova string apenas com letras
    texto_limpo = ""
    for caractere in texto_normalizado:
        if 'a' <= caractere.lower() <= 'z':
            texto_limpo += caractere.lower()
            
    # Inverte a string e compara
    texto_invertido = texto_limpo[::-1]
    
    return texto_limpo == texto_invertido

def main():
    print("--- Verificador de Palíndromos ---")
    print("Digite uma palavra ou frase para verificar.")
    print("Para sair, digite 'sair' ou pressione Enter.\n")

    while True:
        palindromo = input("Digite seu texto: ")

        if palindromo.lower() == 'sair' or not palindromo:
            print("Saindo do programa. Até mais!")
            break

        if eh_palindromo(palindromo):
            print("Sim, é um palíndromo!")
        else:
            print("Não, não é um palíndromo.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()