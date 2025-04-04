salario_bruto = float(input("Ingrese el salario bruto de su empleado: "))
impuesta_renta = salario_bruto * 0.10   
seguro_social = salario_bruto * 0.05
fondos_pensiones = salario_bruto * 0.03
descuentos_totales = impuesta_renta + seguro_social + fondos_pensiones
salario_neto = salario_bruto - descuentos_totales
print(f"El salario neto es: {salario_neto:.2f}")
print(f"Descuentos totales: {descuentos_totales:.2f}")
print(f"El salario bruto es: {salario_bruto:.2f}")
