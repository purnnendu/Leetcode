const max = 1_000_000_000 + 7

func knightDialer(n int) int {
    var (
        x1 uint = 1
        x2 uint = 1
        x3 uint = 1
        x4 uint = 1
        x5 uint = 1
        x6 uint = 1
        x7 uint = 1
        x8 uint = 1
        x9 uint = 1
        x0 uint = 1
    )

    for i := 0; i < n - 1; i++ {
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 =
            (x6 + x8) % max,
            (x7 + x9) % max,
            (x4 + x8) % max,
            (x3 + x9 + x0) % max,
            0,
            (x1 + x7 + x0) % max,
            (x2 + x6) % max,
            (x1 + x3) % max,
            (x2 + x4) % max,
            (x4 + x6) % max
    }

    return int((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % max)
}

func knightDialer2(n int) int {
    var res int

    dp := make([]int, 4 * 3 * (n - 1))

    for i := 0; i < 4; i++ {
        for j := 0; j < 3; j++ {
            res = (res + paths(i, j, n, dp)) % max
        }
    }

    return res
}

func paths(i, j, n int, dp []int) int {
    // i == 3 && j != 1 are `*` and `#`.
    if i < 0 || j < 0 || i >= 4 || j >= 3 || (i == 3 && j != 1) {
        return 0
    }

    if n <= 1 {
        return 1
    }

    key := (n - 2) * 4 * 3 + j * 4 + i
    if dp[key] > 0 {
        return dp[key]
    }

    res := paths(i - 1, j - 2, n - 1, dp) % max + // jump to a
        paths(i - 2, j - 1, n - 1, dp) % max + // jump to b
        paths(i - 2, j + 1, n - 1, dp) % max + // jump to c
        paths(i - 1, j + 2, n - 1, dp) % max + // jump to d
        paths(i + 1, j + 2, n - 1, dp) % max + // jump to e
        paths(i + 2, j + 1, n - 1, dp) % max + // jump to f
        paths(i + 2, j - 1, n - 1, dp) % max + // jump to g
        paths(i + 1, j - 2, n - 1, dp) % max // jump to h
    dp[key] = res

    return res
}
