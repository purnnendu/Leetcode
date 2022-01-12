func checkValid(matrix [][]int) bool {
    N := len(matrix)

    target := 0
    for i:=0; i<N; i++ {
        target = target ^ (i+1)
    }

    for i:=0; i<N; i++ {
        row := 0
        col := 0

        for j:=0; j<N; j++ {
            row = row ^ matrix[i][j]
            col = col ^ matrix[j][i]
        }


        if row != target || col != target {
            return false
        }
    }

    return true
}
