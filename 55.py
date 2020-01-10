class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        length = len(nums)
        for i,j in enumerate(nums):
            if distance >= i and i + j > distance:
                distance = i + j
            if i > distance:
                return False
            if distance >=length:
                return True
        return distance >= i