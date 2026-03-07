print("||Sistema de Cadastro e Login||")
print("> Realizando o cadastro!")
usuarioCad = input("Digite o Usuário:")
senhaCad = input("Digite a Senha: ")

print("|Cadastrado com Sucesso|")

print("> Realizando o login!")
usuarioLogin = input("Usuário: ")
senhaLogin = input("Senha: ")

if usuarioCad == usuarioLogin and senhaCad == senhaLogin:
    print("**FALHA DE LOGIN FALHADO COM SUCESSO**")
else:
    print("!!SUCESSO DE LOGIN FALHADO COM SUCESSO!!")