class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        #divide into two array
        length = len(A)
        odd_list = []
        even_list = []
        for i in A:
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        output = []
        n = len(even_list)
        for i in range(0,n):
            output.append(even_list[i])
            output.append(odd_list[i])
        return output
