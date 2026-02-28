#Estrutura de Condição
#Tal ação acontece se a condição for verdadeira

#Estrutura If (condição simples)
numero = int(input("Digite um número: "))

#Operadores Comparativos:
# == -> Igual a
# > -> Maior que
# >= -> Maior ou Igual a
# < -> Menor que
# <= -> Menor ou Igual a
# != -> Diferente de

if numero == 10: #Se o número for igual a 10
    print("Você digitou o número 10") #Então
else: #Senão
    print("Você não digitou o número 10") #Então

#If Encadeado (mais de uma pergunta)
#Else If - Senão Se
if numero > 0: #Se o número for maior que 0
    print("Número Positivo")
elif numero == 0: #Senão se o número for igual a 0
    print("Número Neutro")
else: #Senão
    print("Número Negativo")

#Condição Composta (If Composto)
# AND e OR -> E ou OU
# AND -> Todas condições devem ser verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 a 10")
else:
    print("Você NÃO digitou um número entre 0 a 10")

# OR -> Uma das condições devem ser verdadeiras
if numero == 6 or numero == 459 or numero == 57:
    print("Você digitou um dos números mágicos")
else:
    print("Você não digitou um dos números mágicos")