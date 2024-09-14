# Crear la matriz 3D de temperaturas (Ciudades x Semanas x Días)
# Ciudades: Ventanas, Guayaquil, Babahoyo
# Semanas: 4
# Días: 7 (Lunes a Domingo)

# Datos de temperaturas:
temperaturas = [
    # Ventanas
    [
        [28, 30, 29, 31, 27, 26, 25],  # Semana 1
        [29, 28, 30, 32, 31, 29, 30]   # Semana 2
        [23, 18, 36, 30, 24, 20, 32],  # Semana 3
        [20, 27, 22, 31, 21, 25, 20]  # Semana 4
    ],
    # Guayaquil
    [
        [30, 32, 31, 33, 29, 28, 27],  # Semana 1
        [31, 30, 32, 34, 33, 31, 32]   # Semana 2
        [20, 26, 24, 31, 25, 30, 22],  # Semana 3
        [23, 19, 32, 30, 25, 25, 23]  # Semana 4
    ],
    # Babahoyo
    [
        [27, 29, 28, 30, 26, 25, 24],  # Semana 1
        [28, 27, 29, 31, 30, 28, 29]   # Semana 2
        [33, 24, 26, 30, 24, 30, 22],  # Semana 3
        [30, 28, 21, 33, 21, 25, 30]  # Semana 4
    ]
]

# Lista de nombres de ciudades
ciudades = ["Ventanas", "Guayaquil", "Babahoyo"]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad_3d, ciudad in enumerate(temperaturas):
    print(f"Promedios de temperaturas para {ciudades[ciudad_3d]}:")
    for semana_d, semana in enumerate(ciudad):
        promedio_semana = sum(semana) / len(semana)
        print(f"  Semana {semana_d + 1}: {promedio_semana:.2f}°C")
    print()  # Línea en blanco para separar la salida de cada ciudad

