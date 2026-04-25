#Estrutura de Repetição CONDICIONADA - While
#O código irá se repetir até que a condição seja obedecida

#Exemplo: O código se repetirá até o usuário digitar algo diferente de 0 (zero)

numero = 0

while numero == 0:
    numero = int(input("Digite um número: "))
    print(f"Você digitou: {numero}")

print("Quebrou a repetição!")