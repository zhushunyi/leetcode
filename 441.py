class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        temp = n
        while i <= temp:
            temp = temp - i
            i = i + 1
        if i == temp:
            return i
        else:
            return i - 1