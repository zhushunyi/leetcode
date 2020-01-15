from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bull = 0
        cow = 0
        k = ["%d"%(i) for i in range(0,10)]
        for i in range(0,n):
            if secret[i] == guess[i]:
                bull = bull + 1
        #two counter for examining every element
        c1 = Counter(secret)
        c2 = Counter(guess)
        print(c1)
        print(c2)
        for i in k:
            cow = cow + min(c1[i],c2[i])
        cow = cow - bull
        return "%dA%dB"%(bull,cow)