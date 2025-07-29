ano = int(input("Digite qual ano você deseja verificar: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 ==0:
            print(f"O {ano} é bissexto.")
        else:
            print(f"O {ano} não é bissexto.")
    else:
        print(f"O {ano} é bissexto")
else:
    print(f"O {ano} não é bissexto.")