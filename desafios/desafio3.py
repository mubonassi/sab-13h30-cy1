#Faça um algortimo
#Que converta de graus célsius para fahrenheit e kelvin
#- Equações -
#Fahrenheit: (C * 9/5) + 32
#Kelvin: C + 273.15

celsius = float(input("Digite a temperatura em ºC: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("-"*10)
print("--Temperaturas--")
print(f"Celsius: {celsius} ºC")
print(f"Fahrenheint: {fahrenheit} ºF")
print(f"Kelvin: {kelvin} K")