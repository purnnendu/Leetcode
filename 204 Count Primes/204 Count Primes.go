func countPrimes(n int) int {
    if n < 3 { return 0 }
    npr := make([]bool, n/2)
    npr[0] = true
    for i := 3; i * i < n; i += 2 {
        if npr[i/2] { continue }
        for j := i * i; j < n; j += 2 * i {
            npr[j/2] = true
        }
    }
    res := 1
    for i := 3; i < n; i += 2 {
        if !npr[i/2] {
            res++
        }
    }
    return res
}
