#While True - Repetição indefinida (loop infinito)

#Break - Quebra o loop
while True:
    instrucao = input("Deseja quebrar a estrutura?: ")
    if instrucao.lower() == "sim":
        break
print("Fim da repetição")

for i in range(1000000000):
    print(i)
    if i >= 5:
        break

#quit() -> função que ENCERRA o algoritmo
while True:
    instrucao = input("E ai, quebra essa também?: ").lower()
    if instrucao == "sim":
        quit()
print("Você não verá esse print")

