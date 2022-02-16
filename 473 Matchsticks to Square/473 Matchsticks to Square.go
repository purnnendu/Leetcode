func makesquare(matchsticks []int) bool {
    sum := 0
	for _, n := range matchsticks {
		sum += n
	}
	if sum%4 != 0 || sum == 0 {
		return false
	}
	target := sum / 4
	sort.Slice(matchsticks, func(i, j int) bool { return matchsticks[i] > matchsticks[j] })
	var dfs func(curSum int, side int, i int) bool
	dfs = func(curSum int, side int, idx int) bool {
		if side == 4 {
			return true
		}
		if curSum == target {
			return dfs(0, side+1, 0)
		}
		if curSum > target {
			return false
		}
		for i := idx; i < len(matchsticks); i++ {
			if matchsticks[i] != 0 {
				tmp := matchsticks[i]
				matchsticks[i] = 0
				if dfs(curSum+tmp, side, i+1) {
					return true
				}

				matchsticks[i] = tmp
                if curSum == 0 {
                    return false
                }
			}
		}
		return false
	}
	return dfs(0, 1, 0)
}
