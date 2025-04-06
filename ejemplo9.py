"""Cálculo del tiempo total de una película con comerciales"""

tiempo_min=float(input("Ingrese la duración de la película en minutos: "))
tiempo_comercialesprev=float(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas=int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
tiempo_pausas=float(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales=cantidad_pausas*tiempo_pausas
tiempo_total=tiempo_min+tiempo_comercialesprev+total_comerciales

print("La duración original de la película en minutos es ",tiempo_min)
print("La duración total de los comerciales en minutos es ",total_comerciales)
print("La duración total de la película en minutos es ",tiempo_total)