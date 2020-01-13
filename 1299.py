class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        #considering sorting from right to the left
        max_val = -1
        for i in range(length - 1, -1 , -1):
            temp = arr[i]
            arr[i] = max_val
            max_val = max(max_val,temp) 
        return arr