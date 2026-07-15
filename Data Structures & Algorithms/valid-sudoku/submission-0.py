class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9): # Check the rows
            hashset = set()
            for column in range(9):
                if board[row][column] == '.':
                    continue
                elif board[row][column] in hashset:
                    return False
                else:
                    hashset.add(board[row][column])
        
        for column in range(9): # Check the columns
            hashset = set()
            for row in range(9):
                if board[row][column] == '.':
                    continue
                elif board[row][column] in hashset:
                    return False
                else:
                    hashset.add(board[row][column])
        
        for box_row in range(3):
            for box_column in range(3):
                hashset = set()
                for row in range(box_row*3, box_row*3 + 3):
                    for column in range(box_column*3, box_column*3 + 3):
                        if board[row][column] == '.':
                            continue
                        elif board[row][column] in hashset:
                            return False
                        else:
                            hashset.add(board[row][column])
        
        return True
        
        
            