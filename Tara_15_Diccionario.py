#Diccionario
# Crear un Diccionario:

#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una
# persona, incluyendo al menos las claves
# "nombre", "edad", "ciudad" y "profesion".

informacion_personal = {
    "nombre": "Jose",
    "edad": 40,
    "ciudad": "Piñas",
    "sexo": "Masculino",
    "profesion": "Estudiante"
}
#1.1 Imprimir el diccionario final
print("Estes es el Diccionario Inicial:")
print(informacion_personal)
print()
# 2 Acceder y modificar valores
informacion_personal["ciudad"] = "Quito"  # Modificar la ciudad
informacion_personal["profesion"] = "Ingeniero_de_las_TIC"  # Agregar profesión

#3. # Verificar existencia de clave y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "593939152334"

#4 Eliminar una clave
if "sexo" in informacion_personal:
    del informacion_personal["sexo"]

#5 Imprimir el diccionario final
print("Estes es el Diccionario Completo:")
print(informacion_personal)
#5 Imprimir el clave eliminadad
if "sexo" in informacion_personal:
    print("La clave 'sexo' aún existe en el diccionario.")
else:
    print("\nLa clave 'sexo' ha sido eliminada del diccionario.")
    arr== [[[10, 20], [30, 40]],
           [[50, 60], [70, 80]]
           ]