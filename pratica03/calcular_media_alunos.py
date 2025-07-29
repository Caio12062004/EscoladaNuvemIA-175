n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"A média é: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado")
else:
    print("Aluno em exame.")

    exame = float(input("Digite a nota do exame: "))
    print(f"A nota do exame é {exame:.1f}")

    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")
    print(f"A média final é : {media_final:.1f}")