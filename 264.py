class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #dynamic programming
        #num[i] = min(2 * num[i2], 3 * num[i3], 5 * num[i5])
        num = n * [0]
        num[0] = 1
        i2 = i3 = i5 = 0
        for i in range(1,n):
            num[i] = min(2 * num[i2], 3 * num[i3], 5 * num[i5])
            if num[i] == 2 * num[i2]:
                i2 = i2 + 1
            if num[i] == 3 * num[i3]:
                i3 = i3 + 1
            if num[i] == 5 * num[i5]:
                i5 = i5 + 1
        return num[-1]