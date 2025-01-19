# Scalar Multiplication of a Matrix
# Write a Python function that multiplies a matrix by a scalar and returns the result.

# %%
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	
    n = len(matrix) # Número de linhas da matriz
    m = len(matrix[0]) # Número de colunas da matriz

    result = [[0]*n for i in range(m)] # Inicializa uma matriz de zeros com n linhas e m colunas

    for i in range(n):
        for j in range(m):
            result[i][j] = matrix[i][j]*scalar
    
    return result

# %%

matrix = [[1, 2], [3, 4]]
scalar = 2

resultado = scalar_multiply(matrix, scalar) # Resultado esperado: [[2, 4], [6, 8]]

print(resultado)