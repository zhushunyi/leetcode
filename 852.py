class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        max_val = max(A)
        return A.index(max_val,0)