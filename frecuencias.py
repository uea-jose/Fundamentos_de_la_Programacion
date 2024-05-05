import pandas as pd

# Datos de temperatura
temperaturas = [28, 29, 28, 30, 32, 31, 30, 29, 31, 32, 31, 31, 30, 31, 32, 32, 34, 33, 32, 34]

# Crear un DataFrame de pandas
df = pd.DataFrame(temperaturas, columns=['Temperatura'])

# Calcular frecuencia absoluta
frecuencia_absoluta = df['Temperatura'].value_counts().sort_index()

# Calcular frecuencia relativa
frecuencia_relativa = df['Temperatura'].value_counts(normalize=True).sort_index()

# Calcular frecuencia acumulada
frecuencia_acumulada = frecuencia_absoluta.cumsum()

# Calcular frecuencia relativa acumulada
frecuencia_relativa_acumulada = frecuencia_relativa.cumsum()

# Crear DataFrame con los resultados
resultado = pd.DataFrame({
    'Temperatura': frecuencia_absoluta.index,
    'Frecuencia Absoluta': frecuencia_absoluta.values,
    'Frecuencia Relativa': frecuencia_relativa.values,
    'Frecuencia Acumulada': frecuencia_acumulada.values,
    'Frecuencia Relativa Acumulada': frecuencia_relativa_acumulada.values
})

# Guardar en un archivo Excel
resultado.to_excel('resultado_estadisticas_temperatura.xlsx', index=False)

# Organizar los datos en la matriz
for temperatura in sorted(frecuencia_absoluta.index):
    fa = frecuencia_absoluta[temperatura]
    fr = frecuencia_relativa[temperatura]
    fac = frecuencia_acumulada[temperatura]
    fra = frecuencia_relativa_acumulada[temperatura]
    resultados.append([temperatura, fa, fr, fac, fra])

# Mostrar la matriz en pantalla
print("Temperatura".center(20), "Frecuencia Absoluta".center(20), "Frecuencia Relativa".center(20), "Frecuencia Acumulada".center(20), "Frecuencia Relativa Acumulada".center(30), sep='\t')
for resultado in resultados:
    print("\t".join(map(str, resultado)).center(20))
