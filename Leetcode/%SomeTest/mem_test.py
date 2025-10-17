import tracemalloc

# тест памяти по заданию 108
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def build_tree(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])

        node.left = build_tree(left, mid - 1)
        node.right = build_tree(mid + 1, right)

        return node

    return build_tree(0, len(nums) - 1)

def sortedArrayToBST1(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left=sortedArrayToBST(nums[:mid])
    root.right=sortedArrayToBST(nums[mid+1:])
    return root

def test_108():
    nums = list(range(1000))

    # Тест версии с индексами
    tracemalloc.start()
    root1 = sortedArrayToBST(nums)
    current1, peak1 = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Тест версии со срезами
    tracemalloc.start()
    root2 = sortedArrayToBST1(nums)
    current2, peak2 = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Срезы: {peak1 / 1024:.1f} KB")
    print(f"Индексы: {peak2 / 1024:.1f} KB")

if __name__ == '__main__':
    test_108()