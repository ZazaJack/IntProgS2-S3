peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")

#Clasificación del IMC
if imc < 18.5:
    Clasificación = "Peso bajo"
elif 18.5 <= imc < 24.9:
    Clasificación = "Peso normal"
elif 25 <= imc < 29.9:
    Clasificación = "Sobrepeso"
else:
    Clasificación = "Obesidad"
print(f"Clasificación del IMC: {Clasificación}")
