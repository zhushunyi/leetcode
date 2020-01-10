class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for i in J:
            sum = sum + S.count(i)
            J.replace(i,"")
        return sum