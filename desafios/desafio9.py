print("| SORVETERIA+PLAY |")

sabores = ["Chocolate","Limão","Baunilha","Pipoca Caramelizada","Morango","Flocos"]

sabor = int(input("Digite o # do sabor desejado: "))

if sabor <= 5 and sabor >= 0:
    print(f"Você escolheu {sabores[sabor]}")
else:
    print("Escolha o sabor certo!")