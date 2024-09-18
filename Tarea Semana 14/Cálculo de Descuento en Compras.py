#Funcion paracalcular de Descuento en Compras
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento y devuelve el monto del descuento"""
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# el monto total de la compra
monto1 = 100
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Monto total: ${monto1}, Descuento: ${descuento1}, Monto final a pagar: ${monto_final1}")

monto2 = 200
porcentaje2 = 15
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2
print(f"Monto total: ${monto2}, Descuento: ${descuento2}, Monto final a pagar: ${monto_final2}")
