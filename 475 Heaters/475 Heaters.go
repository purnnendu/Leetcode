func findRadius(houses []int, heaters []int) int {
	if len(houses) == 0 || len(heaters) == 0 {
		return 0
	}
	sort.Ints(heaters)
	maxDistance := math.MinInt32
	for _, house := range houses {
		l, r := 0, len(heaters)-1
		var m int
		for l <= r {
			m = (l + r) / 2
			if heaters[m] < house {
				l = m + 1
			} else if heaters[m] > house {
				r = m - 1
			} else {
				break
			}
		}
		lV, rV, mV := math.MaxInt32, math.MaxInt32, math.MaxInt32
		if r >= 0 {
			rV = abs(heaters[r] - house)
		}
		if l < len(heaters) {
			lV = abs(heaters[l] - house)
		}
		if m < len(heaters) {
			mV = abs(heaters[m] - house)
		}
		min := min(min(lV, rV), mV)
		if min > maxDistance {
			maxDistance = min
		}
	}
	return maxDistance
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}
