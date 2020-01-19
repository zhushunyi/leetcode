class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums = sorted(nums)
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False