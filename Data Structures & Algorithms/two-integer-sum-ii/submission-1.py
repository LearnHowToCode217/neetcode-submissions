class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while r > l:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1, r+1]
            if val < target:
                l += 1
            if val > target:
                r -= 1
        return []
