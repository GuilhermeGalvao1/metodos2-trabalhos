import numpy as np

def householder_transformation(A):
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
    R = H @ R

    # Passo 5: Acumular a transformação em Q
    Q = Q @ H.T

  return Q, R


# Exemplo de uso
A = np.array([[40, 4, 8, 2, 1], [8, 30, 12, 6, 2], [4, 12, 20, 1, 2],
              [2, 6, 1, 25, 4], [1, 2, 2, 4, 5]],
             dtype=float)
Q, R = householder_transformation(A)
print("Matriz Q:\n", Q)
print("Matriz R:\n", R)
