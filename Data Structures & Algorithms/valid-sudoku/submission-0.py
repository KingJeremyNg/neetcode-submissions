class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                square = (row // 3, col // 3)

                if val == ".":
                    continue

                # Initialize arrays in sets
                if row not in rows:
                    rows[row] = []
                if col not in cols:
                    cols[col] = []
                if square not in squares:
                    squares[square] = []

                # Checks for validity
                if val in rows[row]:
                    return False
                else:
                    rows[row].append(val)
                if val in cols[col]:
                    return False
                else:
                    cols[col].append(val)
                if val in squares[square]:
                    return False
                else:
                    squares[square].append(val)

        return True
