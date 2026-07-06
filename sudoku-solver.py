class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty.append((r, c))
                else:
                    b = (r // 3) * 3 + c // 3
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)

        def backtrack(idx):
            if idx == len(empty):
                return True

            row, col = empty[idx]
            b = (row // 3) * 3 + col // 3

            for num in "123456789":
                if num not in rows[row] and num not in cols[col] and num not in boxes[b]:
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[b].add(num)

                    if backtrack(idx + 1):
                        return True

                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack(0)
