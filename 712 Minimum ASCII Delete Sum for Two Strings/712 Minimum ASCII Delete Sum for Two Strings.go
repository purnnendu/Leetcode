func minimumDeleteSum(s1 string, s2 string) int {

    if len(s1) < len(s2) {
        s1, s2 = s2, s1
    }

    m, n := len(s1), len(s2)

    var tot int
    for i := range s1 {
        tot += int(s1[i])
    }
    for i := range s2 {
        tot += int(s2[i])
    }

    dp := make([]int, n+1)
    next_dp := make([]int, n+1)

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if s1[i] == s2[j] {
                next_dp[j+1] = dp[j] + int(s1[i])
            } else {
                next_dp[j+1] = max(dp[j], next_dp[j], dp[j+1])
            }
        }
        dp, next_dp = next_dp, dp
    }

    return tot - 2*dp[n]
}

func max(a, b, c int) int {
    if c > b {
        b = c
    }
    if b > a {
        a = b
    }
    return a
}
