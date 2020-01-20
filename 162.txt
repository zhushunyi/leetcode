class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #O(log(n))
        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            mid = (left + right)//2
            if(nums[mid]>nums[mid+1]):
                right=mid
            else:
                left=mid+1
        return left