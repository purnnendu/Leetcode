func findMaxForm(strs []string, m int, n int) int {
    memo := make([][]int, m + 1)
    for i := range memo {
        memo[i] = make([]int, n + 1)
    }
    for _, s := range strs {
        z := strings.Count(s, "0")
        o := len(s) - z
        for i := m; i >= z; i -= 1 {
            for j := n; j >= o; j -= 1 {
                t := memo[i - z][j - o] + 1
                if t > memo[i][j] {
                    memo[i][j] = t
                }
            }
        }
    }
    return memo[m][n]
}
