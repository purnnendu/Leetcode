func updateMatrix(mat [][]int) [][]int {
    q := list.New()
    m, n := len(mat), len(mat[0])
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] == 0 {
                q.PushBack([2]int{i, j})
            } else {
                mat[i][j] = -1
            }
        }
    }
    step := 0
    dirs := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    for q.Len() > 0 {
        k := q.Len()
        for k > 0 {
            item := q.Remove(q.Front()).([2]int)
            for _, d := range dirs {
                x, y := item[0] + d[0], item[1] + d[1]
                if x >= 0 && x < m && y >= 0 && y < n && mat[x][y] == -1 {
                    mat[x][y] = step+1
                    q.PushBack([2]int{x, y})
                }
            }
            k--
        }
        step++
    }
    return mat
}
