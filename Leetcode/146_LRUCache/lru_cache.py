from collections import OrderedDict


class Node:
    def __init__(self, val=-1, key=None, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:
    # LRU через linked list и dict для адресации(на родителя) по key
    def __init__(self, capacity: int):
        self.space = capacity
        self.cash = Node()
        self.c_head = self.cash
        self.key_to_adr = {}

    def get(self, key: int) -> int:
        if key in self.key_to_adr:
            node = self.__touch_node(self.key_to_adr[key])
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_adr:
            node = self.__touch_node(self.key_to_adr[key])
            node.val = value
        else:
            if len(self.key_to_adr) == self.space:
                self.key_to_adr.pop(self.cash.next.key)
                self.cash = self.cash.next
            self.c_head.next = Node(value, key)
            self.key_to_adr[key] = self.c_head
            self.c_head = self.c_head.next

    def __touch_node(self, node: Node):
        # двигаем узел в конец и меняем ссылки, если он не последний
        if node.next.next is not None:
            child = node.next
            node.next = child.next
            self.key_to_adr[node.next.key] = node
            child.next = None
            self.c_head.next = child
            self.key_to_adr[child.key] = self.c_head
            self.c_head = child
            return child
        return node.next

class LRUCache1:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.LRU = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key)
            return self.LRU[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.LRU.move_to_end(key)

        self.LRU[key] = value
        if (len(self.LRU) > self.cap):
            self.LRU.popitem(last=False)


if __name__ == '__main__':
    test = LRUCache(2)
    test.put(1, 0)
    test.put(2, 2)
    test.get(1)
    test.put(3, 3)
    test.get(2)
    test.put(4, 4)
    test.get(1)
    test.get(3)
    test.get(4)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)