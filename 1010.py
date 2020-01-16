from collections import Counter
from scipy.special import comb
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        length = len(time)
        sum = 0
        for i in range(0,length):
            time[i] %= 60
        c1 = Counter(time)
        print(c1)
        for i,v in c1.items():
            if not i == 0 and i <30:
                sum += v*c1[60-i]
            if i == 30:
                sum += comb(c1[30],2)
        print(sum)
        #special case
        sum = int(sum + comb(c1[0],2))
        return sum