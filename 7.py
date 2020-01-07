class Solution:
    def reverse(self, x: int) -> int:
        out = 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        while x != 0:
            a = x % 10
            out = 10 * out + a
            #print(out)
            x = x//10
        if flag:
            #print(out)
            out = -out
            #print(out)
        if out < -math.pow(2,31) or out > math.pow(2,31)-1:
            return 0
        return out