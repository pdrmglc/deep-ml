# Calculate Mean by Row or Column
# Write a Python function that calculates the mean of a matrix either by
# row or by column, based on a given mode.
# The function should take a matrix (list of lists) and a mode ('row' or 'column')
# as input and return a list of means according to the specified mode.

# %%

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
    if mode not in ["row", "column"]:
        return -1

    n = len(matrix) # Número de linhas da matriz
    m = len(matrix[0]) # Número de colunas da matriz
    
    means = []

    for i in range(n):
        tmp_valor = 0
        for j in range(m):
            if mode == "column":
                tmp_valor += matrix[j][i]
            elif mode == "row":
                tmp_valor += matrix[i][j]
        if mode == "column":
            mean = tmp_valor/m
        else:
            mean = tmp_valor/n
        means.append(mean)

    return means

# %%

# Test cases

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'

resultado = calculate_matrix_mean(matrix, mode) # Resultado esperado: [4.0, 5.0, 6.0]

print(resultado)
