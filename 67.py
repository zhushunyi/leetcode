class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = int(a,2)
        b_dec = int(b,2)
        sum = a_dec + b_dec
        return bin(sum)[2:]

