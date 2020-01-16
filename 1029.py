class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        #suppose all go to a
        new_list = []
        sum = 0
        for i in range(0,length):
            new_list.append(costs[i][0]-costs[i][1])
            sum = sum + costs[i][0]
        #print(new_list)
        #print(sum)
        new_list = sorted(new_list,reverse= True)
        for i in range(0,int(length/2)):
            sum = sum - new_list[i]
        return sum
