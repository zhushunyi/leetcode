
class Solution:
    def tribonacci(self, n: int) -> int:
        #dynamic programming
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        a = [0]*(n+1)
        a[0] = 0
        a[1] = 1
        a[2] = 1
        for i in range(3,n+1):
            a[i] = a[i-1]+a[i-2]+a[i-3]
        return a[n]