func integerBreak(n int) int {
    if n > 3 { n++ }
    dp := make([]int, n+1)
    dp[1] = 1
    for i:= 2; i <= n; i++ {
        for j:= 1; j < i; j++ {
            a := dp[i]
            if a < j * dp[i-j] {
                dp[i] = j * dp[i-j]
            }
        }
    }
    return dp[n]
}
