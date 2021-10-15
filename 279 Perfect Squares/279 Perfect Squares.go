import "math"

var res = make([]int, 16000);

func numSquares(n int) int {
    if res[n] > 0 {
        return res[n]
    }
    sqrt := sqrtInt(n)
    if n == sqrt * sqrt {
        return 1
    }
    for i := 1; i <= sqrt; i++ {
        res[i * i] = 1
    }
    for i := 2; i <= n; i++ {
        if res[i] > 0 {
            continue
        }
        sqrt = sqrtInt(i)
        min := 4
        for j := 1; j <= sqrt; j++ {
            if min > res[i - j * j] + 1 {
                min = res[i - j * j] + 1
            }
        }
        res[i] = min
    }
    return res[n]
}

func sqrtInt(a int) int {
    return int(math.Sqrt(float64(a)))
}
