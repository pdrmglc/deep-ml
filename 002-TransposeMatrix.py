# Transpose of a Matrix
# Write a Python function that computes the transpose of a given matrix.
# %%
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n = len(a) # Número de linhas da matriz
    m = len(a[0]) # Número de colunas da matriz

    b = [[0]*n for i in range(m)] # Inicializa uma matriz de zeros com m linhas e n colunas

    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    return b

# %%
# Test cases
a = [[1,2,3],[4,5,6]]

resultado = transpose_matrix(a) # Resultado esperado: [[1, 4], [2, 5], [3, 6]]

print(resultado)