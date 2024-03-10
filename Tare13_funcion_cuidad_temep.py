#Desarrollo de la Función:
#Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo.
#La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.
#Utiliza como base el ejemplo anterior, donde tenías datos de 3 ciudades durante 4 semanas.
#Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.

#Definir funcion de parametros de entrada ciudad, temperatura
def calcular_promedio_ciudad(ciudad, temperaturas):
    print(f"\nPromedio de temperaturas de la ciudad: {ciudad}")
    for i in range(1, len(temperaturas) + 1):
        semana = temperaturas[i - 1]
        promedio_semana = sum(dia['temp'] for dia in semana) / 7
        print(f" Temperatura Promedio de Semana {i}  : {promedio_semana:.2f}°C")


temperaturas = [
    [  # Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 1},
            {"day": "Domingo", "temp": 20}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 21}
        ]
    ],
    [  # Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [  # Piñas
        [  # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 25}
        ]
    ]
]
#
while True:
    print("\nPresentación de Temp Promedio  Semanal de cada Ciudad:")
    print("1. Quito")
    print("2. Guayaquil")
    print("3. Piñas ")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        print("Ha seleccionado la Opción Quito.")
        calcular_promedio_ciudad("Quito", temperaturas[opcion-1])
    elif opcion == 2:
        print("Ha seleccionado la Opción 2.")
        calcular_promedio_ciudad("Guayaquil", temperaturas[opcion-1])
    elif opcion == 3:
        print("Ha seleccionado la Opción 3.")
        calcular_promedio_ciudad("Piñas", temperaturas[opcion-1])
    elif opcion == 0:
        print("Muchas Gracias por usar el Sistema ...")
        break
    else:
        print("OPor favor, seleccione una opción correta.")
