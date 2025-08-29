import numpy as np

def calculate_priorities(matrix):
    # Нахождение собственных векторов и значений
    eigenvalues, eigenvectors = np.linalg.eig(matrix.T)

    # Максимальное собственное значение
    max_eigenvalue = np.max(eigenvalues)

    # Вектор приоритетов
    priorities = eigenvectors[:, np.argmax(eigenvalues)]

    # Нормализация вектора приоритетов
    priorities = priorities / np.sum(priorities)

    return priorities.real, max_eigenvalue.real

# Матрица S1
S1_matrix = np.array([
    [1, 3, 3],
    [1/3, 1, 1],
    [1/3, 1, 1]
])

# Матрица S1'
S1_transposed_matrix = np.array([
    [1, 1/3, 1/3],
    [3, 1, 1],
    [3, 1, 1]
])

# Вычисление приоритетов для S1
priorities_S1, max_eigenvalue_S1 = calculate_priorities(S1_matrix)

# Вычисление приоритетов для S1'
priorities_S1_transposed, max_eigenvalue_S1_transposed = calculate_priorities(S1_transposed_matrix)

print("Приоритеты для S1:", priorities_S1)
print("Максимальное собственное значение для S1:", max_eigenvalue_S1)

print("Приоритеты для S1':", priorities_S1_transposed)
print("Максимальное собственное значение для S1':", max_eigenvalue_S1_transposed)