func maximalSquare(matrix [][]byte) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	// row column size
	r, c := len(matrix), len(matrix[0])
	res := 0
	dp := make([][]int, r)
	for i := range dp {
		dp[i] = make([]int, c)
	}
	for i := 0; i < r; i++ {
		for j := 0; j < c; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = int(matrix[i][j] - '0')
			} else if matrix[i][j] == '1' {
				dp[i][j] = Min(dp[i-1][j-1], Min(dp[i][j-1], dp[i-1][j])) + 1
			}
			res = Max(res, dp[i][j])
		}
	}

	return res * res
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
