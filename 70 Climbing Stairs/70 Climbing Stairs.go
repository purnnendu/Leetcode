func climbStairs(n int) int {
    if n < 3 {
        return n
    }
    prev, current := 1, 2
    for i := 3; i <= n; i++ {
        prev, current = current, prev+current
    }
    return current
}
