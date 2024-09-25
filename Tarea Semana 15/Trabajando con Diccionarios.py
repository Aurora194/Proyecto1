# Creación del diccionario con información personal
informacion_personal = {
    "Nombre": "Briggitte Lorenti",
    "Edad": 20,
    "Ciudad": "Guayaquil",
    "Profesion": "Enfermera"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Ventanas"

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["Profesion"] = "Periodista"

# Verificar existencia de la clave "telefono"
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0928542843"  # Agregar número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

# Imprimir el diccionario final
print(informacion_personal)
