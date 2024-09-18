#Funcion para calcular de descuento en compras
def calcular_descuento(monto_total, porcentaje_descuento=10):
    "Calcula el descuento y devuelve el monto del descuento"
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# El monto total de la compra
monto_tot1 = 100
descuen1 = calcular_descuento(monto_tot1)
monto_fin1 = monto_tot1 - descuen1
print(f"Monto total: ${monto_tot1}, Descuento: ${descuen1}, Monto final a pagar: ${monto_fin1}")

# El monto total de la compra como el porcentaje de descuento.
monto_tot2 = 250
porcentaje2 = 15
descuen2 = calcular_descuento(monto_tot2, porcentaje2)
monto_fin2 = monto_tot2 - descuen2
print(f"Monto total: ${monto_tot2}, Descuento: ${descuen2}, Monto final a pagar: ${monto_fin2}")
