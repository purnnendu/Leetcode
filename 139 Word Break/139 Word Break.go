func wordBreak(s string, wordDict []string) bool {
	dict := make(map[string]struct{}, len(wordDict))

	for _, w := range wordDict {
		dict[w] = struct{}{}
	}

	return wordBreakRec(s, dict, 0, map[int]bool{})
}

func wordBreakRec(s string, dict map[string]struct{}, start int, memo map[int]bool) bool {
	if start == len(s) {
		return true
	}
	if v, ok := memo[start]; ok {
		return v
	}
	for end := start+1; end <= len(s); end++ {
		if _, ok := dict[s[start:end]]; ok && wordBreakRec(s, dict, end, memo) {
			memo[start] = true
			return true
		}
	}
	memo[start] = false
	return false
}
