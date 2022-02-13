func eraseOverlapIntervals(intervals [][]int) int {
    sort.Sort(byIntervalEnd(intervals))

    if len(intervals) == 0 {
        return 0
    }
    var remove int
    current := intervals[0]
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] < current[1] {
            remove++
        } else {
            current = intervals[i]
        }
    }
    return remove
}

type byIntervalEnd [][]int

func (b byIntervalEnd) Len() int {
    return len(b)
}

func (b byIntervalEnd) Swap(i, j int) {
    b[i], b[j] = b[j], b[i]
}

func (b byIntervalEnd) Less(i, j int) bool {
    return b[i][1] < b[j][1]
}
