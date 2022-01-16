"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
"""
class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:

        def returnMinItem(possible_values):
            i, j, min_value_len = -1, -1, 10
            for k, v in possible_values.items():
                possible_values_count = len(v)
                if possible_values_count == 1:
                    return k
                if possible_values_count < min_value_len:
                    (i, j), min_value_len = k, possible_values_count
            return i, j

        def placeNextDigit(board, possible_values):
            i, j = returnMinItem(possible_values)
            numbers = possible_values.pop((i, j))

            for n in numbers:
                board[i][j] = n
                if not possible_values:
                    return

                discarded = []

                for (i2, j2), v in possible_values.items():
                    if n in v and (i == i2 or j == j2 or i // 3 == i2 // 3 and j // 3 == j2 // 3):
                        # if v == {n}:
                        if len(v) == 1:
                            for v in discarded: 
                                v.add(n)
                            possible_values[i, j] = numbers
                            return
                        v.discard(n) #
                        discarded.append(v)

                placeNextDigit(board, possible_values)

                if not possible_values:
                    return

                for v in discarded:
                    v.add(n)

            possible_values[i, j] = numbers


        possible_values = {
            (i, j): (
                {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
                - {
                    board[i][k] for k in range(9)
                    # if board[i][k] != '.'
                }
                - {
                    board[k][j] for k in range(9)
                    # if board[k][j] != '.'
                }
                - {
                    board[3 * (i // 3) + di][3 * (j // 3) + dj]
                    for di in range(3) for dj in range(3)
                    # if board[3 * (i // 3) + di][3 * (j // 3) + dj] != '.'
                }
            )
            for i in range(9) for j in range(9)
            if board[i][j] == '.'
        }

        i, j = returnMinItem(possible_values)
        while possible_values and len(possible_values[i, j]) == 1:
            n = next(iter(possible_values.pop((i, j))))
            board[i][j] = n
            for (i2, j2), v in possible_values.items():
                if n in v and (i == i2 or j == j2 or (i // 3, j // 3) == (i2 // 3, j2 // 3)):
                    v.discard(n)
            if possible_values:
                i, j = returnMinItem(possible_values)

        if possible_values:
            placeNextDigit(board, possible_values)
