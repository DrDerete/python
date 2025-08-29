from MatrixGause import decide


def scalar_product(v1, v2):
    return sum([v1[i]*v2[i] for i in range(len(v1))])


if __name__ == '__main__':
    data = [int(x) for x in input("Количество уравнений и переменных: ").split(" ")]
    matrix = [[int(x) for x in input(f"{i+1} строка ввода: ").split()] for i in range(data[0])]  # ввод считан
    matrix_t = [[matrix[row][col] for row in range(data[0])] for col in range(data[1]+1)]  # транспонировано
    scalars = [[scalar_product(matrix_t[i], matrix_t[j]) for j in range(len(matrix_t))] for i in range(len(matrix_t)-1)]  # все скалярные произведения из векторов
    decide(scalars)
