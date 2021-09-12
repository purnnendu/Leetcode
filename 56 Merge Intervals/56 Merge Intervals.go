func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i, j int) bool { return intervals[i][0] < intervals[j][0] })

    res := [][]int{}
    for i, interval := range intervals {
        if i == 0 {
            res = append(res, interval)
            continue
        }

        r := res[len(res)-1]
        if interval[0] <= r[1] && r[1] < interval[1] {
            res[len(res)-1] = []int{r[0], interval[1]}
        }
        if r[1] < interval[0] {
            res = append(res, interval)
        }
    }

    return res
}
