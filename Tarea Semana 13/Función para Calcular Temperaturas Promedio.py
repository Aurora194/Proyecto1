# Función para calcular el promedio de temperaturas
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad a partir de los datos semanales proporcionados.

    Parámetros:
    temperaturas (list): Lista de listas donde cada sublista contiene las temperaturas semanales para una ciudad.

    Retorna:
    dict: Diccionario con el nombre de la ciudad como clave y la temperatura promedio como valor.
    """
    # Lista de nombres de ciudades
    ciudades = ["Ventanas", "Guayaquil", "Babahoyo"]
    promedios = {}

    # Iterar sobre cada ciudad
    for i, ciudad_temperaturas in enumerate(temperaturas):
        suma_total = 0
        conteo_total = 0

        for semana in ciudad_temperaturas:
            suma_total += sum(semana)
            conteo_total += len(semana)

        promedio = suma_total / conteo_total
        promedios[ciudades[i]] = promedio

    return promedios


# Temperaturas de 3 ciudades durante 4 semanas
# Cada sublista representa las temperaturas semanales de una ciudad
temperaturas_ciudades = [
    # Ventanas
    [
        [28, 30, 29, 31, 21, 26, 25],  # Semana 1
        [29, 28, 30, 32, 31, 29, 30],  # Semana 2
        [23, 18, 36, 30, 24, 20, 32],  # Semana 3
        [20, 27, 22, 31, 21, 25, 20]  # Semana 4
    ],
    # Guayaquil
    [
        [30, 32, 31, 33, 18, 29, 27],  # Semana 1
        [31, 30, 32, 34, 33, 31, 32],  # Semana 2
        [20, 26, 24, 31, 25, 30, 22],  # Semana 3
        [23, 19, 32, 30, 25, 25, 23]  # Semana 4
    ],
    # Babahoyo
    [
        [27, 29, 28, 30, 26, 25, 24],  # Semana 1
        [28, 27, 29, 31, 30, 28, 29],  # Semana 2
        [33, 24, 26, 30, 24, 30, 22],  # Semana 3
        [30, 28, 21, 33, 21, 25, 30]  # Semana 4
    ]
]

# Llamada a la función
promedios = calcular_temperatura_promedio(temperaturas_ciudades)

# Mostrar resultados
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f} °C")
