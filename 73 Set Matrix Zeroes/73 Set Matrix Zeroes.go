func setZeroes(matrix [][]int) {

	m := len(matrix)
	n := len(matrix[0])

	leftTop := 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {

				matrix[0][j] = 0

				if i == 0 {
					leftTop = 0
				} else {
					matrix[i][0] = 0
				}
			}

		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[0][j] == 0 || matrix[i][0] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	topLeft := matrix[0][0]

	if topLeft == 0 {
		for i := 0; i < m; i++ {
			matrix[i][0] = 0
		}
	}

	if leftTop == 0 {
		for j := 0; j < n; j++ {
			matrix[0][j] = 0
		}
	}

	return
}
