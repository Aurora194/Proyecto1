
# Escritura de Archivo de Texto
# Se crea un archivo llamado my_notes.txt
file = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando write()
file.write("Nota 1: Recoger la ropa del patio.\n")
file.write("Nota 2: Comprar ingredientes para el almuerzo.\n")
file.write("Nota 3: Llamar a mamá.\n")

# Cerramos el archivo después de escribir
file.close()

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt
file = open("my_notes.txt", "r")

# Leemos y mostramos cada línea utilizando readline()
line = file.readline()  # Leer la primera línea
while line:
    print(line.strip())  # Mostramos la línea sin saltos de línea extra
    line = file.readline()  # Leer la siguiente línea

# Cerramos el archivo después de leer
file.close()
