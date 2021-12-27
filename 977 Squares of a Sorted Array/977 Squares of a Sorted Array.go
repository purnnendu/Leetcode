func sortedSquares(A []int) []int {
    N := len(A)
	B := make([]int, N)

	for i, v := range A {
		A[i] = v * v
	}

	for i, j, k := 0, N-1, N-1; i <= j; k-- {
		if A[i] > A[j] {
			B[k] = A[i]
			i++
		} else {
			B[k] = A[j]
			j--
		}
	}

    return B
}
