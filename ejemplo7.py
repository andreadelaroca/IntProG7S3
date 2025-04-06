"""Cálculo del precio final de un producto con impuestos y descuentos 
"""
precio=float(input("Ingrese el precio original ($): "))
desc=float(input("Ingrese el porcentaje de descuento aplicado: "))
desc=desc/100
descuento=precio*desc
precio_desc=precio-descuento

iva=float(input("Ingrese el porcentaje de IVA: "))
iva=iva/100
impuesto=precio_desc*iva
precio_final=precio_desc+impuesto

print("Precio original ($): ", precio)
print("Descuento aplicado ($): ", descuento)
print("Precio con descuento ($)", precio_desc)
print("IVA calculado ($): ", impuesto)
print("Precio final ($): ", precio_final)