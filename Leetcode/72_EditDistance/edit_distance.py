class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] - минимальное расстояние между word1[0:i] и word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Инициализация базовых случаев
        for i in range(m + 1):
            dp[i][0] = i  # удалить все символы из word1
        for j in range(n + 1):
            dp[0][j] = j  # вставить все символы в word2

        # Заполнение таблицы
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Символы совпадают - без операции
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Выбираем минимальную операцию:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # удаление из word1
                        dp[i][j - 1] + 1,  # вставка в word1
                        dp[i - 1][j - 1] + 1  # замена
                    )

        return dp[m][n]