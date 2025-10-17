class MinStack:

    def __init__(self):
        self.stack = []
        self.__min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.__min_vals:
            self.__min_vals.append(val)
        elif val <= self.__min_vals[-1]:
            self.__min_vals.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.__min_vals[-1]:
            self.__min_vals.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.__min_vals[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(2147483646)
    obj.push(2147483646)
    obj.push(2147483647)
    t1 = obj.top()
    obj.pop()
    min1 = obj.getMin()
    obj.pop()
    min2 = obj.getMin()
    obj.pop()
    obj.push(2147483647)
    t2 = obj.top()
    min3 = obj.getMin()
    obj.push(2147483648)
