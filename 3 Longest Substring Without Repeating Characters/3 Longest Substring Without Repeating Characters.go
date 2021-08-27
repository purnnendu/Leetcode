func isSafe(s []byte, b byte) (bool, int) {
	if len(s) == 0 {
		return true, -1
	}

	for i, v := range s {
		if b == v {
			return false, i
		}
	}

	return true, -1
}

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}

	max := 0
	current_max := max
	sub := []byte{}
	current_sub := []byte{}

	for i := 0; i < len(s); i++ {
		// fmt.Printf("\ncurrent_sub:%v\n", string(current_sub))

		if safe, j := isSafe(current_sub, s[i]); safe {
			// fmt.Printf("safe: %v, j: %v, max: %v, current_max: %v\n", safe, j, max, current_max)
			current_max += 1
			// fmt.Println("change current_max to: ", current_max)
			current_sub = append(current_sub, s[i])
		} else {
			// fmt.Printf("safe: %v, j: %v,  max: %v, current_max: %v\n", safe, j, max, current_max)
			current_sub = current_sub[j+1:]
			current_sub = append(current_sub, s[i])
            current_max = len(current_sub)
		}

		if current_max > max {
			// fmt.Printf("current_max: %v, max: %v, current_max > max:, update max to: %v\n", current_max, max, current_max)
			max = current_max
			sub = append([]byte{}, current_sub...)
		}

	}

	return len(sub)
}
