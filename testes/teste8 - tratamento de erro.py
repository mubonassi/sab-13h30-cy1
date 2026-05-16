#Tratamento de Erro
#Interceptar o erro e fazer a tratativa, criando um código como resposta ao possível erro

#try -> vai executar o código e pegar um possível erro
#except -> o código de reação ao possível erro
#else -> o código caso não retorne erro
#finally -> o código é executado independentemente

try:
    numero = int(input("Digite um N Ú M E R O: "))
except ValueError:
    print("Idiota, é para digitar um N  Ú  M  E  R  O")
except:
    print("Deu erro")
else:
    print(f"Você digitou o número {numero}")
finally:
    print("Fim de código")

#exemplos de erros
#ValueError -> Valor inválido (int("abc"))
#TypeError -> Tipo errado ("S" + 10)
#NameError -> Variável Não Existe (print(variavel))
#ZeroDivisionError -> Divisão por Zero (10/0)
#OverflowError -> Número Gigante para Processar