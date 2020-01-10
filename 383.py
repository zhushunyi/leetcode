class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        length = len(ransomNote)
        for i in ransomNote:
            if i in magazine and (ransomNote.count(i) <= magazine.count(i)):
                continue
            else:
                return False
        return True