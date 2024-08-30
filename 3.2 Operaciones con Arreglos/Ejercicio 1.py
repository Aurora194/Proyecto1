# Matriz 3x3
matriz = [
    [5, 8, 2],
    [1, 7, 3],
    [9, 4, 6]
]

print(matriz)

#Función que realice una búsqueda en la matriz de un valor específico
def buscar_valor_en_matriz(matriz, valor_a_buscar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                return f"Valor encontrado en la posición ({i}, {j})"
    return "Valor no encontrado en la matriz"


# Valor a buscar
valor = 4

# Llamar a la función y mostrar el resultado
resultado = buscar_valor_en_matriz(matriz, valor)
print(resultado)
