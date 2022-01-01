type coords struct {
	i int
	j int
}

func maxAreaOfIsland(grid [][]int) int {
	seen := make([][]bool, len(grid))
	for i := range seen {
		seen[i] = make([]bool, len(grid[0]))
	}

	maxArea := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 && seen[i][j] == false {
				seen[i][j] = true
				stack := make([]coords, 0)
				stack = append(stack, coords{i, j})
				area := 0
				for len(stack) > 0 {
					x := stack[len(stack)-1].i
					y := stack[len(stack)-1].j
					stack = stack[:len(stack)-1]

					area++
					for r := 0; r < 4; r++ {
						x1 := x - 1
						y1 := y
						switch r {
						case 1:
							x1, y1 = x, y-1
						case 2:
							x1, y1 = x+1, y
						case 3:
							x1, y1 = x, y+1
						}

						if x1 >= 0 && x1 < len(grid) &&
							y1 >= 0 && y1 < len(grid[0]) &&
							grid[x1][y1] == 1 &&
							seen[x1][y1] == false {
							seen[x1][y1] = true
							stack = append(stack, coords{x1, y1})
						}
					}
				}
				if area > maxArea {
					maxArea = area
				}
			}
		}
	}
	return maxArea
}
