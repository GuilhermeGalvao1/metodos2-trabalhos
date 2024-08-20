import numpy as np

def decomposicao_qr(A):
    """Realiza a decomposição QR usando ortogonalização de Gram-Schmidt."""
    n = A.shape[0]
    Q = np.zeros_like(A)
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    
    return Q, R

def metodo_qr(A, tol=1e-6, max_iteracoes=1000):
    """Calcula autovalores e autovetores usando o método QR."""
    n = A.shape[0]
    P = np.eye(n)
    A_k = A.copy()
    
    for iteracao in range(max_iteracoes):
        Q, R = decomposicao_qr(A_k)
        A_k = R @ Q  # A_k+1 = R * Q
        P = P @ Q  # Acumula as transformações ortogonais

        # Verifica convergência inspecionando os elementos fora da diagonal
        fora_diagonal = np.sqrt(np.sum(np.square(np.tril(A_k, -1))))
        if fora_diagonal < tol:
            break
        
        print(f"Iteração {iteracao + 1}, A_k =\n{A_k}\n")

    autovalores = np.diag(A_k)
    autovetores = P
    
    return autovalores, autovetores

# Matriz A fornecida
A = np.array([
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]
], dtype=float)

# Aplicando o método QR
autovalores, autovetores = metodo_qr(A)

print("Matriz diagonal A':")
print(np.diag(autovalores))
print("\nMatriz acumulada P:")
print(autovetores)
print("\nPares (autovalor, autovetor):")
for i in range(len(autovalores)):
    print(f"Autovalor: {autovalores[i]:.4f}, Autovetor: {autovetores[:, i]}")
