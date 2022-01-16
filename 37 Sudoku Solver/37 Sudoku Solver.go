func solveSudoku(board [][]byte)  {
    rowM, colM, gridM := [9][10]bool{}, [9][10]bool{}, [3][3][10]bool{}
    for i, row := range board {
        for j := range row {
            if board[i][j] == '.' {
                continue
            }

            v := int(board[i][j]-'0')
            rowM[i][v] = true
            colM[j][v] = true
            gridM[i/3][j/3][v] = true
        }
    }

    m, n := 9, 9
    var helper func(i, j int) bool
    helper = func(i, j int) bool {
        if i == m {
            return true
        }

        ni, nj := i, j+1
        if nj == n {
            ni, nj = i+1, 0
        }

        if board[i][j] != '.' {
            return helper(ni, nj)
        }

        for v := 1; v < 10; v++ {
            if rowM[i][v] || colM[j][v] || gridM[i/3][j/3][v] {
                continue
            }
            rowM[i][v] = true
            colM[j][v] = true
            gridM[i/3][j/3][v] = true
            board[i][j] = '0' + byte(v)

            if helper(ni, nj) {
                return true
            }

            rowM[i][v] = false
            colM[j][v] = false
            gridM[i/3][j/3][v] = false
            board[i][j] = '.'
        }
        return false
    }

    helper(0, 0)
}
