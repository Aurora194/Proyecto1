# Matriz 3x3
matriz = [
    [9, 1, 7],
    [8, 12, 2],
    [5, 3, 10]
]

print(matriz)

# Función que ordene una fila específica de la matriz
def ordenar_fila_en_matriz(matriz, fila):
    # Ordenar la fila especificada en orden ascendente
    matriz[fila].sort()
    return matriz

# Fila a ordenar (índice 1, que es la segunda fila)
fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila y mostrar la matriz resultante
matriz_ordenada = ordenar_fila_en_matriz(matriz, fila_a_ordenar)
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
