func uniquePathsWithObstacles(mat [][]int) int {
    m, n := len(mat), len(mat[0])
    if mat[0][0] == 1 {
        mat[0][0] = 0
    } else {
        mat[0][0] = 1
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i == 0 && j == 0 {
                continue
            }
            r := 0
            if mat[i][j] != 1 {
                if i-1 >= 0 {
                    r += mat[i-1][j]
                }
                if j-1 >= 0 {
                    r += mat[i][j-1]
                }
            }
            mat[i][j] = r
        }
    }
    return mat[m-1][n-1]
}
