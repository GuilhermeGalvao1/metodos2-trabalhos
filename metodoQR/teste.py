import numpy as np

def transformacao_householder(A):
    m, n = A.shape
    Q = np.eye(m)  # Matriz identidade de dimensão m
    R = A.copy()  # Inicialmente, R é uma cópia de A

    for k in range(n):
        # Passo 1: Selecionar o vetor x a partir da coluna k de R
        x = R[k:m, k]

        # Passo 2: Calcular o vetor de Householder v
        e1 = np.zeros_like(x)
        e1[0] = 1
        v = x + np.sign(x[0]) * np.linalg.norm(x) * e1
        v = v / np.linalg.norm(v)

        # Passo 3: Construir a matriz de Householder H_k
        H_k = np.eye(m - k) - 2 * np.outer(v, v)
        H = np.eye(m)
        H[k:m, k:m] = H_k

        # Passo 4: Aplicar a transformação H a R
        R = H @ R @ H
        # Passo 5: Acumular a transformação em Q
        Q = Q @ H

    return R, Q

def decomposicao_qr(A, tol=1e-10, max_iter=1000):
    n = A.shape[0]
    Q_total = np.eye(n)
    A_nova = A.copy()

    for it in range(max_iter):
        # Decomposição QR usando numpy
        Q, R = np.linalg.qr(A_nova)
        A_nova = R @ Q
        Q_total = Q_total @ Q

        # Verifica se a matriz está praticamente diagonal
        if np.allclose(A_nova - np.diag(np.diagonal(A_nova)), np.zeros_like(A_nova), atol=tol):
            break

    autovalores = np.diag(A_nova)
    return Q_total, autovalores, A_nova

def main():
    A = np.array([[40, 8, 4, 2, 1],
                  [8, 30, 12, 6, 2],
                  [4, 12, 20, 1, 2],
                  [2, 6, 1, 25, 4],
                  [1, 2, 2, 4, 5]], dtype=float)
    
    # Transformação de Householder para matriz tridiagonal
    MatrizT, MatrizH = transformacao_householder(A)

    print("Matriz T")
    print(MatrizT)
    print("\n")

    print("Matriz H")
    print(MatrizH)
    print("\n")

    # Método QR para encontrar autovalores e autovetores
    P_barra, lamb, A_nova = decomposicao_qr(MatrizT, 1e-7)

    print("Matriz P antes de P = H*P_barra\n")
    print(P_barra)
    print("\n")

    P = MatrizH.dot(P_barra)

    print("Matriz P depois de P = H*P_barra\n")
    print(P)
    print("\n")

    P = np.transpose(P)
    print("Pares autovalor-autovetor\n")
    for i in range(len(lamb)):
        print("{} -> {}".format(lamb[i], P[i]))

main()
