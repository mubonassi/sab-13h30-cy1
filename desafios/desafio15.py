print("| SOMANDO EM SEQUÊNCIA |")

intervalo = int(input("Digite o intervalo: "))

#Resposta 1
resultado = 0
conta = ""
for i in range(intervalo+1):
    conta = conta + str(i)
    resultado = resultado + i
    if i < intervalo:
        conta = conta + "+"

print(f"{conta} = {resultado}")

#Resposta 2
resultado = 0
for i in range(intervalo+1):
    resultado = resultado + i
    print(i, end="")
    if i < intervalo:
        print("+",end="")

print(f" = {resultado}")