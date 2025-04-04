""" Conversión de temperatura """
tempf = float(input("Ingrese la temperatura en grados Fahrenheit (F): "))
tempc = ((tempf - 32) * 5) / 9
tempk = tempc + 273.15
print("La temperatura en Celsius es:", tempc)
print("La temperatura en Kelvin es:", tempk)


