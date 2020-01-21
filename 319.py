class Solution:
    def bulbSwitch(self, n: int) -> int:
        #time exceed
        '''bulb = [0] * n
        for i in range(1,n+1):
            for j in range(i-1,n,i):
                if bulb[j] == 0:
                    bulb[j] = 1
                else:
                    bulb[j] = 0
        #print(bulb)
        return sum(bulb)'''
        return int(n**0.5)
