"""Cálculo del índice de masa corporal (IMC)"""
pesokg=float(input("Ingrese el peso en kilogramos: "))
alturam=float(input("Ingrese la altura en metros: "))
imc=pesokg/(alturam**2)
roundimc=round(imc, 2)
if imc<18.5:
    clasificacion="Bajo peso"
elif 18.5<=imc<25:
    clasificacion="Peso saludable"
elif 25<=imc<30:
    clasificacion="Sobrepeso"
else:
    clasificacion="Obesidad"
    
print("Peso ingresado (kg): ", pesokg)
print("Altura ingresada (m): ", alturam)
print("IMC calculado: ", imc)
print("IMC según los valores estándar: ", roundimc)
print("Clasificación: ", clasificacion)