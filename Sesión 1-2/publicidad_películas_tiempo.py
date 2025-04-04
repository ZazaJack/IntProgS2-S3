
duración_pelicula = float(input("Ingrese la duración de la película en minutos: "))
duración_comerciales = float(input("Ingrese la duración de los comerciales en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duración_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales = cantidad_pausas * duración_pausa
duración_total = duración_pelicula + duración_comerciales + total_comerciales

