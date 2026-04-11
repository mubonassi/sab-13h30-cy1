print("| TABUADA PERSONALIZADA |")
print("-"*30)

tabuada = int(input("Digite o número que deseja fazer a tabuada: "))
intervalo = int(input("Digite o intervalo da tabuada: "))

for i in range(1,intervalo+1):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")