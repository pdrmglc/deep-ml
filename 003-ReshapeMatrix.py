# Reshape Matrix
# Write a Python function that reshapes a given matrix into a specified shape.

# %%

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    
    a_linear = [valor for linha in a for valor in linha] # Transforma a matriz em um vetor
    reshaped_matrix = [[0]*new_shape[1] for i in range(new_shape[0])] # Inicializa uma matriz de zeros com new_shape[0] linhas e new_shape[1] colunas

    c = 0
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            reshaped_matrix[i][j] = a_linear[c]
            c += 1

    return reshaped_matrix

# %%

# Test cases
a = [[1,2,3,4],[5,6,7,8]]
new_shape = (4, 2)

resultado = reshape_matrix(a, new_shape) # Resultado esperado: [[1, 2], [3, 4], [5, 6], [7, 8]]
print(resultado)