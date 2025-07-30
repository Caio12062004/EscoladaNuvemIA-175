def numero_int():
    par = 0
    impar = 0

    while True:
        entrada = input("digite um número inteiro ou digite 'fim' para encerrar: ")

        if entrada.lower() == "fim":
            print("Programa encerrando.")
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é par.")
                par += 1
            else:
                print(f"O número {numero} é ímpar.")
                impar += 1
        except ValueError:
            print("Erro: Por favor digite apenas numeros inteiros.")

    print("\nResultado Final")
    print(f"Numeros Pares: {par}")
    print(f"Numeros Impares: {impar}")

numero_int()