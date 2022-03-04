func deleteAndEarn(nums []int) int {
    numMap := map[int]int{}
    for _, n := range nums {
        numMap[n]++
    }
    sortedNums := make([]int, 0, len(numMap))
    for num := range numMap {
        sortedNums = append(sortedNums, num)
    }
    sort.Ints(sortedNums)

    dp1, dp2 := 0, 0
    for i, n := range sortedNums {
        if i > 0 && sortedNums[i] == sortedNums[i-1] + 1 {
            dp1, dp2 = dp2 + n * numMap[n], max(dp1, dp2)
        } else {
            dp1, dp2 = max(dp1, dp2) + n * numMap[n], max(dp1, dp2)
        }
    }
    return max(dp1, dp2)
}

func max(n1, n2 int) int {
    if n1 > n2 {
        return n1
    } else {
        return n2
    }
}
