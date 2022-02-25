func findLongestChain(pairs [][]int) int {
    	// sort them
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][1] < pairs[j][1]
	})

	// create chains
	curr := math.MinInt32
    result := 0
    for j := 0; j < len(pairs); j++ {
        if curr < pairs[j][0] {
            curr = pairs[j][1]
            result++
        }
    }
    return result
}

func GetMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}
