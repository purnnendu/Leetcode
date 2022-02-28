func knightProbability(n int, k int, row int, column int) float64 {
    dp := make([][]float64, n)
    for i := range dp {
        dp[i] = make([]float64, n)
    }

    nxt := make([][]float64, n)
    for i := range nxt {
        nxt[i] = make([]float64, n)
    }

    moves := []int{1, 2,
                  2, 1,
                  -1, 2,
                  -2, 1,
                  -1, -2,
                  -2, -1,
                  1, -2,
                  2, -1,}

    dp[row][column] = 1.0
    for i := 0; i < k; i++ {
        for r := 0; r < n; r++ {
            for c := 0; c < n; c++ {
                if dp[r][c] > 0 {
                    for w := 0; w < 16; w += 2 {
                        nr, nc := r+moves[w], c+moves[w+1]
                        if nr >= 0 && nr < n && nc >= 0 && nc < n {
                            nxt[nr][nc] += dp[r][c] / 8
                        }
                    }
                }
            }
        }

        dp, nxt = nxt, dp
        for i := range nxt {
            for j := range nxt[i] {
                nxt[i][j] = 0
            }
        }
    }



    res := 0.0
    for i := range dp {
        for _, d := range dp[i] {
            res += d
        }
    }

    return res
}
