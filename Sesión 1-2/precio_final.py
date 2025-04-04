precio_original = float(input("Introduce el precio original del producto: "))
descuento_porcentaje = float(input("Introduce el porcentaje de descuento: "))
descuento = precio_original * (descuento_porcentaje / 100)
precio_con_descuento = precio_original - descuento
iva_porcentaje = float(input("Introduce el porcentaje de IVA: "))
iva = precio_con_descuento * (iva_porcentaje / 100)
precio_final = precio_con_descuento + iva
print(f"Precio original: {precio_original:.2f}")
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Precio con descuento: {precio_con_descuento:.2f}")
print(f"IVA aplicado: {iva:.2f}")
print(f"Precio final: {precio_final:.2f}")