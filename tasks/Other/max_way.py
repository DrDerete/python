def find_max_reward_path(arr, rew):
    max_reward = 0
    best_path = []

    def dfs(current_node, visited, current_path, current_sum):
        nonlocal max_reward, best_path

        visited.add(current_node)
        current_path.append(current_node)
        current_sum += rew[current_node]

        # Если текущая сумма больше максимальной, обновляем результат
        if current_sum > max_reward:
            max_reward = current_sum
            best_path = current_path.copy()

        # Рекурсивно посещаем всех непосещённых соседей
        for neighbor in arr[current_node]:
            if neighbor not in visited:
                dfs(neighbor, visited, current_path, current_sum)

        # Возвращаемся назад (backtracking)
        visited.remove(current_node)
        current_path.pop()

    # Запускаем поиск из каждой вершины (если граф несвязный)
    for start_node in arr:
        dfs(start_node, set(), [], 0)

    return best_path, max_reward


if __name__ == '__main__':
    arr = {"00": {"10"}, "10": {"00", "20"}, "20": {"10", "21"}, "21": {"20", "22", "31"}, "31": {"21"},
           "22": {"21", "12"}, "12": {"02"}, "02": {"12"}}
    rew = {"00": 1, "10": 2, "20": 3, "21": 4, "31": 3, "22": 5, "12": 6, "02": 7}

    path, total_reward = find_max_reward_path(arr, rew)
    print("Лучший путь:", path)
    print("Сумма наград:", total_reward)
