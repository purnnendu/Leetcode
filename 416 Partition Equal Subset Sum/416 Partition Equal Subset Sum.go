func canPartition(nums []int) bool {
    sum := 0
    for _, n := range nums {
        sum += n
    }
    if sum % 2 == 1 {
        return false
    }

    sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })

    sum /= 2

    dp := make([]int, len(nums))

    for i, n := range nums {
        if n == sum {
            return true
        }
        if n > sum {
            continue
        }
        max := n
        for j := 0; j < i; j++ {
            v := dp[j] + n
            if v == sum {
                return true
            }
            if v < sum && v > max {
                max = v
            }
        }
        dp[i] = max
    }
    return false
}
