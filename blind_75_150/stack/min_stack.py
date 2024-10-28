from collections import defaultdict


class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.cur_mins or self.cur_mins[-1] >= val:
            self.cur_mins.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.cur_mins[-1]:
            self.cur_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cur_mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

