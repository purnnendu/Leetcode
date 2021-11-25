func isValidSudoku(board [][]byte) bool {

	checkRow := func() bool {
		for i := 0; i < len(board); i++ {
			m := make(map[byte]bool)
			for j := 0; j < len(board[i]); j++ {
				if board[i][j] == '.' {
					continue
				} else if _, ok := m[board[i][j]]; ok {
					return false
				} else {
					m[board[i][j]] = true
				}
			}
		}
		return true
	}
	checkColumn := func() bool {
		for i := 0; i < len(board); i++ {
			m := make(map[byte]bool)
			for j := 0; j < len(board[i]); j++ {
				if board[j][i] == '.' {
					continue
				} else if _, ok := m[board[j][i]]; ok {
					return false
				} else {
					m[board[j][i]] = true
				}
			}
		}
		return true
	}
	checkBox := func() bool {
		for rowBorder := 0; rowBorder < len(board); rowBorder += 3 {
			for columnBorder := 0; columnBorder < len(board); columnBorder += 3 {
				m := make(map[byte]bool)
				for i := rowBorder; i < rowBorder+3; i++ {
					for j := columnBorder; j < columnBorder+3; j++ {
						if board[i][j] == '.' {
							continue
						} else if _, ok := m[board[i][j]]; ok {
							return false
						} else {
							m[board[i][j]] = true
						}
					}
				}
			}
		}
		return true
	}
	if checkRow() && checkColumn() && checkBox() {
		return true
	}
	return false
}
