# função para calcular o produto escalar de dois vetores
def produto_escalar(A, B):
    resultado = 0
    
    for i in range(len(A)):
        resultado += A[i] * B[i]
    
    return resultado

# exemplo
A = [1, 2, 3]
B = [1, 4, 2]

# exibindo o resultado
print(produto_escalar(A, B))