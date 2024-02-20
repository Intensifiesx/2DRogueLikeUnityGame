import numpy as np

def optimized_complex_matrix_operation(matrix):
    """
    Perform a complex operation on a square matrix more efficiently.

    Args:
        matrix (np.array): A square numpy array representing the matrix.

    Returns:
        np.array: The result of the complex matrix operation.
    """
    determinant = np.linalg.det(matrix)
    # Compute the outer product of the matrix with itself and then add the determinant
    result = matrix @ matrix.T + determinant
    return result
