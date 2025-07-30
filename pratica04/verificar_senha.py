while True:
    senha = input("Digite a sua senha ou 'sair' para encerrar: ")
    
    if senha.lower() == "sair":
        break

    if len(senha) < 8:
        print("Senha fraca. A senha necessita de 8 caracteres.")
        continue

    if not any(caracter.isdigit() for caracter in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    if not any(caracter.isalpha() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra.")
        continue

    if not any(caracter.isupper() for caracter in senha):
        print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
        continue

    print("Senha é válida.")
    break