import importlib.util
import sys, os
import timeit
import random


def test_88():
    # динамический импорт модуля
    package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '88_MergeSortedArray'))
    sys.path.append(os.path.dirname(package_path))

    spec = importlib.util.spec_from_file_location(
        "merge_sorted_array",
        os.path.join(package_path, 'merge_sorted.py')
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    solution = module.Solution()

    # Генерация тестовых данных
    def generate_test_case(size_m, size_n):
        arr1 = sorted([random.randint(0, 1000) for _ in range(size_m)]) + [0] * size_n
        arr2 = sorted([random.randint(0, 1000) for _ in range(size_n)])
        return arr1, size_m, arr2, size_n

    test_cases = [
        (10, 10),
        (100, 100),
        (1000, 1000),
        (10000, 10000)
    ]

    for m, n in test_cases:
        def test_merge_sort():
            merged_arr = nums1[:m_val] + nums2[:n_val]
            solution.split_sort(merged_arr)

        def test_merge():
            nums1_copy = nums1.copy()
            nums2_copy = nums2.copy()
            solution.merge(nums1_copy, m_val, nums2_copy, n_val)

        nums1, m_val, nums2, n_val = generate_test_case(m, n)

        time_merge = timeit.timeit(test_merge, number=1)
        time_merge_sort = timeit.timeit(test_merge_sort, number=1)

        print(f"m={m}, n={n}:")
        print(f"  Сортировка слиянием: {time_merge_sort:.5f} сек")
        print(f"  Слияние сортированных массивов: {time_merge:.5f} сек")
        print(f"  Ускорение: {time_merge_sort / time_merge:.2f}x")
        print()


if __name__ == '__main__':
    test_88()
