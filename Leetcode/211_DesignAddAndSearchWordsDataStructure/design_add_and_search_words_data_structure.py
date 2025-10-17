class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['*'] = True  # Маркер конца слова

    def search(self, word: str) -> bool:
        return self._search_in_node(word, self.trie)

    def _search_in_node(self, word: str, node: dict) -> bool:
        for i, ch in enumerate(word):
            if ch == '.':
                # Для каждой возможной ветки проверяем остаток слова
                for next_ch in node:
                    if next_ch != '*' and self._search_in_node(word[i + 1:], node[next_ch]):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                node = node[ch]

        return '*' in node


class WordDictionary1:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for ch in word:
            next_nodes = []
            for node in nodes:
                if ch == '.':
                    for key in node:
                        if key != '#':
                            next_nodes.append(node[key])
                else:
                    if ch in node:
                        next_nodes.append(node[ch])
            if not next_nodes:
                return False
            nodes = next_nodes
        return any('#' in node for node in nodes)