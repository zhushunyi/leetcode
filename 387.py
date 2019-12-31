class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        num = len(s)
        print(num)
        while i < num:
            if s[i] in s[0:i] or s[i] in s[i+1:]:
                i = i + 1
            else:
                break
        if i == num:
            return -1
        else:
            return i