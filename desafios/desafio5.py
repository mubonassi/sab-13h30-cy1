print("||Galactic Ultra Mega Blaster Warriors DX 2 Online Gachapon Season Pass||")
pontos = int(input("Digite quantos pontos você fez: "))

if pontos >= 1000:
    print("Rank: Lendário")
elif pontos >= 500:
    print("Rank: Mestre")
elif pontos >= 200:
    print("Rank: Profissional")
elif pontos >= 50:
    print("Rank: Iniciante")
else:
    print("Rank: Noobão")