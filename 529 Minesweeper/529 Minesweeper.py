"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

    'M' represents an unrevealed mine,
    'E' represents an unrevealed empty square,
    'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
    digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
    'X' represents a revealed mine.

You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

    If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
    If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    Return the board when no more squares will be revealed.

Example 1:

Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Example 2:

Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        x, y = click[0], click[1]
        vis = {(x,y)}
        explore = [(x,y)]

        def neighbourBombs(x, y):
            neighs = [[x-1,y], [x+1,y], [x,y-1], [x,y+1], [x+1,y+1], [x-1,y-1], [x+1,y-1], [x-1,y+1]]
            cnt = 0
            temp = []
            for x1, y1 in neighs:
                if rows > x1 >= 0 <= y1 < cols and (x1,y1) not in vis: # neighbour in grid
                    if board[x1][y1] == 'M':
                        cnt += 1
                    temp.append((x1,y1))
            return cnt, temp

        # Case 1: You hit a fucking mine
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        # Case 2: You hit a neighbour to a mine
        cnt, t = neighbourBombs(x, y)
        if cnt > 0:
            board[x][y] = str(cnt)
            return board

        # Case 3: You hit an empty spot
        for x,y in explore:
            cnt, temp = neighbourBombs(x, y)
            vis.add((x,y))
            if cnt > 0:
                board[x][y] = str(cnt)
            else:
                #print(x,y)
                board[x][y] = 'B'
                explore.extend(temp)
                for x,y in temp:
                    vis.add((x,y))



        return board
