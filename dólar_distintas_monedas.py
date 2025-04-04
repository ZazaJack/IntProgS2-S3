cantidad_dolares = float(input("Ingrese la cantidad de dólares: "))
tasa_euros = 0.85 
tasa_libras = 0.75
tasa_yenes = 110.0

cantidad_euros = cantidad_dolares * tasa_euros
cantidiad_libras = cantidad_dolares * tasa_libras
cantidad_yenes = cantidad_dolares * tasa_yenes

print(f"Cantidad en dólares: {cantidad_dolares:.2f}")
print(f"Cantidad en euros: {cantidad_euros:.2f}")
print(f"Cantidad en libras: {cantidiad_libras:.2f}")
print(f"Cantidad en yenes: {cantidad_yenes:.2f}")
