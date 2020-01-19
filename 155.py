class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sta = []
        self.min = float("inf")


    def push(self, x: int) -> None:
        self.sta.append(x)
        if x < self.min:
            self.min = x


    def pop(self) -> None:
        del(self.sta[-1])
        if len(self.sta) == 0:
            self.min = float("inf")
        else:
            self.min = min(self.sta)


    def top(self) -> int:
        return self.sta[-1]


    def getMin(self) -> int:
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()