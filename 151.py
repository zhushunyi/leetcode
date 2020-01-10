class Solution:
    def reverseWords(self, s: str) -> str:
        #count the space
        num = s.count(" ")
        sentence = s.split(" ",num+1)
        sentence.reverse()
        out = ""
        while '' in sentence:
            sentence.remove('')
        for i in sentence:
            print(i)
            out = out + i + " "
        #print(out.count(' '))
        return out[:-1]