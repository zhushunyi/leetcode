class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a set
        ret = 0
        new_set = set(nums)
        for i in new_set:
            if not i - 1 in new_set:
                temp = i
                temp_ret = 1
                while temp + 1 in new_set:
                    temp_ret = temp_ret + 1
                    temp = temp + 1
                ret = max(ret,temp_ret)
        return ret