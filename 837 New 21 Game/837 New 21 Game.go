func new21Game(n int, k int, w int) float64 {
	if n >= k+w || k == 0 {
		return 1.0
	}

	dp := make([]float64, n+1)
	dp[0] = 1.0

	res := 0.0
	runningSum := dp[0]

	for i := 1; i <= n; i++ {
		// at this point, i assume that i have with me the sum of the previous w elements
		dp[i] = runningSum / float64(w)

		// if the element we are trying to add is less than k, only then we will add
		if i < k {
			runningSum += dp[i]
		} else {
			// in case the current i is greater than k we will add it to our answer because at the end we need the sum of dp values from k to n
			res += dp[i]
		}

		if i-w >= 0 {
			// adjust the tail end
			runningSum -= dp[i-w]
		}
	}
	return res
}
