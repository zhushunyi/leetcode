class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''n = len(nums)
        #print(n)
        i = 0
        while i < n:
            if nums[i] in nums[i+1:]:
                return nums[i]
            i = i + 1'''
        p1 = nums[0]
        p2 = nums[0]
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        #print(p1)
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = p1
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1