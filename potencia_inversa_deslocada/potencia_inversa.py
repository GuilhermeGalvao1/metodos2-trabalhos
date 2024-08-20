import numpy as np

def decompLU(A):
    U = np.copy(A).astype(float)
    n = np.shape(U)[0]
    L = np.eye(n, dtype=float)

    for j in np.arange(n-1):
        if U[j, j] == 0:
            raise ValueError("Zero pivot encountered. Consider pivoting or check the input matrix.")
        for i in np.arange(j+1, n):
            L[i, j] = U[i, j] / U[j, j]
            for k in np.arange(j+1, n):
                U[i, k] = U[i, k] - L[i, j] * U[j, k]
            U[i, j] = 0
    return L, U

def solverLU(L, U, b):
    # Resolve o sistema de equações lineares Ax = b usando decomposição LU
    # Primeiro resolve Ly = b
    y = np.linalg.solve(L, b)
    # Depois resolve Ux = y
    x = np.linalg.solve(U, y)
    return x

def normalizacao(v):
    # Normaliza o vetor v
    norm = np.linalg.norm(v)
    return v / norm

def Potencia_inversa(A, v1, epsilon):
    # Passo 1: Receber a matriz A, o vetor inicial v1, e a tolerância epsilon
    tam = len(v1)
    
    # Passo 2: Calcular a decomposição LU de A
    L, U = decompLU(A)
    
    # Passo 3: Inicializar o autovalor
    lambda_n = 0
    
    # Passo 4: Copiar o vetor v1 para v_old
    v_old = np.copy(v1)
    
    while True:
        # Passo 5: Copiar lambda_n para lambda_old
        lambda_old = lambda_n
        
        # Passo 6: Copiar v_old para v_older
        v_older = np.copy(v_old)
        
        # Passo 7: Normalizar v_older
        x = normalizacao(v_older)
        
        # Passo 8: Calcular v_old não normalizado
        v_old = solverLU(L, U, x)
        
        # Passo 9: Calcular a nova estimativa de lambda_n
        lambda_n = np.dot(x, v_old)
        
        # Passo 10: Verificar convergência de lambda_n
        if abs((lambda_n - lambda_old) / lambda_n) < epsilon:
            break
    
    # Passo 11: Calcular lambda
    lambda_final = 1 / lambda_n
    
    # Passo 12: Copiar x para o autovetor correspondente
    autovetor_final = x
    
    return lambda_final, autovetor_final