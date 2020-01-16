from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c1 = Counter(S)
        print(c1)
        s1 = ''
        # nums of character in T
        for i in T:
            if i in S:
                c1[i]+=1
            if not i in S:
                s1+=i
        for k,v in c1.items():
            print(k,v)
            for i in range(0,v-1):
                s1+=k
        return s1
