func findTargetSumWays(nums []int, target int) int {
    sum := 0
	for _, v := range nums {
		sum += v
	}

	if sum < target || -sum > target {
		return 0
	}

	if (target+sum)%2 == 1 {
		return 0
	}

	sumOfPositives := (target + sum) / 2

	dp := make([]int, sumOfPositives+1)
	dp[0] = 1

	for i := 0; i < len(nums); i++ {
		for j := sumOfPositives; j >= nums[i]; j-- {
			dp[j] = dp[j] + dp[j-nums[i]]
		}
	}

    return dp[sumOfPositives]
}
