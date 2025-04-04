
duración_vuelo1 = float(input("Ingrese la duración del primer tramo del vuelo (en horas) : "))
duración_escala1 = float(input("Ingrese la duración de la primera escala (en horas) : "))
duración_vuelo2 = float(input("Ingrese la duración del segundo tramo del vuelo (en horas) : "))
duración_escala2 = float(input("Ingrese la duración de la segunda escala (en horas) : "))
duración_vuelo3 = float(input("Ingrese la duración del tercer tramo del vuelo (en horas) : "))
tiempo_total = duración_vuelo1 + duración_escala1 + duración_vuelo2 + duración_escala2 + duración_vuelo3
print(f"El tiempo total de vuelo es: {tiempo_total:.2f} horas")