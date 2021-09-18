func f(n int, pool []int) int {
	if pool[n] != 0 {
		return pool[n]
	}

	sum := 0
	for i := n-1; i >= 0; i--{
		sum += f(i, pool) * f(n-1-i, pool)
	}
	pool[n] = sum
	return sum
}

func numTrees(n int) int {
    pool := make([]int, n+1) //save f(i)
    pool[0] = 1 //recursive base case, init here
    return f(n, pool)
}
