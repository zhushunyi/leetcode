class Solution:
    def power(self,a,b):
        if b == 0:
            return 1
        if b == 1:
            return a
        ret = 1
        while b > 0:
            if b & 1 == 1:
                ret = ret * a % 1337
            a = a * a % 1337     
            b = b >> 1
        return ret   


    def superPow(self, a: int, b: List[int]) -> int:
        #time exceed
        '''sum = 0
        for i in b:
            sum = sum*10 + i
        q = str(pow(a,sum))
        
        value = 0
        for i in q:
            value = (value*10 + int(i))%1337
        return value'''
        sum = 1
        for i in b:
            print(sum)
            sum = (self.power(sum,10) * self.power(a,i))%1337
            print(sum)
        return sum