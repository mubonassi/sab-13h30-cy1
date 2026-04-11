#Estrutura de Repetição - PARTE I

#FOR - Repetição Contada (Quantidade Definida)
#Função range(x), que define quantas vezes ele vai repetir (criar intervalo)
for i in range(5):
    print("teste")
print("-- FIM DA REPETIÇÃO --")

#Utilizando a variável em contexto dentro da repetição
for i in range(5):
    print(f"Repetição {i}")
print("-- FIM DA REPETIÇÃO -- ")

#Determinando em qual número(index) irá começar no range(x)
for i in range(7,11):
    print(f"{i}")
print("-- FIM DA REPETIÇÃO --")

#Determinando os intervalos do range(x)
for i in range(0,11,5):
    print(f"{i}")
print("-- FIM DA REPETIÇÃO --")

#Quebrando Estrutura

#Palavras-Chaves/funções de quebra de código
#break -> quebra o laço de repetição
#quit() -> encerra o algoritmo

for i in range(1000000000000000000):
    print("repetindo")
    if i >= 10:
        break
print("-- FIM DA REPETIÇÃO --")
for i in range(1000000000000000000):
    print("repetindo")
    if i >= 10:
        quit()
print("VOCÊ NÃO VAI ENXERGAR ESSE CÓDIGO")