func subarraySum(nums []int, k int) int {
    pre := make(map[int]int, len(nums)+1)
    sum := 0
    pre[0] = 1
    res := 0
    for i := range nums {
        sum += nums[i]
        if v, ok := pre[sum-k]; ok {
            res += v
        }
        pre[sum]++
    }
    return res
}
