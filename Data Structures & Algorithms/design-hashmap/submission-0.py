class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for c in self.hashmap:
            if c[0] == key:
                c[1] = value
                return
                
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for c in self.hashmap:
            if c[0] == key:
                return c[1]
         
        return -1

    def remove(self, key: int) -> None:
        for c in self.hashmap:
            if c[0] == key:
                self.hashmap.remove(c)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)