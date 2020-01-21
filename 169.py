from collections import Counter
class Solution:
    def majorityElement(self, nums):
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)