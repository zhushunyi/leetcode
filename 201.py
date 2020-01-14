class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        #time exceeds
        '''length1 = len(bin(m)[2:])
        length2 = len(bin(n)[2:])
        if length1 - length2 <2:
            for i in range(m,n):
                temp = temp & i
        else:
            temp =  2**(length1-1)'''

        while n > m:
            #keep the digits same
            n = n & (n-1)
        return n