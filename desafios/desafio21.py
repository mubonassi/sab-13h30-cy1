print("| CAIXA DE FERRAMENTAS DE CALCULOS |")
print("-"*30)

try:
    valor1 = float(input("Digite o #1 valor: "))
    valor2 = float(input("Digite o #2 valor: "))
except ValueError:
    print("Necessitava digitar apenas números!")
except:
    print("Deu erro! Não sei qual, mas deu. Fiz minha parte em te avisar")
else:
    print("Escolha um dos operadores que deseja realizar!")
    print("1) Divisão 2) Potência 3) Comparador de Maior 4) É Múltiplo?")
    op = input("Digite aqui")

    if op == "1":
        try:
            res = valor1/valor2
        except ZeroDivisionError:
            print("Não se pode dividir por zero")
        else:
            print(f"{valor1}/{valor2}={res}")
    if op == "2":
        try:
            res = valor1**valor2
        except OverflowError:
            print("Resultado deu um número GIGANTE DEMAIS!")
        else:
            print(f"{valor1}^{valor2}={res}")
    if op == "3":
        if valor1 > valor2:
            print(f"{valor1} é maior que {valor2}")
        elif valor1 < valor2:
            print(f"{valor2} é maior que {valor1}")
        else:
            print("Erro! Ambos são iguais, sua mula.")
    if op == "4":
        try:
            res = valor1%valor2
        except ZeroDivisionError:
            print("Não se pode dividir por zero!")
        else:
            if res == 0:
                print("É múltiplo!")
            else:
                print("Não é múltiplo!")