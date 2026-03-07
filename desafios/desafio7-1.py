print("||Posto do Ipiranga||")

tanque = float(input("Digite o tamanho do tanque (l): "))
falta = float(input("Digite o quanto está faltando (l): "))
enche = float(input("Digite o quanto deseja encher (l): "))

if falta > tanque or falta < 0:
    print("Erro: Valor de 'falta' está inválido!")
elif enche > falta:
    print("Erro: Valor de 'enche' excede o limite!")
else:
    print("Tanque abastecido com sucesso!")