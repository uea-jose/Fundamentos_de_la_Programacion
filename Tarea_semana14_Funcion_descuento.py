def calcular_descuento(total, porcentaje_descuento):
    """
    #formula para calcular el descuent del total de la compra
    """
    descuento = total * (porcentaje_descuento / 100)
    return descuento # retorna el Descuento

#ingreso del usario del total compra.
total_compra = float(input("Ingrese el total de la compra: "))
porcentaje_descuento = float(input("Ingrese  ejemplo de porcentaje de descuento: 10 (10% ): "))

# Llamda a función para el descuento
descuento = calcular_descuento(total_compra, porcentaje_descuento)

# Llamda a función para el calulo de la compra menots el descuento
# formula para calcular el total desl descuento.
compra_menos_descuento= total_compra - descuento

# resultados
print("\nValor de la compra sin descuento: $", total_compra)
print("Ahorro (DESCUENTO): $", descuento)
print("Pago con descuento: $", compra_menos_descuento)