import random


class RandomizedSet1(object):
    # 99% память 36% время
    def __init__(self):
        self.__s = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.__s:
            return False
        else:
            self.__s.add(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.__s:
            self.__s.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.__s))


class RandomizedSet2:
    # 69% память 72% время, но тут всё O(1)
    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val not in self.dict:
            return False
        idx = self.dict[val]
        del self.dict[val]
        if idx != len(self.list) - 1:
            self.list[idx] = self.list[-1]
            self.dict[self.list[-1]] = idx
        self.list.pop()
        return True

    def getRandom(self):
        return random.choice(self.list)


if __name__ == '__main__':
    r = RandomizedSet2()
    print(r.insert(1))
    print(r.remove(2))
    print(r.insert(2))
    print(r.getRandom())
    print(r.remove(1))
    print(r.insert(2))
    print(r.getRandom())


