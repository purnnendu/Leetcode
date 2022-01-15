func lastStoneWeightII(stones []int) int {
	total := 0
	for _, v := range stones {
		total += v
	}
	half := total >> 1
	dp := make([]int, half+1)
	sort.Ints(stones)
	for _, v := range stones {
		for i := half; i >= v; i-- {
			dp[i] = max(dp[i], dp[i-v] + v)
		}
	}
	return total - 2*dp[half]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
