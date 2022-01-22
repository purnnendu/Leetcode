func isSubsequence(s string, t string) bool {
    idx := 0
	for i := range t {
		if idx > len(s)-1 {
			return true
		}

		if t[i] == s[idx] {
			idx++
		}
	}

    return idx > len(s)-1
}
