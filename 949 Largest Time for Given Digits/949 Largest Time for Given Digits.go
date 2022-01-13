func permutations(arr []int)[][]int{
    var helper func([]int, int)
    res := [][]int{}

    helper = func(arr []int, n int){
        if n == 1{
            tmp := make([]int, len(arr))
            copy(tmp, arr)
            res = append(res, tmp)
        } else {
            for i := 0; i < n; i++{
                helper(arr, n - 1)
                if n % 2 == 1{
                    tmp := arr[i]
                    arr[i] = arr[n - 1]
                    arr[n - 1] = tmp
                } else {
                    tmp := arr[0]
                    arr[0] = arr[n - 1]
                    arr[n - 1] = tmp
                }
            }
        }
    }
    helper(arr, len(arr))
    return res
}
func inRange(rangeStart int, rangeEnd int, element int) bool {
    if element >= rangeStart && element <= rangeEnd {
        return true
    }
    return false
}
func isValid(A []int) bool {
    rst := true
    if !inRange(0, 2, A[0]) {
        rst = false
    }
    if A[0] == 2 {
        if !inRange(0,3, A[1]) { rst = false}
    } else {
        if !inRange(0,9, A[1]) { rst = false}
    }
    if !inRange(0, 5, A[2]) { rst = false}
    return rst

}
func sliceToInt(s []int) int {
    res := 0
    op := 1
    for i := len(s) - 1; i >= 0; i-- {
        res += s[i] * op
        op *= 10
    }
    return res
}
func findMax(validTime [][]int) []int {
    max := 0000
    index := 0
    for idx, i := range validTime {
        val := sliceToInt(i)
        if val > max {
            max = val
            index = idx
        }
    }
    return validTime[index]
}
func largestTimeFromDigits(A []int) string {
    perms := permutations(A)
    valid := make([][]int, 0)
    for _, perm := range perms {
        if isValid(perm) {valid = append(valid, perm)}
    }
    if len(valid) == 0 { return "" }
    max := findMax(valid)
    return fmt.Sprintf("%d%d:%d%d", max[0], max[1], max[2], max[3])
}
