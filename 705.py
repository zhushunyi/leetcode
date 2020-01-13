class MyHashSet:

    def __init__(self,a = [], number = 1000):
        """
        Initialize your data structure here.
        """
        
        self.number = 1000
        self.a = [[] for _ in range(self.number)]

    def add(self, key: int) -> None:
        index = key % self.number
        if key not in self.a[index]:
            self.a[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % self.number
        if key in self.a[index]:
            self.a[index].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.number
        return key in self.a[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)