"""Cálculo del volumen de un cilindro y su área superficial"""
r=float(input("Ingrese el radio del cilindro: "))
h=float(input("Ingrese la altura del cilindro: "))

pi=3.1416
area_base=pi*(r**2)
vol=area_base*h
area_lateral=2*pi*r*h
area_superficial=area_lateral+2*area_base

print("El radio del cilindro es ",r)
print("La altura del cilindro es ",h)
print("El volumen calculado es ",vol)
print("El área superficial calculada es ",area_superficial)