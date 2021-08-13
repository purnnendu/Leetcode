func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	buyPrice := prices[0]
	maxProfit := 0

	for i := 1; i < len(prices); i++ {
		if prices[i] > buyPrice {
			maxProfit = Max(maxProfit, prices[i]-buyPrice)
		} else {
			buyPrice = prices[i]
		}
	}

	return maxProfit
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
