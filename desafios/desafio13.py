print("| PARES E IMPARES |")
print("-"*30)

intervalo = int(input("Digite o intervalo do número: "))

print("> Pares")
for i in range(2,intervalo+1,2):
    print(i, end=" ")
print()

print("> Impares")
for i in range(1,intervalo+1,2):
    print(i, end=" ")
print()