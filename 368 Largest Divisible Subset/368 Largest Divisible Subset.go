func largestDivisibleSubset(nums []int) []int {
	sort.Ints(nums)
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = 1
	}
	maxSubsetLength, maxSubsetLastIndex := 0, 0
	for i := range nums {
		if curLength := divisibleSubsetLength(nums, dp, i); curLength > maxSubsetLength {
			maxSubsetLength, maxSubsetLastIndex = curLength, i
		}
	}
	if maxSubsetLength == 0 {
		return []int{}
	}
	subset := make([]int, maxSubsetLength)
	indexOfSubset := maxSubsetLength - 1
	subset[indexOfSubset] = nums[maxSubsetLastIndex]
	indexOfSubset--
	for i := maxSubsetLastIndex - 1; i >= 0 && indexOfSubset >= 0; i-- {
		if subset[indexOfSubset+1]%nums[i] == 0 && dp[i] == indexOfSubset+1 {
			subset[indexOfSubset] = nums[i]
			indexOfSubset--
		}
	}
	return subset
}

func divisibleSubsetLength(nums []int, dp []int, index int) int {
	for i := 0; i < index; i++ {
		if nums[index]%nums[i] == 0 {
			dp[index] = max(dp[index], dp[i]+1)
		}
	}
	return dp[index]
}

func max(values ...int) int {
	maxValue := math.MinInt32
	for _, v := range values {
		if v > maxValue {
			maxValue = v
		}
	}
	return maxValue
}
