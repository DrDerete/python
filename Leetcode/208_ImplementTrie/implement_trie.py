class Node:
    def __init__(self, val="", children=None):
        self.val = val
        self.children = children if children is not None else {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        head = self.root
        for ch in word:
            if ch not in head.children:
                head.children[ch] = Node(head.val + ch)
            head = head.children[ch]
        head.is_end = True

    def search(self, word: str) -> bool:
        head = self.root
        for ch in word:
            if ch not in head.children:
                return False
            head = head.children[ch]
        return head.is_end

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for ch in prefix:
            if ch not in head.children:
                return False
            head = head.children[ch]
        return True

class Trie1:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    obj.search("app")
    obj.search("apple")
    obj.startsWith("app")
