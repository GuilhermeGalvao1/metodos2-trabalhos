import numpy as np
import math

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

# Função para aplicar o filtro Sobel na direção x
def sobel_filter_x(matrix):
    filter = np.array([[-1, 0, 1], 
                       [-2, 0, 2], 
                       [-1, 0, 1]], dtype=float)
    result = np.zeros((matrix.shape[0] - 2, matrix.shape[1] - 2))

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            region = matrix[i:i+3, j:j+3]
            result[i, j] = np.sum(region * filter)
    
    return result

# Função para aplicar o filtro Sobel na direção y
def sobel_filter_y(matrix):
    filter = np.array([[-1, -2, -1], 
                       [0, 0, 0], 
                       [1, 2, 1]], dtype=float)
    result = np.zeros((matrix.shape[0] - 2, matrix.shape[1] - 2))

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            region = matrix[i:i+3, j:j+3]
            result[i, j] = np.sum(region * filter)
    
    return result

# Função para calcular a magnitude do gradiente
def sobel_magnitude(gx, gy):
    result = np.sqrt(gx**2 + gy**2)
    return result

# Função para aplicar o limiar e gerar a matriz final
def apply_threshold(matrix, threshold):
    result = np.zeros_like(matrix)
    result[matrix > threshold] = 255
    return result

# Função principal para detectar bordas
def edge_detection_sobel(matrix, threshold):
    result_gaussian = gaussian_filter(matrix)
    result_gx = sobel_filter_x(result_gaussian)
    result_gy = sobel_filter_y(result_gaussian)
    result_sobel = sobel_magnitude(result_gx, result_gy)
    final_result = apply_threshold(result_sobel, threshold)
    return final_result

# Exemplo de uso
if __name__ == "__main__":
    matrix = np.array([[3, 0, 1, 2, 7, 4], 
                       [1, 5, 8, 9, 3, 1], 
                       [2, 7, 2, 5, 1, 3],
                       [0, 1, 3, 1, 7, 8],
                       [4, 2, 1, 6, 2, 8],
                       [2, 4, 5, 2, 3, 9]], dtype=float)
    
    threshold = float(input("Enter the threshold: "))
    edges = edge_detection_sobel(matrix, threshold)

    print("Matrix after the Sobel edge detection:")
    print(edges)
