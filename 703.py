class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums,reverse = True)
        self.k = k
        if k > len(nums):
            self.ret = float("-inf")
        else:
            self.ret = self.nums[self.k-1]
        

    def add(self, val: int) -> int:
        if val > self.ret:
            self.nums.append(val)
            self.nums = sorted(self.nums,reverse = True)
            self.ret = self.nums[self.k-1]
        return self.ret
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)