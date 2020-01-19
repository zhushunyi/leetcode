class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #Monotonic stack
        stack = []
        length = len(nums)
        res = [-1]*length
        for i in range(length*2-1,-1,-1):
            while(stack and nums[stack[-1]]<=nums[i%length]):
                stack.pop()
            res[i%length] = -1 if stack==[] else nums[stack[-1]]            
            stack.append(i%length)
        return res