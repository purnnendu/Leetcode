func tribonacci(n int) int {
    triset := [3]int{0, 1, 1}
    if n < 3 {
        return triset[n]
    }
    for i := 3; i <= n; i++ {
        triset[i % 3] = triset[0] + triset[1] + triset[2]
    }
    return triset[n % 3]
}
