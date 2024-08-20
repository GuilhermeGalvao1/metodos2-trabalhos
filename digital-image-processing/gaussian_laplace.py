import numpy as np

# Função para aplicar o filtro Gaussiano
def gaussian_filter(matrix):
    filter = np.array([[1, 2, 1], 
                       [2, 4, 2], 
                       [1, 2, 1]], dtype=float)
    filter /= np.sum(filter)  # Normalizar o filtro
    result = np.zeros((matrix.shape[0] - 2, matrix.shape[1] - 2))

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            region = matrix[i:i+3, j:j+3]
            result[i, j] = np.sum(region * filter)
    
    return result

# Função para aplicar o filtro Laplaciano
def laplace_filter(matrix):
    filter = np.array([[0, 1, 0], 
                       [1, -4, 1], 
                       [0, 1, 0]], dtype=float)
    result = np.zeros((matrix.shape[0] - 2, matrix.shape[1] - 2))

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            region = matrix[i:i+3, j:j+3]
            result[i, j] = np.sum(region * filter)
    
    return result

# Função para aplicar a tolerância e gerar a matriz final
def apply_tolerance(matrix, tolerance=0.0001):
    result = np.zeros_like(matrix)
    result[np.abs(matrix) > tolerance] = 255
    return result

# Função principal para detectar bordas
def edge_detection_laplace(matrix, tolerance=0.0001):
    result_gaussian = gaussian_filter(matrix)
    result_laplace = laplace_filter(result_gaussian)
    final_result = apply_tolerance(result_laplace, tolerance)
    return final_result

# Exemplo de uso
if __name__ == "__main__":
    matrix = np.array([[3, 0, 1, 2, 7, 4], 
                       [1, 5, 8, 9, 3, 1], 
                       [2, 7, 2, 5, 1, 3],
                       [0, 1, 3, 1, 7, 8],
                       [4, 2, 1, 6, 2, 8],
                       [2, 4, 5, 2, 3, 9]], dtype=float)
    
    edges = edge_detection_laplace(matrix)

    print("Matrix after the Laplace edge detection:")
    print(edges)
