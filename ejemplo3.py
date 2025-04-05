"""Cálculo del salario neto de un empleado"""
salarbrut=float(input("Ingrese el salario bruto del empleado: "))
imprenta=salarbrut*0.1
segurosoc=salarbrut*0.05
fondopen=salarbrut*0.03
desctotal=(imprenta+segurosoc+fondopen)
salarneto=salarbrut-desctotal
print("El salario bruto es: ", salarbrut)
print("El descuento total es: ", desctotal)
print("El salario neto es: ", salarneto)
