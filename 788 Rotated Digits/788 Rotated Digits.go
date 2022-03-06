func validate(n int) bool {
    valid := false

    for n > 0 {
        switch n % 10 {
            case 2, 5, 6, 9:
                valid = true
            case 3, 4, 7:
                return false
        }

        n /= 10
    }

    return valid
}

func rotatedDigits(N int) int {
    result := 0;

    for i := 1; i <= N; i++ {
        if validate(i) {
            result++
        }
    }

    return result
}
