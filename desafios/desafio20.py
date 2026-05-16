print("Sistema de Menu! Ferramentas de Conversões!")
print("-"*30)

while True:
    print("1) Centímetros -> Metros -> Kilômetros")
    print("2) Bytes -> Kilobytes -> Megabytes -> Gigabytes")
    print("3) Minutos -> Horas -> Dias")
    print("4) Miligramas -> Gramas -> Quilogramas")
    print("5) Watts -> Kilowatts -> Megawatts")
    print("6) Mililitros -> Litros -> Galões Americanos")
    print("7) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        centimetros = float(input("Digite os centímetros: "))

        metros = centimetros / 100
        kilometros = metros / 1000

        print(f"Centímetros: {centimetros}")
        print(f"Metros: {metros}")
        print(f"Kilômetros: {kilometros}")

    elif opcao == 2:

        bytes = float(input("Digite os bytes: "))

        kilobytes = bytes / 1024
        megabytes = kilobytes / 1024
        gigabytes = megabytes / 1024

        print(f"Bytes: {bytes}")
        print(f"Kilobytes: {kilobytes}")
        print(f"Megabytes: {megabytes}")
        print(f"Gigabytes: {gigabytes}")

    elif opcao == 3:

        minutos = float(input("Digite os minutos: "))

        horas = minutos / 60
        dias = horas / 24

        print(f"Minutos: {minutos}")
        print(f"Horas: {horas}")
        print(f"Dias: {dias}")

    elif opcao == 4:

        miligramas = float(input("Digite as miligramas: "))

        gramas = miligramas / 1000
        quilogramas = gramas / 1000

        print(f"Miligramas: {miligramas}")
        print(f"Gramas: {gramas}")
        print(f"Quilogramas: {quilogramas}")

    elif opcao == 5:

        watts = float(input("Digite os watts: "))

        kilowatts = watts / 1000
        megawatts = kilowatts / 1000

        print(f"Watts: {watts}")
        print(f"Kilowatts: {kilowatts}")
        print(f"Megawatts: {megawatts}")

    elif opcao == 6:

        mililitros = float(input("Digite os mililitros: "))

        litros = mililitros / 1000
        galoes = litros / 3.785

        print(f"Mililitros: {mililitros}")
        print(f"Litros: {litros}")
        print(f"Galões Americanos: {galoes}")

    elif opcao == 7:

        print("Sistema encerrado!")
        break

    else:

        print("Opção inválida!")