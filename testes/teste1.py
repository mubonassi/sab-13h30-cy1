#Esse código serve para estudo/revisão de conteudo essencial

#Variaveis - Espaço na memória para guardar informações
#Exemplo nome_da_variavel = valor

texto = "Qualquer coisa" #Texto -> String
numero = 20 #Numero Inteiro -> Int/Integer
numero_real = 33.99 #Numero Real -> Float

#Comandos Básicos
#1 - print() -> Exibe uma informação (qualquer tipo de valor)
print("Banana") #Exibindo um texto puro
print(texto) #Exibindo uma variavel
print("Numero: ",numero) #Concatenando informações
print(f"E o número real é: {numero_real}")

#2 - input() -> Recebe uma informação
#Exemplo: variavel = input("Texto opcional para acompanhar o input")
texto = input("Escreva um texto aleatório: ")
numero = input("Escreva um número: ")
numero_real = input("Escreva um numero real: ")

#Exibindo as informações em um único print
print(f"Você escreveu {texto}, e você digitou o número {numero}, e o número real {numero_real}")

#Operando com Variaveis
#Exemplo 1 - com string
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nome_completo = nome + " " + sobrenome
print(f"Seu nome completo é {nome_completo}")

#Exemplo 2 - com numeros
#Necessita conversão de valores
#exemplo: variavel = tipo_da_variavel(valor)
numero1 = int(input("Digite o numero 1: "))
numero2 = int(input("Digite o numero 2: "))
numero3 = int(input("Digite o numero 3: "))
resultado = numero1 * (numero2 + numero3)
print(f"{numero1} * ({numero2} + {numero3}) = {resultado}")