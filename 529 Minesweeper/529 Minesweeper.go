var row, col int
var iter = [][]int{[]int{1, 0}, []int{-1, 0}, []int{0, 1}, []int{0, -1}, []int{1, 1}, []int{1, -1}, []int{-1, -1}, []int{-1, 1}}

func updateBoard(board [][]byte, click []int) [][]byte {
	if board[click[0]][click[1]] == 'M' {
		board[click[0]][click[1]] = 'X'
		return board
	}
	row, col = len(board), len(board[0])
	calcBoard(board, click[0], click[1])
	return board
}

func calcBoard(board [][]byte, r int, c int) {
	if r < 0 || r == row ||
		c < 0 || c == col ||
		board[r][c] != 'E' {
		return
	}

	adjMines := getAdjMines(board, r, c)
	if adjMines > 0 {
		board[r][c] = []byte(strconv.Itoa(adjMines))[0]
		return
	}

	board[r][c] = 'B'
	for _, v := range iter {
		calcBoard(board, r+v[0], c+v[1])
	}
}

func getAdjMines(board [][]byte, r int, c int) int {
	mineCount := 0
	for _, v := range iter {
		x, y := r+v[0], c+v[1]
		if (x >= 0 && x < row) &&
			(y >= 0 && y < col) &&
			(board[x][y] == 'M' || board[x][y] == 'X') {
			mineCount++
		}
	}
	return mineCount
}
