import random
from collections import Counter
class Solution

    def __init__(self, nums List[int])
        self.nums = nums
        

    '''def pick(self, target int) - int
        new_list = []
        temp = Counter(self.nums)
        num = temp[target]
        for i in range(0,num)
            new_list.append(self.nums.index(target,i))
        return new_list[random.randint(0,len(new_list)-1)]'''

    def pick(self, target int) - int
        import random
        ret = -1
        length = -1
        for i, v in enumerate(self.nums)
            if v == target
                length += 1
                if ret == -1
                    ret = i
                else
                    r = random.randint(0, length)
                    if r  1
                        ret = i
        return ret
        


# Your Solution object will be instantiated and called as such
# obj = Solution(nums)
# param_1 = obj.pick(target)