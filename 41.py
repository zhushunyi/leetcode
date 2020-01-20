class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bit map
        length = len(nums)
        if 1 not in nums:
            return 1
        if length == 1:
            return 2
        #negative numbers and numbers over n
        for i in range(length):
            if nums[i] <= 0 or nums[i] > length:
                nums[i] = 1
        #change the bit map
        for i in range(length): 
            a = abs(nums[i])
            if a == length:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
        for i in range(1, length):
            if nums[i] > 0:
                return i       
        if nums[0] > 0:
            return length           
        return length + 1

