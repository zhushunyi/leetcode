class Solution:
    def mySqrt(self, x: int) -> int:
        '''if x == 0:
            return 0
        if x == 1:
            return 1
            
        for i in range(1,int(x/2)+1):
            if i * i <= x and (i+1)*(i+1) > x:
                print(i)
                return i'''
        #Newton
        if x == 0:
            return 0
        init = 2
        while True:
            pre = init
            init = (init + x/init)/2
            if abs(pre-init) < 0.01:
                return int(init)