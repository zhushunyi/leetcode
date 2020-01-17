from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        counter = Counter(deck)
        q = list(counter.values())
        return reduce(gcd,q)>1