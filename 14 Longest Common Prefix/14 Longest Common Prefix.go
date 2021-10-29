func longestCommonPrefix(strs []string) string {
    prefix := ""
	j := 0
	if len(strs) == 0 {
		return ""
	}
	if len(strs) == 1 {
		return strs[0]
	}
	for {
		tmp := make(map[string]int)
		for _, element := range strs {
			word := element
			if j > len(word) || len(word) == 0 {
				return prefix
			} else {
				if j == len(word) {
					tmp[word[j:]] +=1
				} else{
					tmp[word[j:j+1]] += 1
				}

				if len(tmp) > 1 {
					return prefix
				}
			}
		}
		if len(tmp) != 1 {
			return prefix
		} else {
			for k := range tmp {
				prefix = prefix + k
			}
		}
		j += 1
	}

}
