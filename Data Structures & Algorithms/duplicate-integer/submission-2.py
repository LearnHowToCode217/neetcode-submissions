class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = []
        for num in nums:
            if num in hashmap:
                return True
            hashmap.append(num)
        return False