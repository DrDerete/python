from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # идея - массив индексов для сборки комбинации
        # каждую итерацию записываем слово и меняем индексы
        if not digits:
            return []
        dig_to_let = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        indices = [0] * len(digits)
        while True:
            combination = []
            for i in range(len(digits)):
                letters = dig_to_let[digits[i]]
                combination.append(letters[indices[i]])
            ans.append("".join(combination))
            i = len(digits) - 1
            while i >= 0:
                letters = dig_to_let[digits[i]]
                indices[i] += 1
                # если буква есть break, чтобы записать
                if indices[i] < len(letters):
                    break
                # в противном случае переходим в следующий разряд с обнулением текущего
                indices[i] = 0
                i -= 1
            if i < 0:
                break
        return ans

    def letterCombinations1(self, digits: str) -> List[str]:
        # базированная рекурсия
        if not digits:
            return []
        dig_to_let = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index, current):
            # записываем в ответ, когда слово заполнилось
            if index == len(digits):
                ans.append("".join(current))
                return
            letters = dig_to_let[digits[index]]
            for letter in letters:
                # записываем букву и переходим к следующему разряду
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()
        ans = []
        backtrack(0, [])
        return ans

    def letterCombinations2(self, digits: str) -> List[str]:
        # okak
        if not digits: return []
        mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        # комбинационное решение - каждая буква с каждой следующей образует новую комбинацию
        result = [""]
        for digit in digits:
            new_result = []
            for comb in result:
                for letter in mapping[digit]:
                    new_result.append(comb + letter)
            result = new_result
        # и сразу получаем ответ
        return result

if __name__ == '__main__':
    Solution().letterCombinations2("238")

