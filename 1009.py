class Solution:
    def bitwiseComplement(self, N: int) -> int:
        a = bin(N)[2:]
        p = 0
        q = []
        for i in a:
            if i == '1':
                q.append('0')
            else:
                q.append('1')
            p = p + 1
        k = ''.join(q)
        return int(k,2)