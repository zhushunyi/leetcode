class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            a1 = max(stones)
            stones.remove(a1)
            a2 = max(stones)
            stones.remove(a2)
            if a1 != a2:
                stones.append(abs(a1-a2))
        
        if len(stones) == 0:
            return 0
        else:
            return max(stones)
