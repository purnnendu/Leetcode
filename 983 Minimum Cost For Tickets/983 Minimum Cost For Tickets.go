func getIndex(days []int, index, num int) int {
    i := index - 1
    for ; i >= 0; i-- {
        if days[i] <= num {
            return i
        }
    }
    return -1
}

func mincostTickets(days []int, costs []int) int {
    n := len(days)
    dp := make([]int, n+1)
    for i := 1; i<=n; i++ {
        dp[i] = costs[0] + dp[i-1]
        weekIndex := getIndex(days, i-1, days[i-1] - 7) + 1
        monthIndex :=  getIndex(days, i-1, days[i-1] - 30) + 1
        dp[i] = min(dp[i], costs[1] + dp[weekIndex])
        dp[i] = min(dp[i], costs[2] + dp[monthIndex])
    }
    return dp[n]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
