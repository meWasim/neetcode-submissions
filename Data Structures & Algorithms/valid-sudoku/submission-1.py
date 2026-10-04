class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                for c1 in range(c + 1, 9):
                    if board[r][c] == board[r][c1]:
                        return False

        # Check columns
        for c in range(9):
            for r in range(9):

                if board[r][c] == '.':
                    continue

                for r1 in range(r + 1, 9):
                    if board[r][c] == board[r1][c]:
                        return False

        # Check 3x3 boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                for boxr in range(r, r + 3):
                    for boxc in range(c, c + 3):

                        if board[boxr][boxc] == '.':
                            continue

                        for r2 in range(r, r + 3):
                            for c2 in range(c, c + 3):

                                if boxr == r2 and boxc == c2:
                                    continue

                                if board[boxr][boxc] == board[r2][c2]:
                                    return False

        return True