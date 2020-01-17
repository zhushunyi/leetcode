class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        length_1 = len(g)
        length_2 = len(s)
        g = sorted(g)
        s = sorted(s)
        i = j = 0
        sum = 0
        while i < length_1 and j < length_2:
            if g[i] > s[j]:
                j += 1
            else:
                j += 1
                i += 1
                sum += 1
        return sum