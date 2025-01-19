# Matrix times Vector
# Write a Python function that takes the dot product of a matrix and a vector.
# return -1 if the matrix could not be dotted with the vector
# %%
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    n = len(a) # Número de linhas da matriz
    m = len(a[0]) # Número de colunas da matriz
    if m != len(b): # Se o número de colunas da matriz for diferente do número de elementos do vetor, não podemos multiplicar
        return -1
    c = [0]*n
    for i in range(n):
        for j in range(m):
            c[i] += a[i][j]*b[j]
    return c


# %%

# Test cases
resultado = matrix_dot_vector([[1,2],[2,4]],[1,2]) # Resultado esperado: [5, 10]

print(resultado)