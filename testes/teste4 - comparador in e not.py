#Condição com array
lista = ["item1","item2","item3","item4","bernarda"]
item = input("Digite o item da lista que deseja escolher: ")

#Comparador IN -> verifica se está dentro da variável
if item in lista:
    print("Você escolheu um item válido")
else:
    print("Você não escolheu um item válido")

#Comparador-adicional NOT -> ele inverte a pergunta
#1 - Array
if item not in lista:
    print("Você escolheu um item que não está na lista parabéns parceiro")

#2 - Variaveis comuns
numero = 1234
if not numero == 4321:
    print("O número não é 4321")