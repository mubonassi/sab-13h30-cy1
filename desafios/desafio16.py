print("| ADIVINHANDO PALAVRA MÁGICA |")

palavra = "corso"

for i in range(1,5+1):
    tentativa = input(f"(Tentativa {i}) Digite uma palavra: ")
    if tentativa == palavra:
        print("ACERTOU! IHU!")
        break
    else:
        print("ERROU! TENTE NOVAMENTE! NOT IHU!")

if tentativa != palavra:
    print("Acabou as tentativas! GAME OVER!")