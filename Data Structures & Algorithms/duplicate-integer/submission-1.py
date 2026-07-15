class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for element in nums:
            if element in hashmap:
                return True
            hashmap.add(element)
        return False