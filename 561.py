class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum = 0
        for i in range(0,len(nums)):
            if i%2 == 0:
                sum =sum + nums[i]

        return sum