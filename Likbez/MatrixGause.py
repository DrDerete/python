def decide(mat):
    mat = triangular_matrix(mat)
    if mat is None:
        return
    solve_matrix(mat)


def triangular_matrix(mat):
    triangle = min(len(mat), len(mat[0])-1)
    for i in range(triangle):
        if mat[i][i] == 0:  # проверяем на 0 и меняем строки, если 0
            row = mat[i]
            for k in range(i + 1, len(mat)):
                if mat[k][i] != 0:
                    mat[i] = mat[k]
                    mat[k] = row
                    break
            if mat[i] == row:
                continue
        for j in range(i+1, len(mat)):  # приводим к ступенчатому виду
            multi = mat[j][i] / mat[i][i]
            new_row = [mat[j][k] - multi * mat[i][k] for k in range(len(mat[i]))]
            if all(0.00001 > new_row[i] > -0.00001 for i in range(len(new_row) - 1)) and new_row[len(new_row) - 1] != 0.0:
                print("NO")  # система несовместна
                return None  # сразу обрабатываем исключение
            mat[j] = new_row
    mat = [mat[i] for i in range(len(mat)) if not all(mat[i][j] == 0.0 for j in range(len(mat[i])-1))]  # удаление нулевых строк
    if len(mat) < len(mat[0]) - 1:  # вывод по получившейся матрице
        print("INF")  # система неопределенна
        return None
    else:
        print("YES")  # система определенна
        return mat


def solve_matrix(mat):  # находим корни
    roots = []
    for i in range(len(mat) - 1, -1, -1):
        if not i == 0:
            for j in range(i):
                multi = mat[j][i] / mat[i][i]
                new_row = [mat[j][k] - multi * mat[i][k] for k in range(len(mat[i]))]
                mat[j] = new_row
            roots.append(mat[i][len(mat[i])-1] / mat[i][i])
        else:
            roots.append(mat[i][len(mat[i])-1] / mat[i][i])
    print(" ".join(str(x) for x in reversed(roots)))


if __name__ == '__main__':
    inp = input("Количество уравнений и переменных: ").split()

    eqs = int(inp[0])
    vars = int(inp[1])
    matrix = [list(map(int, input(f"{i + 1} строка матрицы: ").split(" "))) for i in range(eqs)]

    decide(matrix)
