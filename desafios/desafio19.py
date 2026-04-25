print("| PALAVRA MÁGICA!!!!!112321!!!!!!! |")

tentativas = 0
palavraMagica = "polenta"
tentativa = ""

while tentativa != palavraMagica:
    tentativa = input("Digite a sua tentativa de palavra: ")
    tentativas += 1

    if tentativa != palavraMagica:
        print("Você errou! Tente novamente!")
    else:
        print(f"Você acertou com {tentativas} tentativas!")