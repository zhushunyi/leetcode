class Solution:
    def numTrees(self, n: int) -> int:
        '''if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        i = 1
        num = 0
        while i <= 3:
            print(i,num)
            num = num + self.numTrees(i-1) * self.numTrees(n-i)
            i = i + 1
        return num'''
        num = [0] * (n+2)
        #print(len(num))
        num[0] = 1
        num[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                num[i] = num[i] + num[j-1]*num[i-j]
        return num[n]