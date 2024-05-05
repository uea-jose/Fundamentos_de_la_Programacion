# Datos de temperatura
temperaturas = [28, 29, 28, 30, 32, 31, 30, 29, 31, 32, 31, 31, 30, 31, 32, 32, 34, 33, 32, 34]

# Calcular frecuencia absoluta
frecuencia_absoluta = {}
for temp in temperaturas:
    frecuencia_absoluta[temp] = frecuencia_absoluta.get(temp, 0) + 1

# Calcular frecuencia relativa
total_temperaturas = len(temperaturas)
frecuencia_relativa = {temp: freq / total_temperaturas for temp, freq in frecuencia_absoluta.items()}

# Calcular frecuencia acumulada y relativa acumulada
frecuencia_acumulada = {}
frecuencia_relativa_acumulada = {}
acumulado_absoluto = 0
acumulado_relativo = 0
for temp, freq in sorted(frecuencia_absoluta.items()):
    acumulado_absoluto += freq
    acumulado_relativo += frecuencia_relativa[temp]
    frecuencia_acumulada[temp] = acumulado_absoluto
    frecuencia_relativa_acumulada[temp] = acumulado_relativo

# Mostrar los datos en una tabla de 5 columnas
print("{:<12} {:<20} {:<20} {:<20} {:<20}".format("Temperatura", "Frecuencia Absoluta", "Frecuencia Relativa", "Frecuencia Acumulada", "Frecuencia Relativa Acumulada"))
for temp in sorted(frecuencia_absoluta.keys()):
    print("{:<12} {:<20} {:<20} {:<20} {:<20}".format(temp, frecuencia_absoluta[temp], frecuencia_relativa[temp], frecuencia_acumulada[temp], frecuencia_relativa_acumulada[temp]))
