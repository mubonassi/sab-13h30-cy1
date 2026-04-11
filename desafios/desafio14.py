print("| SOMANDO EM INTERVALOS |")

qtd = int(input("Digite o intervalo da qtd de números: "))
resultado = 0

for i in range(1,qtd+1):
    numero = int(input(f"Digite o número {i}: "))
    resultado = resultado + numero

print(f"Resultado final: {resultado}")