func findAnagrams(s string, p string) []int {
    if len(s) < len(p) {
		return nil
	}
	var pat, mem [26]int
	// filling hashmaps
	for i := range p {
		pat[p[i]-'a']++
		mem[s[i]-'a']++
	}
	var out []int
	for i := 0; i < len(s)-len(p)+1; i++ {
		if pat == mem {
			out = append(out, i)
		}
		// sliding window, no need to change at last iteration
		if i+len(p) < len(s) {
			mem[s[i]-'a']--
			mem[s[i+len(p)]-'a']++
		}
	}
    return out
}
