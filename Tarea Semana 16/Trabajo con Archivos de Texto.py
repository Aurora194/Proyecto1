
# Escritura de Archivo de Texto
# Se crea un archivo llamado my_notes.txt
archi = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando write()
archi.write("Nota 1: Recoger la ropa del patio.\n")
archi.write("Nota 2: Comprar ingredientes para el almuerzo.\n")
archi.write("Nota 3: Llamar a mamá.\n")

# Cerramos el archivo después de escribir
archi.close()

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt
archi = open("my_notes.txt", "r")

# Leemos y mostramos cada línea utilizando readline()
Archivo = archi.readline()  # Leer la primera línea
while Archivo:
    print(Archivo.strip())  # Mostramos la línea sin saltos de línea extra
    Archivo = archi.readline()  # Leer la siguiente línea

# Cerramos el archivo después de leer
archi.close()
