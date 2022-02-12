func numberOfArithmeticSlices(nums []int) int {
    if len(nums) < 3 {
        return 0
    }
    dp := make([]int, len(nums))
    dp[0] = 0
    dp[1] = 0
    for i := 2; i < len(nums); i ++ {
        if nums[i] - nums[i-1] != nums[i-1] - nums[i-2] {
            dp[i] = dp[i-1]
        } else {
            dp[i] = dp[i-1] + dp[i-1] - dp[i-2] + 1
        }
    }
    return dp[len(nums) - 1]
}
