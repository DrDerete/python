from math import prod


def find_determinant(matr):
    perm = 0  # учет четности для детерминанта
    for i in range(len(matr)):
        if matr[i][i] == 0:  # если ноль меняем на не ноль
            for j in range(i+1, len(matr[i])):
                if matr[j][i] != 0:
                    perm += 1
                    matr[i], matr[j] = matr[j], matr[i]
                    break
                if j == len(matr[i])-1:  # если столбец нулей, возвращаем 0
                    return 0
        for j in range(i+1, len(matr)):  # создание ступенчатой матрицы
            if matr[j][i] != 0:
                matr[j] = [matr[j][k]-matr[j][i]/matr[i][i]*matr[i][k] for k in range(len(matr[j]))]
            else:
                continue
    diagonal = [matr[i][i] for i in range(len(matr))]  # диагональ матрицы
    parity = 1 if perm % 2 == 0 else -1  # знак детерминанта
    return prod(diagonal)*parity  # детерминант


if __name__ == '__main__':
    n = int(input())
    matrix = [[int(x) for x in input().split()] for i in range(n)]  # ввод
    print(round(find_determinant(matrix)))  # вывод округленного детерминанта
