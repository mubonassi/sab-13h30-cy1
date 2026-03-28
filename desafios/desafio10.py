print("| Algoritmo de Acesso |")

acessos = ["admin","host","root","mestre"]
login = input("Digite o login do usuário: ")

if login in acessos:
    print("Usuário encontrado! Acesso permitido!")
else:
    print("Usuário não encontrado! Acesso negado!")