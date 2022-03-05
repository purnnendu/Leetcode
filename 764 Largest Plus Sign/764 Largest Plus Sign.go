func orderOfLargestPlusSign(n int, mines [][]int) int {
	grid := make([][]int, 0, n)
	for i := 0; i < n; i++ {
		row := make([]int, n, n)
		for j := 0; j < n; j++ {
			row[j] = n
		}
		grid = append(grid, row)
	}
	for _, ij := range mines {
		grid[ij[0]][ij[1]] = 0
	}

	for i := 0; i < n; i++ { // check four direction in one loop
		for j, left := 0, 0; j < n; j++ { // left
			if grid[i][j] == 0 {
				left = 0
			} else {
				left++
			}
			if left < grid[i][j] {
				grid[i][j] = left
			}
		}
		for j, right := n-1, 0; j >= 0; j-- { // right
			if grid[i][j] == 0 {
				right = 0
			} else {
				right++
			}
			if right < grid[i][j] {
				grid[i][j] = right
			}
		}
		for j, up := 0, 0; j < n; j++ { // up
			if grid[j][i] == 0 {
				up = 0
			} else {
				up++
			}
			if up < grid[j][i] {
				grid[j][i] = up
			}
		}
		for j, down := n-1, 0; j >= 0; j-- { // down
			if grid[j][i] == 0 {
				down = 0
			} else {
				down++
			}
			if down < grid[j][i] {
				grid[j][i] = down
			}
		}
	}

	r := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > r {
				r = grid[i][j]
			}
		}
	}

	return r
}
