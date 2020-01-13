class Solution:
    def binaryGap(self, N: int) -> int:
        b = str(bin(N))[2:]
        n = 1
        array = []
        length = len(b)
        for i in range(0,length):
            if b[i] == '1':
                array.append(i)
        value = 0
        p = len(array)
        for i in range(1,p):
            value = max(value,array[i] - array[i-1])
        #print(array)
        return value