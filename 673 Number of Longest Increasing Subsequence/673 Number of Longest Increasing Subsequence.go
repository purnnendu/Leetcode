func findNumberOfLIS(nums []int) int {
    dp := make([]int, len(nums))
    count := make([]int, len(nums))

    for i := range dp {
        dp[i] = 1
        count[i] = 1
    }

    longest := 1
    totalLIS := 1
    for i := 1; i < len(nums); i++ {
        for j := 0; j < i; j++ {
            if nums[i] > nums[j] {
                if dp[i] < dp[j]+1 {
                    dp[i] = dp[j]+1
                    count[i] = count[j]
                } else if dp[i] == dp[j]+1 {
                    count[i] += count[j]
                }
            }
        }
        if longest < dp[i] {
            longest = dp[i]
            totalLIS = count[i]
        } else if longest == dp[i] {
            totalLIS += count[i]
        }
    }
    return totalLIS
}
