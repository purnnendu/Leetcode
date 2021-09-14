func minPathSum(grid [][]int) int {
    m, n := len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i > 0 && j > 0 {
				g1, g2 := grid[i-1][j], grid[i][j-1]
				if g1 < g2 {
					grid[i][j] += g1
				} else {
					grid[i][j] += g2
				}
				continue
			}
			if i == 0 && j > 0 {
				grid[0][j] += grid[0][j-1]
				continue
			}
			if i > 0 && j == 0 {
				grid[i][0] += grid[i-1][0]
			}
		}
	}
    return grid[m-1][n-1]  
}
