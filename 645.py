class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #time exceeds
        '''n = len(nums)
        out = []
        for i in range(1,n+1):
            if i in nums:
                nums.remove(i)
                if i in nums:
                    a = i
            else:
                b = i
        out.append(a)
        out.append(b)
        return out'''
        n = len(nums)
        arr = [0] * n
        for i in range(len(nums)):
            arr[nums[i]-1] = arr[nums[i]-1] + 1
        #duplicated element
        d = arr.index(2)+1
        #missing
        m = arr.index(0)+1
        return [d,m]
        