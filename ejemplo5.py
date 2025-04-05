"""Conversión de unidades de tiempo"""

cants=int((input ("Ingrese la cantidad total de segundos: ")))
canth=cants//3600
hres=cants-(canth*3600)
cantm=hres//60
sres=hres-(cantm*60)
print("Horas:  ", canth)
print("Minutos: ", cantm)
print("Segundos restantes: ", sres)