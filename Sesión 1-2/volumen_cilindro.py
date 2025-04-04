
pi = 3.1416

radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

area_base = pi * (radio ** 2)
volumen = area_base * altura

area_lateral = 2 * pi * radio * altura
area_superficial = area_lateral + (2 * area_base)

print(f"El radio del cilindro es: {radio:.2f}")
print(f"La altura del cilindro es: {altura:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")
print(f"El área superficial del cilindro es: {area_superficial:.2f}")