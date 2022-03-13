func longestMountain(A []int) int {
	if len(A) < 3 {
		return 0
	}
	last := A[0]
	longest, current := 0, 1
	up := true // mark for up or down
	for i := 1; i < len(A); i++ {
		if A[i] == last {
			if up == false {
				// if down, it's a valid mountain
				longest = max(longest, current)
			}
			current = 1
			up = true
		} else if A[i] > last {
			if up == true {
				current++
			} else {
				longest = max(longest, current)
				current = 2
				up = true
			}
		} else {
			if up == false {
				current++
			} else {
				if current >= 2 {
					up = false
                    current++
				} else {
					current = 1
				}
			}
		}
		last = A[i]
	}
	if up == false {
		longest = max(longest, current)
	}
	if longest < 3 {
		return 0
	}
	return longest
}

func max(values ...int) int {
	maxValue := math.MinInt32
	for _, v := range values {
		if v > maxValue {
			maxValue = v
		}
	}
	return maxValue
}
