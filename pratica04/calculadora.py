while True:  # Loop infinito para continuar pedindo entradas até uma operação válida
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)

            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)

            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ")

            # Realiza a operação com base na entrada
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                # Tenta realizar a divisão e trata o erro de divisão por zero
                try:
                    resultado = num1 / num2
                except ZeroDivisionError:
                    print("Erro: Divisão por zero não é permitida. Tente novamente.")
                    continue
            else:
                print("Erro: Operação inválida. Use +, -, * ou /. Tente novamente.")
                continue

            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            break

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite apenas números. Tente novamente.")
            continue