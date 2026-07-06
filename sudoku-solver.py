class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
                box_row = 3 * (row // 3) + i // 3
                box_col = 3 * (col // 3) + i % 3
                if board[box_row][box_col] == num:
                    return False
            return True

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in "123456789":
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if backtrack():
                                    return True
                                board[row][col] = "."
                        return False
                    
            return True

        backtrack()
