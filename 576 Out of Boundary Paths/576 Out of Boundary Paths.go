var cords = []int{-1, 1}
var M = 1000000000 + 7

func findPathsRecursive(m, n, maxMove, startRow, startColumn int, cache [][][]int) int {

	// Check if row is out of bounds
	if startRow >= m || startRow < 0 {
		return 1
	}

	// Check if column is out of bounds
	if startColumn >= n || startColumn < 0 {
		return 1
	}

	// If no moves left, return
	if maxMove == 0 {
		return 0
	}

	if cache[startRow][startColumn][maxMove] != -1 {
		return cache[startRow][startColumn][maxMove]
	}

	paths := 0

	// Recurse for all adjacent coordinates
	for _, iCord := range cords {
		paths += findPathsRecursive(m, n, maxMove-1, startRow+iCord, startColumn, cache)
	}

	for _, jCord := range cords {
		paths += findPathsRecursive(m, n, maxMove-1, startRow, startColumn+jCord, cache)
	}

	cache[startRow][startColumn][maxMove] = paths % M

	return cache[startRow][startColumn][maxMove]

}

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {

	// Initialise empty cache
	// cache[m][n][maxMove+1]
	cache := make([][][]int, m)
	for i := range cache {
		cache[i] = make([][]int, n)
		for j := range cache[i] {
			cache[i][j] = make([]int, maxMove+1)
			for k := range cache[i][j] {
				cache[i][j][k] = -1
			}
		}
	}

	pathCount := findPathsRecursive(m, n, maxMove, startRow, startColumn, cache)

	return pathCount

}
