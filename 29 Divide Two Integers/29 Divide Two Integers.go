func divide(dividend int, divisor int) int {
    flag := -1
    if dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0{
        flag = 1
    }

    dividend, divisor = abs(dividend), abs(divisor)
    total := 0
    for dividend >= divisor{
        tmp := divisor
        cnt := 1
        for dividend > tmp << 1{
            tmp = tmp << 1
            cnt = cnt << 1
        }
        total += cnt
        dividend -= tmp
    }

    if total * flag > math.MaxInt32{

        return math.MaxInt32
    }
    return total * flag
}

func abs(n int)int{
    if n < 0{
        return -n
    }

    return n
}
