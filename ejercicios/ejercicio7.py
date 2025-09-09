
precio = float(input("Ingresa el precio original del producto: $"))
descuento = float(input("Ingresa el porcentaje de descuento (%):$"))
monto_descuento = precio * descuento / 100
precio_con_descuento = precio - monto_descuento
iva = precio_con_descuento * 0.19
precio_final = precio_con_descuento + iva
print("Descuento aplicado: $", round(monto_descuento, 5))
print("Precio después del descuento: $", round(precio_con_descuento, 2))
print("IVA (19%): $", round(iva, 2))
print("Precio final con IVA: $", round(precio_final, 2))

