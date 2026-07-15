class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exnums = []
        for i in nums:
            if i in exnums:
                return True
            else:
                exnums.append(i)
        return False

