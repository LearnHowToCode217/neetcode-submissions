class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for char in nums:
            if char in hashmap:
                return True
            hashmap.add(char)
        return False    