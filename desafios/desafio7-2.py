print("||Posto do Ipiranga||")

tanque = float(input("Digite o tamanho do tanque (l): "))
falta = float(input("Digite o quanto está faltando (l): "))

if falta > tanque or falta < 0:
    print("!!ERRO: Valor de 'falta' invalido")
else:
    enche = float(input("Digite o quanto deseja encher (l): "))
    if enche > falta:
        print("!!ERRO: Valor de 'enche' invalido!")
    else:
        print("**TANQUE ABASTECIDO COM SUCESSO**")