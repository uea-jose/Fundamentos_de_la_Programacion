 #Crear una función para convertir grados centigrados a Farhrenheit, a grados kelvin
# Fahrenheit = (grados_cel)(9/5) +32
# Kelvin = grados_cel + 273.15

#Definir función conversion
def conversion_f_k(grad_celsius):
    fahrenheit = (grad_celsius * 9/5) + 32
    kelvin = grad_celsius + 273.15
    return fahrenheit, kelvin


#llamo a la función

grados_celcius = int(input("\nIngrese la temperatura en Celsius: "))

fahrenheit, kelvin= conversion_f_k(grados_celcius)

print(f"\nTemperaturas  en grados celcius: {grados_celcius}°C")
print(f"En Grados Kelvin: {kelvin}°K")
print(f"En Grados Fahrenheit: {fahrenheit} °F")