print("| Cadastro de Nomes |")
nomes = ["Mario","Mauro","Maria","Mauri","Marie","Pablo"]
nome = input("Digite o nome que deseja cadastrar")

if nome not in nomes:
    print("> Cadastro realizado com sucesso!")
else:
    print("> Nome existente! Digite outro nome!")