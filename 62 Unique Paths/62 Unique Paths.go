func uniquePaths(m int, n int) int {
    paths := make([][]int, n)
    for i := 0; i < len(paths); i++ {
        paths[i] = make([]int, m)
    }
    for i := 0; i < m; i++ {
        paths[0][i] = 1
    }
    for j := 1; j < n; j++ {
        paths[j][0] = 1
    }

    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            paths[j][i] = paths[j][i-1] + paths[j-1][i]
        }
    }

    return paths[n-1][m-1]
}
