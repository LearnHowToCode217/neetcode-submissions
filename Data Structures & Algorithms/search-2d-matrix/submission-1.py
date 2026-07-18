class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                val = (l+r) // 2
                if matrix[i][val] == target:
                    return True
                elif matrix[i][val] < target:
                    l = val + 1
                else:
                    r = val - 1
        
        return False