func minSteps(n int) int {
    if n == 1 {
        return 0
    }
    factors := factorization(n)
    var res int
    for i := 0; i < len(factors); i++ {
        res += factors[i]
    }

    return res
}


func factorization(n int) []int {
    var res []int
    curNum := n
    for i := 2;  i * i <= curNum; i++ {
        if curNum % i == 0 {
            res = append(res, i)
            curNum = curNum / i
            for curNum % i == 0 {
                res = append(res, i)
                curNum = curNum / i
            }
        }
    }

    if curNum > 1 {
        res = append(res, curNum)
    }


    return res
}
