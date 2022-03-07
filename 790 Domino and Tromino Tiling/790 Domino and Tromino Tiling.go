func numTilings(n int) int {
    if n <= 2 {
        return n
    }
    dp := make([]int, n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for i:=4;i<=n;i++ {
        dp[i] = (2*dp[i-1]+dp[i-3])%1000000007
    }
    return dp[n]
}
