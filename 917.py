class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        #finding from the front
        i = 0
        #finding from the back
        j = len(S)-1
        k = list(S)
        while i < j:
            if ord(S[i]) < 65 or 90 < ord(S[i]) < 97 or ord(S[i]) > 122:
                i = i + 1
                #print(i)
            elif ord(S[j]) < 65 or 90 < ord(S[j]) < 97 or ord(S[j]) > 122:
                j = j - 1
                #print(j)
            else:
                temp = S[i]
                tmp = S[j]
                k[i] = tmp
                k[j] = temp
                i = i + 1
                j = j - 1
                #print(k)
        return ''.join(k)