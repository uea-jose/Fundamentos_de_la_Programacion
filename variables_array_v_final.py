# Declaración y asignación de arreglos multidimensionales
# 1.     Declare 6 variables unidimensionales y asigne valores entero
# guardas los 6 arrelgos en las variables
# Declaración y asignación de arreglos multidimensionaleso
print("================ ARREGLOS UNIDIMENSIOANLES ======================")
print("================================================================")
array_uni_1 = [12, 2, 3, 43]
array_uni_2 = [1, 3, 44, 1, -23]
array_uni_3 = [1, -1, 99, 23, -26, 34, -56, ]
array_uni_4 = [1, 9]
array_uni_5 = [-1, 0, 0, 23, 12, 23, 4, 4, 4]
array_uni_6 = [2, 23, -9, 23]
print("----------------------------------------------")
print("---1. Arreglos Unidimensionales con Enteros---")
print("----------------------------------------------")
# Imprime los 6 arreglos  unidimensionales
print("Array 1 = ", array_uni_1)
print("Array 2 = ", array_uni_2)
print("Array 3 = ", array_uni_3)
print("Array 4 = ", array_uni_4)
print("Array 5 = ", array_uni_5)
print("Array 6 = ", array_uni_6)

# 2. Declare 6 variables unidimensionales y asigne valores flotantes
# Asignacion de numeros float y guardar en arreglos
array_f1 = [5.3, 2.34, 35.3, 43.2]
array_f2 = [1.23, 33.5, 44.3, 100.3, -23, 23]
array_f3 = [1.23, -14, 2, 99.23, 23.2, -26.23, 34.2, -56.34, ]
array_f4 = [1.2, 9.23]
array_f5 = [-1.2, 0.23, 0.5, 23.34, 12.23, 23.40, 4.1, 422.23, 4232.3]
array_f6 = [2.23, 2.233, -9.23, 23.23]
print("------------------------------------------------")
print("---2. Arreglos Unidimensionales con flotantes---")
print("------------------------------------------------")
# Imprime los 6 arreglos  unidimensionales
print("Array f1 = ", array_f1)
print("Array f2 = ", array_f2)
print("Array f3 = ", array_f3)
print("Array f4 = ", array_f4)
print("Array f5 = ", array_f5)
print("Array 66 = ", array_f6)
# 3.     Declare 6 variables unidimensionales y asignar valores de texto
array_txt1 = ["Ducati", "pelota", "Orlando", "loro"]
array_txt2 = ["carro", "perro"]
array_txt3 = ["bicicelta", "panaderia", "passwd", "Karla", "pera"]
array_txt4 = ["naturalez", "1234", "-Pila-"]
array_txt5 = ["++++", "****", "rise"]
array_txt6 = ["cocoa", "lote", "casa"]
print("------------------------------------------------")
print("---3. Arreglos Unidimensionales con texto  -----")
print("------------------------------------------------")
# Imprime los 6 arreglos  unidimensionales
print("Array txt1 = ", array_txt1)
print("Array txt2 = ", array_txt2)
print("Array txt3 = ", array_txt3)
print("Array txt4 = ", array_txt4)
print("Array txt5 = ", array_txt5)
print("Array txt6 = ", array_txt6)

# 4.  Declare 6 variables unidimensionales y asignar valores de enteros, flotantes y texto
array_mix1 = [4, "pelota", 34.5, "loro"]
array_mix2 = ["carro", 34]
array_mix3 = [-23, 34, "panaderia", 0, "Karla", "pera"]
array_mix4 = [-300, "1234", 34.54]
array_mix5 = [34, 4.5, "rise"]
array_mix6 = [0, "lote", 3.4]
print("------------------------------------------------------")
print("---4. Arreglos Unidimensionales mix: int-txt-float ---")
print("------------------------------------------------------")
# Imprime los 6 arreglos  unidimensionales
print("Array mix1 = ", array_mix1)
print("Array mix2 = ", array_mix2)
print("Array mix3 = ", array_mix3)
print("Array mix4 = ", array_mix4)
print("Array mix5 = ", array_mix5)
print("Array mix6 = ", array_mix6)
print()
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Declaración y asignación de arreglos multidimensionaleso
print("================ ARREGLOS BIDIMENCIONALES ======================")
print("================================================================")
# Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores enteros (6 variables en total)
print("-------------------------------------------------")
print("---5. Arreglos Bidimensionales con Enteros ------")
print("-------------------------------------------------_")
print("____5.1. Arreglos Bi de 2x3 (int) ____")
# Declaración Arreglo 1 de enteros de 2x3
array_bi_int1 = [
    [2, 3, 4],
    [0, 2, 2]
]
# Declaración Arreglo 2 de enteros de 2x3
array_bi_int2 = [
    [-3, 3, -5],
    [9, 0, 23]
]
# Impresion de la bi matriz1 int 2x3 de mejor manera
print("______5.1.1 Array1 bi_int1_2x3 :")
for i in array_bi_int1:
    print(i, end=" ")
    print()
# Impresion de la bi matriz2 int 2x3 de mejor manera
print("______5.1.2 Array2 bi_int_2x3 :")
for i in array_bi_int2:
    print(i, end=" ")
    print()
print()
print("____5.2. Arreglos Bi de 5x5 (int) ____")
# Arreglo 1 de enteros bi de 5x5
array_bi_int3 = [
    [2, 3, 4, 5, -2],
    [3, -3, 0, 34, 13],
    [13, 2, 9, 3, 0],
    [1, 0, 0, 0, 2],
    [2, 56, 0, -2, 12]
]
# Impresion de la bi matriz1 int 5x5 de mejor manera
print("______5.2.1 Arreglo1_bi_int_5x5 :")
for i in array_bi_int3:
    print(i, end=" ")
    print()
# Arreglo 2 de enteros bi de 5x5
array_bi_int4 = [
    [43, 3, 30, -5, -22],
    [33, -31, 10, 3, 3],
    [3, 29, 92, 23, 0],
    [1, 2, 4, 5, 5],
    [-2, -6, 0, -5, 2]
]
print()
print("______5.2.2 Arreglo2_bi_int_5x5:")
# Impresion de la matriz2  5x5 de mejor manera
for i in array_bi_int4:
    print(i, end=" ")
    print()
print()
print("____5.3 Arreglos Bi de 3x6 (int) ____")
# Declaracion arreglo1 Bidimensional 3x6_enteros
array_bi1_3x6 = [
    [0, 2, 34, -12, 23, 9],
    [-1, 3, -63, -8, 1, 5],
    [14, 23, 0, 0, -9, 2]
]
print("______5.3.1 Arreglo1_bi_int_3X6 :")
# Impresion de la matriz1  3x6 de mejor manera
for i in array_bi1_3x6:
    print(i, end=" ")
    print()
print()
# Declaracion arreglo2 Bidimensional 3x6_enteros
array_bi2_3x6 = [
    [2, -12, 0, -0, 3, 19],
    [-14, 43, -3, -18, 11, 15],
    [-1, 1, 0, 20, -9, 18]
]
print("______5.3.2 Arreglo2_bi_int_3X6 :")
# Impresion de la matriz2  3x6 de mejor manera
for i in array_bi2_3x6:
    print(i, end=" ")
    print()
print()
print("------------------------------------------------")
print("---6. Arreglos Bidimensionales con Flotantes ---")
print("------------------------------------------------")
# 6.Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores flotantes
# (6 variables en total)
print("____6.1 Arreglos BI de 2x3 (float)_____")
# Declaracion arreglo1 Bidimensional 2x3_flotantes
array1_bi_flt_2x3 = [
    [-2.23, 12.3, 0.4],
    [0.23, 1.2, -23.2]
]
# Declaracion arreglo2 Bidimensional 25x3_flotantes
array2_bi_flt_2x3 = [
    [-33.3, 8.9, -5.0],
    [9.1, 0.34, 2.3]
]

# Impresion de la matriz|  2x3 flotantes de mejor manera
print("______6.1.1 Arreglo1_bi_flt_2X3 :")
for i in array1_bi_flt_2x3:
    print(i, end=" ")
    print()
# Impresion de la matriz2  2x3 de mejor manera
print("______6.1.2 Arreglo2_bi_flt_2X3:")
for i in array2_bi_flt_2x3:
    print(i, end=" ")
    print()
print()
print("____6.2 Arreglos Bi de 5x5 (float)_____")
# Declaracion arreglo1 Bidimensional 5x5_flotantes
array1_bi_flt_5x5 = [
    [2.57, -3.09, 4.25, 5.5, -2.64],
    [63.98, -31.324, 0.93, 3.4, 1.3],
    [-1.3, -22.2, 9.999, 3.09, 0.43],
    [1.0, 0.0, 0.234, -30.4, 2.45],
    [7.2, 56, 0, -2.5, 1.2]
]

# Declaracion arreglo2 Bidimensional 5x5_flotantes
array2_bi_flt_5x5 = [
    [4.3, 0.3, 3.0, -4.5, -2.2],
    [3.3, -3.1, 0.1, -3.45, 4.3],
    [-13.3, -29.3, 9.2, 2.3, 0],
    [1.12, -2.32, 4.5, 5.5, -93.0],
    [-2.5, -6.18, 0.93, -54.3, 2.11]
]
# Impresion de la matriz1 Bidimensional 5x5 flotantes de mejor manera
print("______6.2.1 Arreglo1_bi_flt_5x5 :")
for i in array1_bi_flt_5x5:
    print(i, end=" ")
    print()
print()
# Impresion de la matriz2 Bidimensional 5x5 flotantes de mejor manera
print("______6.2.2 Arreglo1_bi_flt_5x5 :")
for i in array2_bi_flt_5x5:
    print(i, end=" ")
    print()
print()
print("____6.3 Arreglos Bi de 3x6 (float)_____")
# Declaracion arreglo1 Bidimensional 3x6_float
array1_bi_flt_3x6 = [
    [0.5, 2.45, 34.45, -1.2, 2.3, 1.9],
    [-12.63, 33.45, -0.3, -0.8, 0.1, 0.5],
    [1.4, 2.3, 0, 0, -9, 2]
]
# Declaracion arreglo2 Bidimensional 3x6_float
array2_bi_flt_3x6 = [
    [2, -12, 0, -0, 3, 19],
    [-14, 43, -3, -18, 11, 15],
    [-1, 1, 0, 20, -9, 18]
]

# Impresion de la matriz1 Bidimensional 3x6 flotantes de mejor manera
print("______6.3.1 Arreglo1_bi_flt_3x6:")
for i in array1_bi_flt_3x6:
    print(i, end=" ")
    print()
print()

# Impresion de la matriz2 Bidimensional 3x6 flotantes de mejor manera
print("______6.3.2 Arreglo2_bi_flt_3x6:")
for i in array2_bi_flt_3x6:
    print(i, end=" ")
    print()
print()
# 7. Declare 2 variables bidimensionales 2x3, 5x5, 3x6 #asignar valores de texto (6 variables en total)
print("----------------------------------------------")
print("---7. Arreglos Bidimensionales con Texto------")
print("----------------------------------------------")
# 6.Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores txt
# (6 variables en total)
print("____7.1 Arreglos Bi de 2x3 (txt)_______")
# Declaracion arreglo1 Bidimensional 2x3_txt
Arreglo1_bi_txt_2X3 = [
    ["Piedra", "te", "pera"],
    ["torre", "polo", "tata"]
]
# Declaracion arreglo2 Bidimensional 2x3_txt
Arreglo2_bi_txt_2X3 = [
    ["#64", "tesla", "pato"],
    ["taza", "castillo", "latido"]
]
# Impresion de la matriz1 Bidimensional txt  2x3   de mejor manera
print("______7.1.1 Arreglo1_bi_txt_2X3 :")
for i in Arreglo1_bi_txt_2X3:
    print(i, end=" ")
    print()
print()
print("______7.1.2 Arreglo2_bi_txt_2X3 :")
# Impresion de la matriz2 Bidimensional  txt 2x3   de mejor manera
for i in Arreglo2_bi_txt_2X3:
    print(i, end=" ")
    print()
print()
print("____7.2 Arreglos Bi de 5x5 (txt)_____")
# Declaracion arreglo1 Bidimensional 5x5_txt
array1_bi_txt_5x5 = [
    ["t2", "pi", "e`^x", "2^x", "texto"],
    ["matematicas", "literatura", "Historia", "ciencia", "lengua"],
    ["3,14", "ctte", "fuerza", "newton", "ley"],
    ["fisca", "masa", "tiempo", "aceleraciob", "resorte"],
    ["potencia", "corriente", "voltaje", "graveda", "parabola"]
]
# Declaracion arreglo2 Bidimensional 5x5_txt
array2_bi_txt_5x5 = [
    ["in", "cm", "ft", "m", "mi"],
    ["km", "milla", "fermi", "año-luz", "dia"],
    ["año", "kq", "lb", "N", "J"],
    ["eV", "kWh", "W", "hp", "Hz"],
    ["V", "T", "Wb", "t", "rad"]
]
# Calcular la longitud del elemento más largo en cada columna, dato que sirve para ordenar de mejor manera
longitudes = [max(len(str(array1_bi_txt_5x5[i][j])) for i in range(5)) for j in range(5)]
# Impresion de la matriz1  Bidimensional txt 5x5 de mejor manera  ordenada
print("______7.2.1 Arreglo_bi_txt_5x5 :")
for i in range(5):
    print("[", end="")
    for j in range(5):
        print(f"{array1_bi_txt_5x5[i][j]:<{longitudes[j]}}", end=" ")
    print("]")
print()

print("______7.2.2 Arreglo_bi_txt_5x5 :")
# Impresion de la matriz2  Bidimensional txt 5x5 de mejor manera  ordenada
for i in range(5):
    print("[", end="")
    for j in range(5):
        print(f"{array2_bi_txt_5x5[i][j]:<{longitudes[j]}}", end=" ")
    print("]")
print()
print("____7.3 Arreglos Bi de 3x6 (txt)_____")
# Declaracion arreglo1 Bidimensional 3x6_txt
array1_bi_txt_3x6 = [
    ["longitud", "energia", "presion", "masa", "fuera", "angulo"],
    ["ralidez", "luz", "carga", "electron", "planck", "molecula"],
    ["neutron", "espacio", "calor", "presion", "calor", "atomo"]
]
# Declaracion de arreglo 2 Bidimensional txt 3x6
array2_bi_txt_3x6 = [
    ["sol", "luna", "mercurio", "venus", "tierra", "marte"],
    ["jupiter", "saturni", "urano", "neptuno", "pluton", "centauri"],
    ["sirio", "polux", "arturo", "aldebaran", "rigal", "antares"]
]
# Impresion de la matriz1  3x6 de mejor manera y ordenada
print("______7.3 Arreglo_bi_txt_3x6 :")
# Calcular la longitud del elemento más largo en cada columna, dato que sirve para ordenar ls numeros
longitudes = [max(len(str(array1_bi_txt_3x6[i][j])) for i in range(3)) for j in range(6)]
# Impresion de la matriz1  Bidimensional txt 3x6 de mejor manera y ordenada
for i in range(3):
    print("[", end=" ")
    for j in range(6):
        print(f"{array1_bi_txt_3x6[i][j]:>{longitudes[j]}}", end="  ")
    print("]")
print()
# Impresion de la matriz2  3x6 de mejor manera y ordenada
print("______7.3 Arreglo_bi_txt_3x6 :")
# Impresion de la matriz2  3x6 de mejor manera y ordenada
# Calcular la longitud del elemento más largo en cada columna, dato que sirve para ordenar ls numeros
longitudes = [max(len(str(array2_bi_txt_3x6[i][j])) for i in range(3)) for j in range(6)]
for i in range(3):
    print("[", end="")
    for j in range(6):
        print(f"{array2_bi_txt_3x6[i][j]:>{longitudes[j]}}", end="  ")
    print("]")
print()
# 8.     Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de
# enteros, flotantes y texto (6 variables en total)
print("-----------------------------------------------------------")
print("---8. Arreglos Bidimensionales con mix: int,txt,float------")
print("-----------------------------------------------------------")
print("____8.1 Arreglos Bi de 2x3 (int-txt-float)_______")
# Declaracion arreglo1 Bidimensional 2x3_int, txt, float------
Arreglo1_bi_int_txt_fl_2X3 = [
    [2, "casa", 7.2],
    [-23, "pepe", -34.23]
]
# Declaracion arreglo2 Bidimensional 2x3_int, txt, float------
Arreglo2_bi_int_txt_fl_2X3 = [
    [34, "todos", -0.234],
    [-9, "float", -9.23]
]
# Impresion de la matriz1 Bidimensional txt  2x3   de mejor manera
print("______8.1.1 Arreglo1_bi_int_txt_fl_2X3 :")
for i in Arreglo1_bi_int_txt_fl_2X3:
    print(i, end=" ")
    print()
print()
print("______8.1.2 Arreglo2_bi_int_txt_fl_2X3 :")
# Impresion de la matriz2 Bidimensional  txt 2x3   de mejor manera
for i in Arreglo2_bi_int_txt_fl_2X3:
    print(i, end=" ")
    print()
print()
print("____8.2 Arreglos Bi de 5x5 (int-txt-float)_____")
# Declaracion arreglo1 Bidimensional 5x5_txt, int, float
Arreglo1_bi_int_txt_fl_5X5 = [
    [23, "ti", 23.4, "perla", -23],
    [-4, "laura", -2.32, -200, "lengua"],
    [10, "ctte", -23.132, 0, "lados"],
    [100, "moto", 7.5, 6, "resorte"],
    [1000, "capcidad", -100.03, 19, "grifo"]
]
# Declaracion arreglo2 Bidimensional 5x5_txt, int, float
Arreglo2_bi_int_txt_fl_5X5 = [
    [234, "mm", 0.123, 1000, "you"],
    [0, "milla", -103.45, 23, "dona"],
    [-17, "queso", 8.9, 90, "p"],
    [2219, "cabello", 3.14, 34, "pelea"],
    [1, "dos", 234.222, 39, "radio"]
]
# Calcular la longitud del elemento más largo en cada columna, dato que sirve para ordenar de mejor manera
longitudes = [max(len(str(array1_bi_txt_5x5[i][j])) for i in range(5)) for j in range(5)]
# Impresion de la matriz1  Bidimensional txt 5x5 de mejor manera  ordenada
print("______8.2.1 Arreglo1_bi_int_txt_fl_5X5 :")
for i in range(5):
    print("[", end="")
    for j in range(5):
        print(f"{Arreglo1_bi_int_txt_fl_5X5[i][j]:<{longitudes[j]}}", end=" ")
    print("]")
print()

print("______8.2.2 Arreglo2_bi_int_txt_fl_5X5 :")
# Impresion de la matriz2  Bidimensional txt 5x5 de mejor manera  ordenada
for i in range(5):
    print("[", end="")
    for j in range(5):
        print(f"{Arreglo2_bi_int_txt_fl_5X5[i][j]:<{longitudes[j]}}", end=" ")
    print("]")
print()
print("____8.3 Arreglos Bi de 3x6 (int-txt-float)_____")
# Declaracion arreglo1 Bidimensional 3x6_txt, int, float
Arreglo1_bi_int_txt_fl_3X6 = [
    [20, "Elena", -2.3, 93, "furia", -2.12],
    [1200, "late", 2.231212, -48, "platano", -92.2],
    [10, "eter", 20.101, 102, "jota", 9.29]
]
# Declaracion de arreglo 2 Bidimensional 3x6 txt, int, float
Arreglo2_bi_int_txt_fl_3X6 = [
    [-921, "pajaro", -292.101, 9, "tambor", -191.202],
    [2, "samurai", 716.29, -1000, "rojo", 0.00001],
    [0, "kilo", 20.2, 41, "galon", 03.393]
]
# Impresion de la matriz1  3x6 de mejor manera y ordenada
print("______8.3.1 Arreglo1_bi_int_txt_fl_3X6 :")
# Calcular la longitud del elemento más largo en cada columna, dato que sirve para ordenar ls numeros
longitudes = [max(len(str(Arreglo1_bi_int_txt_fl_3X6[i][j])) for i in range(3)) for j in range(6)]
# Impresion de la matriz1  Bidimensional txt 3x6 de mejor manera y ordenada
for i in range(3):
    print("[", end=" ")
    for j in range(6):
        print(f"{Arreglo1_bi_int_txt_fl_3X6[i][j]:>{longitudes[j]}}", end="  ")
    print("]")
print()
# Impresion de la matriz2  3x6 de mejor manera y ordenada
print("______8.3.2 Arreglo2_bi_int_txt_fl_3X6 :")
# Impresion de la matriz2  3x6 de mejor manera y ordenada
# Calcular la longitud del elemento más largo en cada columna, dato que sirve para ordenar ls numeros
longitudes = [max(len(str(Arreglo2_bi_int_txt_fl_3X6[i][j])) for i in range(3)) for j in range(6)]
for i in range(3):
    print("[", end="")
    for j in range(6):
        print(f"{Arreglo2_bi_int_txt_fl_3X6[i][j]:>{longitudes[j]}}", end="  ")
    print("]")
print()
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Declaración y asignación de arreglos multidimensionaleso
print("================ ARREGLOS TRIDIMENCIONALES ======================")
print("================================================================")
#9.     Declare 2 variables tridimensionales 2x3x2, 5x5x5, 3x6x2 
#y asigne valores enteros (6 variables en total)
print("-------------------------------------------------")
print("---9. Arreglos Tridimensionales con Enteros ------")
print("-------------------------------------------------_")
print("____9.1. Arreglos Bi de 2x3x2 (int) ____")
#Declaración Arreglo 1 de enteros de 2x3x2
# Matriz 2x3x2
Arreglo1_3D_int_2x3x2 = [
    [[2, 1], [-1 , 2], [-2, 4]],
    
    [[1, 3], [2, 4],   [3, 7]]
]
#Declaración Arreglo 2 de enteros de 2x3x2
Arreglo2_3D_int_2x3x2 = [
    [[29, 10], [-10 , 29], [-29, 44]],
    
    [[14, 33], [23, 43],   [33, 73]]
]

#Impresion de la  matriz1 3d  2x3x2  enteros
print("______9.1.1 Arreglo1_3D_int_2x3x2:___")
#arrelgo de tal manera que se vea de 2x3x3
for i in Arreglo1_3D_int_2x3x2:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   
 



#Impresion de la bi matriz2 int 2x3 de mejor manera
print("______9.1.2 Arreglo2_3D_int_2x3x2:")
#arrelgo de tal manera que se vea de 2x3x3
for i in Arreglo2_3D_int_2x3x2:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   
   
      


print("____9.2. Arreglos Bi de 5x5x5 (int) ____")
#Declaración Arreglo 1 de enteros de 5x5x5
# Matriz 2x3x2
Arreglo1_3D_int_5x5x5 = [
    [
    [0, 0, 3, 2 , 3], 
    [0, 0, 4, 3, 12],
    [10, 2, 4, 0, 1],
    [10, 2, -4, 0, -1],
    [2, -22, 4, 0, -1]],
   
    [
    [0, 0, 3, 2 , 3], 
    [0, 0, 4, 3, 12],
    [10, 2, 4, 0, 1],
    [10, 2, -4, 0, -1],
    [2, -22, 4, 0, -1]],
   
    
    [
    [0, 0, 3, 2 , 3], 
    [0, 0, 4, 3, 12],
    [10, 2, 4, 0, 1],
    [10, 2, -4, 0, -1],
    [2, -22, 4, 0, -1]],
   
   
    [
    [0, 0, 3, 2 , 3], 
    [0, 0, 4, 3, 12],
    [10, 2, 4, 0, 1],
    [10, 2, -4, 0, -1],
    [2, -22, 4, 0, -1]],
   
    [
    [0, 0, 3, 2 , 3], 
    [0, 0, 4, 3, 12],
    [10, 2, 4, 0, 1],
    [10, 2, -4, 0, -1],
    [2, -22, 4, 0, -1]],
   
]
#Declaración Arreglo 2 de enteros de 2x3x2
Arreglo2_3D_int_5x5x5 = [
    [
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]],
    [
    [1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]],
    [
    [2, 2, 2, 2, 2], 
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2]],
 
    [
    [3, 3, 3, 3, 3], 
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]],
    [
    [4, 4, 4, 4, 4], 
    [4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4]],
]
 
#Impresion de la  matriz1 3d  5x5x5  enteros
print("______9.2.1 Arreglo1_3D_int_5x5x5:")
for i in Arreglo1_3D_int_5x5x5:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   
   
      

#Impresion de la  matriz2 3d  5x5x5  enteros
print("______9.2.2 Arreglo2_3D_int_5x5x5:")
#arrelgo de tal manera que se vea de 5x5x5
for i in Arreglo2_3D_int_5x5x5:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   
   
      
print("____9.3. Arreglos Bi de Arreglo2_3D_int_3x6x2 (int) ____")
#Declaración Arreglo 1 de enteros de 3x6x2 enteros
Arreglo1_3D_int_3x6x2 = [
    [[0, -1], [1, 2], [3, 4], [-2, 3], [4, 3], [-30 ,34]
    ],
    [[3,  3],  [2, 1], [0, 0], [2, 0], [1, 2], [-3, -4]
    ],
    [[-2,-4],  [2, 4], [2, 3], [2, 3], [9, 3], [2,  3]
    ]
    ]
#Declaración Arreglo 2 de enteros de 3x6x2 enteros 
Arreglo2_3D_int_3x6x2 = [
    [[9, 8], [7, 6], [5, 4], [3, 2], [1, 0], [10, 11]],
    [[12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [22, 23]],
    [[24, 25], [26, 27], [28, 29], [30, 31], [32, 33], [34, 35]]
]  
#Impresion de la  matriz1 3d  3x6x2  enteros
print("______9.3.1 Arreglo1_3D_int_3x6x2:")
for i in Arreglo1_3D_int_3x6x2:
    for j in i:
        print(str(j).rjust(8), end="  ")
    print()
print()   
   
#Impresion de la  matriz2 3d  3x6x2  enteros
print("______9.3.2 Arreglo2_3D_int_2x3x2:")
for i in Arreglo2_3D_int_3x6x2:
    for j in i:
        print(str(j).rjust(8), end="  ")
    print()
print()   
   
      

print("-----------------------------------------------------")
print("---10. Arreglos Tridimensionales con Flotantes ------")
print("-----------------------------------------------------")
print("___10.1. Arreglos 3D de 2x3x1 (float) ____")
#Declaración Arreglo 1 de enteros de 2x3x1
Arreglo1_3D_fl_2x3x1 = [
   [
       [2.2], [1.23], [4.23]
   ],
   [
       [5.23], [5.23], [2.23]
       ]
   
]
#Declaración Arreglo 2 de enteros de 2x3x2
Arreglo2_3D_fl_2x3x1 = [
   [
       [-2.2], [-1.23], [-4.23]
   ],
   [
       [-5.23], [-5.23], [-2.23]
       ]
]

#Impresion de la  matriz1 3d  2x3x1  float
print("_____10.1.1 Arreglo1_3D_fl_2x3x1:")
for i in Arreglo1_3D_fl_2x3x1:
    for j in i:
        print(str(j).rjust(8), end="  ")
    print()
print()   
   
print("_____10.1.2 Arreglo1_3D_fl_2x3x1:")
for i in Arreglo2_3D_fl_2x3x1:
    for j in i:
        print(str(j).rjust(8), end="  ")
    print()
print()   
   

print("___10.2. Arreglos Bi de 5x5x2 (float) ____")
#Declaración Arreglo 1 de float de 5x5x2
# Matriz 2x3x2
Arreglo1_3D_fl_5x5x2 = [
      [
        [2.3,-2.3], [1.34, 0.03], [-0.23, 93.92], [19.1, 3.02], [-2.2, 1.2]
    ],
    [
        [1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, -8.8], [-2.2, -3.3]],
    [
        [2.4, 39.10], [8.9, 30.23], [2.3, -9.34], [-3.14, 2.14], [3.34, -3.9]],
    [
        [2.23, -18.9], [72.9, -36.93], [12.21, 9.47], [2.2, 9.3], [-1.2, -3.4]],
    [
        [0.3, -0.3], [1.3, -3.4], [2.9, -84.92], [39.39, -283.58], [282.49, -393.30]]
]
   
    
#Declaración Arreglo 2 de float de 5x5x2
Arreglo2_3D_fl_5x5x2 =  [
    [[9.9, 8.8], [7.7, 6.6], [5.5, 4.4], [3.3, 2.2], [1.1, 0.0]],
    [[0.0, 1.1], [2.2, 3.3], [4.4, 5.5], [6.6, -7.7], [8.8, -9.9]],
    [[10.0, 20.0], [30.0, 40.0], [50.0, 60.0], [70.0, 80.0], [90.0, 100.0]],
    [[-10.0, 20.0], [30.0, 40.0], [50.0, 60.0], [70.0, 80.0], [90.0, 100.0]],
    [[-100.0, -200.0], [-300.0, -400.0], [-500.0, -600.0], [-700.0, -800.0], [-900.0, -1000.0]]
]
#Impresion de la  matriz1 3d  5x5x2  float
print("______10.2.1 Arreglo1_3D_fl_5x5x2:")
#arrelgo de tal manera que se vea de 5x5x2
for i in Arreglo1_3D_fl_5x5x2:
    for j in i:
        print(str(j).rjust(20), end="   ")
    print()
print()   
   
    
#Impresion de la  matriz2 3d  5x5x2  float
print("______10.2.2 Arreglo2_3D_fl_5x5x2:")
#arrelgo de tal manera que se vea de 5x5x2
for i in Arreglo2_3D_fl_5x5x2:
    for j in i:
        print(str(j).rjust(20), end="   ")
    print()
print()   
   
    
print()  # Nueva línea al final de cada dimensión en el eje x
print("____10.3. Arreglos 3D de_3x6x5 (float) ____")
#Declaración Arreglo 1 de enteros de 3x6x5 float
Arreglo1_3D_fl_3x6x5 = [
    [[3.2, 3.2, 3.2, 3.2, 3.2], [-5.9, -5.9, -5.9, -5.9, -5.9], [0.5, 0.5, 0.5, 0.5, 0.5], [10.309, 10.309, 10.309, 10.309, 10.309], [3.3, 3.3, 3.3, 3.3, 3.3], [-5.5, -5.5, -5.5, -5.5, -5.5]],
    [[3.2, 3.2, 3.2, 3.2, 3.2], [-5.9, -5.9, -5.9, -5.9, -5.9], [0.5, 0.5, 0.5, 0.5, 0.5], [10.309, 10.309, 10.309, 10.309, 10.309], [3.3, 3.3, 3.3, 3.3, 3.3], [-5.5, -5.5, -5.5, -5.5, -5.5]],
    [[3.2, 3.2, 3.2, 3.2, 3.2], [-5.9, -5.9, -5.9, -5.9, -5.9], [0.5, 0.5, 0.5, 0.5, 0.5], [10.309, 10.309, 10.309, 10.309, 10.309], [3.3, 3.3, 3.3, 3.3, 3.3], [-5.5, -5.5, -5.5, -5.5, -5.5]]
    ]


   

 
#Declaración Arreglo 2 de enteros de 3x6x1 float 
Arreglo2_3D_fl_3x6x5 = [
    [[3.5, 3.5, 3.5, 3.5, 3.5], [-6.0, -6.0, -6.0, -6.0, -6.0], [0.6, 0.6, 0.6, 0.6, 0.6], [10.5, 10.5, 10.5, 10.5, 10.5], [3.4, 3.4, 3.4, 3.4, 3.4], [-5.6, -5.6, -5.6, -5.6, -5.6]],
    [[3.5, 3.5, 3.5, 3.5, 3.5], [-6.0, -6.0, -6.0, -6.0, -6.0], [0.6, 0.6, 0.6, 0.6, 0.6], [10.5, 10.5, 10.5, 10.5, 10.5], [3.4, 3.4, 3.4, 3.4, 3.4], [-5.6, -5.6, -5.6, -5.6, -5.6]],
    [[3.5, 3.5, 3.5, 3.5, 3.5], [-6.0, -6.0, -6.0, -6.0, -6.0], [0.6, 0.6, 0.6, 0.6, 0.6], [10.5, 10.5, 10.5, 10.5, 10.5], [3.4, 3.4, 3.4, 3.4, 3.4], [-5.6, -5.6, -5.6, -5.6, -5.6]]
]
#Impresion de la  matriz1 3d  3x6x1  enteros
print("_____10.3.1 Arreglo1_3D_fl_3x6x5")
#arrelgo de tal manera que se vea de 3x6x1
for i in Arreglo1_3D_fl_3x6x5:
    for j in i:
        print(str(j).rjust(20), end="   ")
    print()
print()   
    
print()  # Nueva línea al final de cada dimensión en el eje x
#Impresion de la  matriz2 3d  5x5x5  enteros
print("_____10.3.2 Arreglo2_3D_fl_3x6x5:")
#arrelgo de tal manera que se vea de 5x5x5
for i in Arreglo2_3D_fl_3x6x5:
    for j in i:
        print(str(j).rjust(20), end="   ")
    print()
print()   
   

print("-----------------------------------------------------")
print("---11. Arreglos Tridimensionales con Texto ------")
print("-----------------------------------------------------")
print("___11.1. Arreglos 3D de 2x3x3 (texto) ____")
#Declaración Arreglo 1 de texto de 2x3x3
Arreglo1_3D_txt_2x3x3 = [
    [["a", "b", "c"], ["d", "f", "g"], ["h", "j", "ms"]],
    [["t", "l", "m"], ["n", "o", "u"], ["p", "q", "r"]]
    ]
#Declaración Arreglo 2 de texto de 2x3x3
Arreglo2_3D_txt_2x3x3 = [
    [["x", "y", "z"], ["w", "v", "u"], ["t", "s", "as"]],
    [["k", "l", "n"], ["m", "p", "q"], ["r", "s", "t"]]
]
#Impresion de la  matriz1 3d  2x3x3:  texto
print("_____11.1.1 Arreglo1_3D_txt_2x3x3:")
#arrelgo de tal manera que se vea de 2x3x3: texto
for i in Arreglo1_3D_txt_2x3x3:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   
#Impresion de la 3d matriz2 texto 2x3x3 de mejor manera
print("_____11.1.2 Arreglo1_3D_txt_2x3x3:")
#arrelgo de tal manera que se vea de 2x3x1
for i in Arreglo1_3D_txt_2x3x3:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   
    
print("___11.2. Arreglos 3D de 5x5x4 (texto) ____")
#Declaración Arreglo 1 de texto de 5x5x4 
Arreglo1_3D_txt_5x5x4 = [
    [["texto111", "texto112", "texto113", "texto114"], ["texto121", "texto122", "texto123", "texto124"], ["texto131", "texto132", "texto133", "texto134"], ["texto131", "texto132", "texto133", "texto134"],  ["texto151", "texto152", "texto153", "texto154"] ],
    [["texto111", "texto112", "texto113", "texto114"], ["texto121", "texto122", "texto123", "texto124"], ["texto131", "texto132", "texto133", "texto134"], ["texto131", "texto132", "texto133", "texto134"],  ["texto151", "texto152", "texto153", "texto154"] ],
    [["texto111", "texto112", "texto113", "texto114"], ["texto121", "texto122", "texto123", "texto124"], ["texto131", "texto132", "texto133", "texto134"], ["texto131", "texto132", "texto133", "texto134"],  ["texto151", "texto152", "texto153", "texto154"] ],
    [["texto111", "texto112", "texto113", "texto114"], ["texto121", "texto122", "texto123", "texto124"], ["texto131", "texto132", "texto133", "texto134"], ["texto131", "texto132", "texto133", "texto134"],  ["texto151", "texto152", "texto153", "texto154"] ],
    [["texto111", "texto112", "texto113", "texto114"], ["texto121", "texto122", "texto123", "texto124"], ["texto131", "texto132", "texto133", "texto134"], ["texto131", "texto132", "texto133", "texto134"],  ["texto151", "texto152", "texto153", "texto154"] ]
    
]

#Declaración Arreglo 2 de texto de 2x3x3
Arreglo2_3D_txt_5x5x4 =[
    [["pato111", "pato112", "pato113", "pato114"], ["pato121", "pato122", "pato123", "pato124"], ["pato131", "pato132", "pato133", "pato134"], ["pato131", "pato132", "pato133", "pato134"],  ["pato151", "pato152", "pato153", "pato154"] ],
    [["pato111", "pato112", "pato113", "pato114"], ["pato121", "pato122", "pato123", "pato124"], ["pato131", "pato132", "pato133", "pato134"], ["pato131", "pato132", "pato133", "pato134"],  ["pato151", "pato152", "pato153", "pato154"] ],
    [["pato111", "pato112", "pato113", "pato114"], ["pato121", "pato122", "pato123", "pato124"], ["pato131", "pato132", "pato133", "pato134"], ["pato131", "pato132", "pato133", "pato134"],  ["pato151", "pato152", "pato153", "pato154"] ],
    [["pato111", "pato112", "pato113", "pato114"], ["pato121", "pato122", "pato123", "pato124"], ["pato131", "pato132", "pato133", "pato134"], ["pato131", "pato132", "pato133", "pato134"],  ["pato151", "pato152", "pato153", "pato154"] ],
    [["pato111", "pato112", "pato113", "pato114"], ["pato121", "pato122", "pato123", "pato124"], ["pato131", "pato132", "pato133", "pato134"], ["pato131", "pato132", "pato133", "pato134"],  ["pato151", "pato152", "pato153", "pato154"] ]
    
    ]
#Impresion de la  matriz1 3d  5x5x4:  texto
print("_____11.2.1 Arreglo1_3D_txt_5x5x4:")
#arrelgo de tal manera que se vea de 5x5x4: texto

for i in Arreglo1_3D_txt_5x5x4:
    for j in i:
        print(str(j).rjust(20), end="   ")
    print()
print()   
print("_____11.2.2 Arreglo2_3D_txt_5x5x4:")
#arrelgo de tal manera que se vea de 5x5x4
for i in Arreglo2_3D_txt_5x5x4:
    for j in i:
        print(str(j).rjust(20), end="   ")
    print()
print()   


print("-----------------------------------------------------")
print("---12. Arreglos Tridimensionales con mixto int, txt, flo ------")
print("-----------------------------------------------------")
print("___12.1. Arreglos 3D de 2x3x2 (txt,int,float) ____")
#Declaración Arreglo 1 de mixto de 2x3x2
Arreglo1_3D_int_txt_fl_2x3x2 =  [
    [["pez", 1], [-1 , "pez"], ["pez", 4]],
    
    [[1, -20.29], ["pez", 4],   [-20.29, 7]]
]
#Declaración Arreglo 2 de mixto de 2x3x2
Arreglo2_3D_int_txt_fl_2x3x2=  [
    [["raton", 1], [-1 , "raton"], ["raton", 4]],
    
    [[1, 0.32923], ["raton", 4],   [0.32923, 7]]
]
#Impresion de la  matriz1 3d  2x3x2:  mixto
print("_____12.1.1 Arreglo1_3D_int_txt-fl_2x3x2:")
#arrelgo de tal manera que se vea de 2x3x2: mixto
for i in Arreglo1_3D_int_txt_fl_2x3x2:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   

#Impresion de la 3d matriz2 mixto 22x3x3 de mejor manera
print("_____12.1.2 Arreglo2_3D_int_txt-fl_2x3x2:")
#arrelgo de tal manera que se vea de 2x3x2
for i in Arreglo2_3D_int_txt_fl_2x3x2:
    for j in i:
        print(str(j).rjust(5), end="   ")
    print()
print()   

print("___12.2. Arreglos 3D de 5x5x1 (texto,int,float) ____")
#Declaración Arreglo 1 de texto de 5x5x1
Arreglo1_3D_int_tx_fl_5x5x1 = [
    [["tina"], [2], [-39.39], ["loop"], [3]],
    [["fox"], [2], [-39.39], ["apple"], [3]],
    [["pala"], [2], [-39.39], ["manzana"], [3]],
    [["ropa"], [2], [-39.39], ["America"], [3]],
    [["taladro"], [2], [-39.39], ["pentos"], [3]]
]


Arreglo2_3D_int_tx_fl_5x5x1 =[
    [["vela"], [-95], [--95.-959-959-95], ["l"], [3]],
    [["xoxo"], [-95], [--95.-959-959-95], ["abu"], [3]],
    [["protos"], [-95], [--95.-959-959-95], ["tulo"], [3]],
    [["cangrejo"], [-95], [--95.-959-959-95], ["Ecuador"], [3]],
    [["Quito"], [-95], [--95.-959-959-95], ["Piñas"], [3]]
]
    
  
#Impresion de la  matriz1 3d  5x5x1:  texto,int, float
print("_____13.2.1 Arreglo1_3D_int_tx_fl_5x5x1:")
#arrelgo de tal manera que se vea de 5x5x1: texto
for i in Arreglo1_3D_int_tx_fl_5x5x1:
    for j in i:
        print(str(j).rjust(13), end="   ")
    print()
print()   

#Impresion de la 3d matriz2 texto 22x3x3 de mejor manera
print("_____12.2.2 Arreglo1_3D_int_tx_fl_5x5x1:")
#arrelgo de tal manera que se vea de 5x5x1
for i in Arreglo2_3D_int_tx_fl_5x5x1:
    for j in i:
        print(str(j).rjust(13), end="   ")
    print()
print()   


print("___12.3. Arreglos 3D de 3x6x2 (texto,int,float) ____")
#Declaración Arreglo 1 de MIXTO de 3x6x2
Arreglo1_3D_int_tx_fl_3x6x2 = [
    [
        [-24, "casa"], [31.14, "sol"], [0, "snow"], [0.837, "vaca"], [38, "tata"], [-100, "BMW"]],
    [
        [-1, "bmw"], [-2.2, "toyota"], [2, "audi"], [2.837, "jav"], [4, "peugeot"], [-1, "kia"]],
    [
        [2, "haval"], [3, "susuki"], [5, "mazda"], [-93.3, "rnault"], [9, "hyundai"], [-3, "mitsubisi"]]
    ]



#Declaración Arreglo 2 de MIXTO de 3x6x2

Arreglo2_3D_int_tx_fl_3x6x2 = [
    [
        [-7, "Ford"], [54.14, "Chevrolet"], [110, "Honda"], [02.837, "Volkswagen"], [8, "Nissan"], [-100, "Tesla"]
    ],
    [
        [0, "Mercedes-Benz"], [-234.2, "Jeep"], [12, "Subaru"], [2.45, "Volvo"], [423, "Lexus"], [-31, "Fiat"]
    ],
    [
        [9, "Dodge"], [3, "Cadillac"], [215, "Chrysler"], [-3.3, "Land Rover"], [239, "hyundai"], [-233, "Ferrari"]
    ]
]

#Impresion de la  matriz1 3d  3x6x2:  texto,int, float
print("_____12.3.1 Arreglo1_3D_int_tx_fl_3x6x2:")
#arrelgo de tal manera que se vea de 3x6x2: texto
for i in Arreglo1_3D_int_tx_fl_3x6x2:
    for j in i:
        print(str(j).rjust(15), end="   ")
    print()
print()   

#Impresion de la 3d matriz2 mixto 3x6x2 de mejor manera
print("_____12.3.2 Arreglo1_3D_int_tx_fl_3x6x2:")
#arrelgo de tal manera que se vea de 5x5x1
for i in Arreglo1_3D_int_tx_fl_3x6x2:
    for j in i:
        print(str(j).rjust(15), end="   ")
    print()
print()   