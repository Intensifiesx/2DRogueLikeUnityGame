import numpy as np

def complex_matrix_operation(matrix):
    """
    Perform a complex operation on a square matrix.

    Args:
        matrix (np.array): A square numpy array representing the matrix.

    Returns:
        np.array: The result of the complex matrix operation.
    """
    n = matrix.shape[0]
    result = np.zeros_like(matrix)
    for i in range(n):
        for j in range(n):
            result[i, j] = sum(matrix[i, :] * matrix[:, j]) + np.linalg.det(matrix)
    return result
