

# Definir la matriz
matriz2 = [
    [122, 108, 3],
    [10, 9, 8],
    [4, 5, 2]
]

#funcion ordenar con sort()
#def ordenar_fila(matriz2, fila):
 #   matriz2[fila] = sorted(matriz2[fila])
 #   return matriz2


# Fila a ordenar (empezando desde 0)
#fila_a_ordenar = 1

# Impresion matriz original
print("=====Matriz original======:")
for i in matriz2:
    print(i, end=" ")
    print()
print("============================")

# llama a funcion y ordernar matriz
#matriz_ordenada = ordenar_fila(matriz2, fila_a_ordenar)
#ordenacion de matriz

for i in matriz2:
    i.sort()
# Mostrar matriz con la fila ordenada
print("\n=====Matriz Ordenada======:")
for i in matriz2:
    print(i, end=" ")
    print()
print("============================")