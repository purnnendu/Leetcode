func reverseWords(words string) string {
	splitted := strings.Split(words, " ")

	for i, word := range splitted {
		tmp := []byte(word)
		reverseString(tmp)
		splitted[i] = string(tmp)
	}

	words = strings.Join(splitted, " ")

	return words
}

func reverseString(s []byte) {
	for l, r := 0, len(s)-1; l < r; l, r = l+1, r-1 {
		s[l], s[r] = s[r], s[l]
	}
}
