class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = address.split(".")
        return "[.]".join(string)