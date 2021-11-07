func titleToNumber(columnTitle string) int {
    var sum float64 = 0
    n := len(columnTitle)
    for i, v := range columnTitle {
        y := float64(n - i - 1)
        sum += math.Pow(26, y) * float64(v - 64)
    }
    return int(sum)
}
