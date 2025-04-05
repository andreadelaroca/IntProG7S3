""" Cálculo del tiempo total de un viaje con escalas """
ttramo1 = float(input("Ingrese la duración del primer tramo del vuelo (minutos): "))
tescala1 = float(input("Ingrese la duración de la primera escala del vuelo (minutos): "))
ttramo2 = float(input("Ingrese la duración del segundo tramo del vuelo (minutos): "))
tescala2 = float(input("Ingrese la duración de la segunda escala del vuelo (minutos): "))
ttramo3 = float(input("Ingrese la duración del tercer tramo del vuelo (minutos): "))
ttotal = (ttramo1 + tescala1) + (ttramo2 + tescala2) + ttramo3
print("El tiempo total en minutos del viaje fue:", ttotal)
