func minimumTotal(triangle [][]int) int {
	s := &solution{}
	return s.minimumTotal(triangle)
}

type solution struct {
}

func (s *solution) minimumTotal(mutableTriangle [][]int) int {
	for row := len(mutableTriangle) - 2; row >= 0; row-- {
		for column := 0; column < len(mutableTriangle[row]); column++ {
			mutableTriangle[row][column] += s.min(mutableTriangle[row+1][column], mutableTriangle[row+1][column+1])
		}
	}

	return mutableTriangle[0][0]
}

func (s *solution) min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
