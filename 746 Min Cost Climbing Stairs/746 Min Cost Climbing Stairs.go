func minCostClimbingStairs(cost []int) int {
    min1, min2 := 0, 0
    for i := 2; i <= len(cost); i++{
        tmp := min2
        min2 = min(min1 + cost[i-2], min2+cost[i-1])
        min1 = tmp
    }
    return min2
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
