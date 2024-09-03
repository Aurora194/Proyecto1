# Crear la matriz 3D de temperaturas (Ciudades x Semanas x Días)
# Ciudades: Ventanas, Guayaquil, Babahoyo
# Semanas: 2
# Días: 7 (Lunes a Domingo)

# Datos de temperaturas:
temperaturas = [
    # Ventanas
    [
        [28, 30, 29, 31, 27, 26, 25],  # Semana 1
        [29, 28, 30, 32, 31, 29, 30]   # Semana 2
    ],
    # Guayaquil
    [
        [30, 32, 31, 33, 29, 28, 27],  # Semana 1
        [31, 30, 32, 34, 33, 31, 32]   # Semana 2
    ],
    # Babahoyo
    [
        [27, 29, 28, 30, 26, 25, 24],  # Semana 1
        [28, 27, 29, 31, 30, 28, 29]   # Semana 2
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

