func containsDuplicate(nums []int) bool {
    var checkMap = map[int]bool{}
    for _, num := range nums {
        if _, ok := checkMap[num]; ok {
            return true
        }
        checkMap[num] = true
    }
    return false
}
