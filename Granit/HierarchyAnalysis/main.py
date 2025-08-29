import numpy as np

# Функция для вычисления нормализованного вектора приоритетов и максимального собственного числа
def calculate_priorities(matrix):
    # нахождение собственных векторов и значений
    eigenvalues, eigenvectors = np.linalg.eig(matrix.T)
    # максимальное собственное значение
    max_eigenvalue = np.max(eigenvalues)
    # вектор приоритетов
    priorities = eigenvectors[:, np.argmax(eigenvalues)]
    # нормализация вектора
    priorities = priorities / np.sum(priorities)
    return priorities.real, max_eigenvalue.real

# Функция для вычисления индекса и отношения согласованности
def calculate_consistency(lambda_max, n):
    CI = (lambda_max - n) / (n - 1)
    RI = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    CR = CI / RI[n]
    return CI, CR

def extend_vector(vector, zero_positions):

    # Создаем новый вектор длиной 5, заполненный нулями
    extended_vector = np.zeros(5)

    # Копируем элементы исходного вектора в новый вектор, пропуская указанные позиции
    current_index = 0
    for i in range(5):
        if i in zero_positions:
            extended_vector[i] = 0
        else:
            extended_vector[i] = vector[current_index]
            current_index += 1

    return extended_vector

# Матрицы парных сравнений для заинтересованных лиц
#     'B', 'Производительность'
#     'C', 'Удобство использования'
#     'D', 'Сообщество и поддержка'
#     'E', 'Масштабируемость'
#     'F', 'Безопасность'

# Для разработчика матрица это B, C, D с соотв. значениями
S1_matrix = np.array([
    [1, 3, 3],
    [1/3, 1, 1],
    [1/3, 1, 1]
])

# Для менеджера матрица это D, E, F с соотв. значениями
S2_matrix = np.array([
    [1, 5, 3],
    [1/5, 1, 3/5],
    [1/3, 5/3, 1]
])

# Для иследователя матрица это B, D, E, F с соотв. значениями
S3_matrix = np.array([
    [1, 1/2, 1/3, 3],
    [2, 1, 2/3, 6],
    [3, 3/2, 1, 9],
    [1/3, 1/6, 1/9, 1]
])

# Вычисление приоритетов и показателей согласованности для заинтересованных лиц
S1_priorities, S1_lambda_max = calculate_priorities(S1_matrix)
S1_CI, S1_CR = calculate_consistency(S1_lambda_max, S1_matrix.shape[0])

S2_priorities, S2_lambda_max = calculate_priorities(S2_matrix)
S2_CI, S2_CR = calculate_consistency(S2_lambda_max, S2_matrix.shape[0])

S3_priorities, S3_lambda_max = calculate_priorities(S3_matrix)
S3_CI, S3_CR = calculate_consistency(S3_lambda_max, S3_matrix.shape[0])

# Веса заинтересованных лиц
weights = np.array([0.4, 0.3, 0.3])

# Локальные приоритеты
local_priorities = np.array([
    extend_vector(S1_priorities, [3, 4]),
    extend_vector(S2_priorities, [0, 1]),
    extend_vector(S3_priorities, [2])
])

# Вычисление глобальных приоритетов
global_priorities = np.dot(weights, local_priorities)
# B, C, D для разработчика
# E, F, D для менеджера
# B, E, C для исследователя

# Показатели согласованности для всех уровней
CR_values = [S1_CR, S2_CR, S3_CR]

# Вычисление общей согласованности иерархии
overall_CR = np.mean(CR_values)

# Матрицы парных сравнений для альтернатив 1. TensorFlow 2. PyTorch 3. Keras 4. Scikit-learn
# Производительность
B_matrix = np.array([
    [1, 2, 1/2, 3],
    [1/2, 1, 1/4, 3/2],
    [2, 4, 1, 6],
    [1/3, 2/3, 1/6, 1]
])
# Удобство использования
C_matrix = np.array([
    [1, 3, 1/2, 4],
    [1/3, 1, 1/6, 4/3],
    [2, 6, 1, 8],
    [1/4, 3/4, 1/8, 1]
])
# Сообщество и поддержка
D_matrix = np.array([
    [1, 3, 1/2, 1/3],
    [1/3, 1, 1/6, 1/9],
    [2, 6, 1, 2/3],
    [3, 9, 3/2, 1]
])
# Масштабируемость
E_matrix = np.array([
    [1, 1, 1/2, 1/4],
    [1, 1, 1/2, 1/4],
    [2, 2, 1, 1/2],
    [4, 4, 2, 1]
])
# Безопасность
F_matrix = np.array([
    [1, 1/2, 1/4, 1/6],
    [2, 1, 1/2, 1/3],
    [4, 2, 1, 2/3],
    [6, 3, 3/2, 1]
])

# Вычисление приоритетов альтернатив для каждого критерия
B_priorities, _ = calculate_priorities(B_matrix)
C_priorities, _ = calculate_priorities(C_matrix)
D_priorities, _ = calculate_priorities(D_matrix)
E_priorities, _ = calculate_priorities(E_matrix)
F_priorities, _ = calculate_priorities(F_matrix)

# Приоритеты альтернатив для каждого критерия
alternative_priorities = np.array([
    B_priorities,
    C_priorities,
    D_priorities,
    E_priorities,
    F_priorities
])

# Вычисление общих приоритетов альтернатив относительно главной цели
overall_alternative_priorities = np.dot(global_priorities, alternative_priorities)

if __name__ == '__main__':
    # Вывод результатов
    print("Приоритеты для разработчика [B, C, D]:", S1_priorities)
    print("Макс. собс. число: ", S1_lambda_max)
    print("CI для разработчика:", S1_CI)
    print("CR для разработчика:", S1_CR, "\n")

    print("Приоритеты для менеджера [D, E, F]:", S2_priorities)
    print("Макс. собс. число: ", S2_lambda_max)
    print("CI для менеджера:", S2_CI)
    print("CR для менеджера:", S2_CR, "\n")

    print("Приоритеты для исследователя [B, D, E, F]:", S3_priorities)
    print("Макс. собс. число: ", S3_lambda_max)
    print("CI для исследователя:", S3_CI)
    print("CR для исследователя:", S3_CR, "\n")

    print("Глобальные приоритеты:", global_priorities, "\n")

    # Вывод приоритетов альтернатив для каждого критерия
    print("Приоритеты альтернатив для критерия B:", B_priorities)
    print("Приоритеты альтернатив для критерия C:", C_priorities)
    print("Приоритеты альтернатив для критерия D:", D_priorities)
    print("Приоритеты альтернатив для критерия E:", E_priorities)
    print("Приоритеты альтернатив для критерия F:", F_priorities, "\n")

    print("Общая согласованность иерархии:", overall_CR, "\n")

    # Вывод общих приоритетов альтернатив относительно главной цели
    print("Альтернативы: 1. TensorFlow 2. PyTorch 3. Keras 4. Scikit-learn")
    print("Общие приоритеты альтернатив относительно главной цели:", overall_alternative_priorities)
