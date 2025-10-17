from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # аналогично прошлому - каждый шаг это + мутация, мутируем по 1 гену строго
        if endGene not in bank:
            return -1
        bank_set = set(bank)
        visited = set()
        queue = deque([(startGene, 0)])
        while queue:
            current, steps = queue.popleft()
            if current == endGene:
                return steps
            # Проверяем все гены в банке, достижимые за 1 мутацию
            for gene in bank_set:
                if gene not in visited:
                    # Считаем различия
                    diff_count = sum(1 for a, b in zip(current, gene) if a != b)
                    if diff_count == 1:  # Ровно одна мутация
                        visited.add(gene)
                        queue.append((gene, steps + 1))
        return -1

    def minMutation1(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([(startGene, 0)])
        # а тут идея от обратного, берем слово
        # и всеми способами мутируем его
        # поскольку проверяем через банк, то либо доходим до конечного варианта либо нет
        visited = {startGene}
        characters = ['A','C','G','T']
        while q:
            node, distance = q.popleft()
            if node == endGene:
                return distance
            for i in range(8):
                for character in characters:
                    if node[i] == character:
                        continue
                    mutation = node[:i] + character + node[i+1:]
                    if mutation not in visited and mutation in bank:
                        visited.add(mutation)
                        q.append((mutation, distance+1))
        return -1

if __name__ == '__main__':
    Solution().minMutation1("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"])
    Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
    Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
