class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        arr = [0]* N
        length = len(trust)
        for i in range(0,length):
            arr[trust[i][1]-1] += 1
            arr[trust[i][0]-1] -= 1
        #print(arr)
        if max(arr) == N - 1:
            return arr.index(max(arr)) + 1
        else:
            return -1