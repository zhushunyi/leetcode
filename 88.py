class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1)
        i = j = k = 0
        #new array
        num = [0] * len(nums1)
        while i < m or j < n:
            print(i,j,k)
            #remaining elements in one array, we can also use inf as a flag to simplify the code
            if i == m:
                num[k] = nums2[j]
                j = j + 1
                k = k + 1
                print(i)
            elif j == n:
                num[k] = nums1[i]
                i = i + 1
                k = k + 1
                print(j)
            else:
                #compare elements
                if nums1[i] >= nums2[j]:
                    num[k] = nums2[j]
                    j = j + 1
                    k = k + 1
                else:
                    num[k] = nums1[i]
                    i = i + 1
                    k = k + 1
                
        print(num)
        for i in range(0,len(nums1)):
            nums1[i] = num[i]