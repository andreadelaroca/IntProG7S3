"""Conversión de una cantidad en dólares a distintas monedas"""

dolares=float(input("Ingrese la cantidad en dólares: "))
tasa_euros=0.91
tasa_libras=0.78
tasa_yenes=145.53

cantidad_euros=dolares*tasa_euros
cantidad_libras=dolares*tasa_libras
cantidad_yenes=dolares*tasa_yenes

print("La cantidad en dólares es: ", dolares)
print("La cantidad en euros es: ", round(cantidad_euros,2))
print("La cantidad en libras es: ", round(cantidad_libras,2))
print("La cantidad en yenes es: ", round(cantidad_yenes,2))