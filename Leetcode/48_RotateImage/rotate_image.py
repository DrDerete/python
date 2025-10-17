from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # первая идея посимвольно вращать грани в зависимости от глубины
        for deep in range(len(matrix) // 2):
            # просто тяжесть
            for edge in range(deep, len(matrix) - 1 - deep):
                # бытия
                mem1 = matrix[deep][edge]
                matrix[deep][edge] = matrix[-(edge + 1)][deep]
                mem2 = matrix[edge][-(deep + 1)]
                matrix[edge][-(deep + 1)] = mem1
                mem1, mem2 = mem2, matrix[-(deep + 1)][-(edge + 1)]
                matrix[-(deep + 1)][-(edge + 1)] = mem1
                matrix[-(edge + 1)][deep] = mem2

    # если поменять направление вращения, станет легче
    def rotate1(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for deep in range(n // 2):
            for edge in range(deep, n - 1 - deep):
                temp = matrix[deep][edge]
                # Верхний левый = нижний левый
                matrix[deep][edge] = matrix[n - 1 - edge][deep]
                # Нижний левый = нижний правый
                matrix[n - 1 - edge][deep] = matrix[n - 1 - deep][n - 1 - edge]
                # Нижний правый = верхний правый
                matrix[n - 1 - deep][n - 1 - edge] = matrix[edge][n - 1 - deep]
                # Верхний правый = сохраненный верхний левый
                matrix[edge][n - 1 - deep] = temp

    def rotate2(self, matrix: List[List[int]]) -> None:
        # тут меняем строки со столбцами [i][j] и [n-j][n-i]
        # получается первую строку с последней диагональю в обратном порядке
        for i in range(0, len(matrix) - 1):
            for j in range(0, len(matrix) - 1 - i):
                matrix[i][j], matrix[len(matrix) - 1 - j][len(matrix) - 1 - i] = (
                    matrix[len(matrix) - 1 - j][len(matrix) - 1 - i], matrix[i][j])
        # тадам, после прошлой операции осталось поменять местами 2 грани
        # делаем делаем делаем
        for i in range(0, (len(matrix) + 1) // 2):
            matrix[i], matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]

    def rotate3(self, matrix: List[List[int]]) -> None:
        # транспонируем и отражаем по вертикали
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()



if __name__ == '__main__':
    print(Solution().rotate3([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().rotate3([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
