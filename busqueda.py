# creacion de matrz
matriz = [
    [11, 20, 35],
    [108, 51, 63],
    [70, -98, 9]
]


# Valor a buscar
elemento_a_buscar = 9
var_bolanea=False # Elemento apra saltar la condicion boolaneao
# Función para buscar un valor en la matriz

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == elemento_a_buscar:
            var_bolanea= True
            break
    if var_bolanea:
        break
# Correcion sin funcion
if var_bolanea:
    print(f"El valor {elemento_a_buscar} se encontró en la posición ({fila}, {columna})")
else:
    print(f"No se encontró el valor {elemento_a_buscar} osición ({fila}, {columna})")



