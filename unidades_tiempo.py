total_segundo = int(input("Ingrese el total en segundos: "))
horas = total_segundo // 3600
minutos = (total_segundo % 3600) // 60
segundos = total_segundo % 60
print(f"Tiempo total: {horas} horas, {minutos} minutos y {segundos} segundos")