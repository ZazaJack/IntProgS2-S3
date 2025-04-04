
""" Se debe leer el nombre del cliente, nombre del prodcuto y mostar una factura """
print("="*20)
print("Sistema de facturación")
print("="*20)
print("Ingresa los siguientes datos ")
nombre_cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto: ")
cantidad = float(input("Cantidad: "))
precio = float(input("Precio: "))

total = cantidad * precio
iva = total * 0.15
descuento = total * 0.1
monto = total + iva - descuento

# Limpiar la pantalla

import os
press_key = input("Presione cualquier tecla para continuar...")
os.system("cls || clear")
print("+"*30)
print("Factura" )
print (f"Cliente: {nombre_cliente}")
print ('Productos \t Cantidad \tPrecio \t Total')
print(f"{producto:>10} {cantidad:>10} {precio:>10} {total:>10}")
print(f"IVA: {iva}")
print(f"Descuento: {descuento}")
print(f"Monto total: {monto}")

