class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check(values):
            seen = set()

            for value in values:
                if value == '.':
                    continue
                elif value in seen:
                    return False
                
                seen.add(value)
            return True
        
        for row in board:
            if not check(row):
                return False
        
        for column in range(9):
            values = []
            for row in board:
                values.append(row[column])
            if not check(values):
                return False

        for box_row in range(3):
            for box_column in range(3):
                values = []
                for row in range(box_row*3, box_row*3 + 3):
                    for column in range(box_column*3, box_column*3 + 3):
                        values.append(board[row][column])
                    if not check(values):
                        return False
        return True    
        