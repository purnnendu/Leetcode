func exist(board [][]byte, word string) bool {
    for x:=0; x < len(board) ; x++ {
        for y :=0; y < len(board[0]); y++ {
            if board[x][y] == word[0] && dfs(board, word, x, y) {
                return true
            }
        }
    }
    return false
}

func dfs(board [][]byte, word string, x, y int) bool {
    if len(word) <= 1 {
        return true
    }

    tmp := board[x][y]
    board[x][y] = '0'
    if x - 1 >= 0 && board[x-1][y] == word[1] && dfs(board, word[1:], x-1, y) {
        return true
    }
    if y - 1 >= 0 && board[x][y-1] == word[1] && dfs(board, word[1:], x, y-1) {
        return true
    }
    if x + 1 < len(board) && board[x+1][y] == word[1] && dfs(board, word[1:], x+1, y) {
        return true
    }
    if y + 1 < len(board[0]) && board[x][y+1] == word[1] && dfs(board, word[1:], x, y+1) {
        return true
    }
    board[x][y] = tmp
    return false
}
