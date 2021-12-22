func maxv(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func search(obj []byte, k int) int {
    freq := make(map[byte]int)
    for _, c := range obj {
        freq[c]++
    }
    res, i := 0, 0
    for i < len(obj) {
        if freq[obj[i]] < k {
            i++
            continue
        }
        j := i
        for j < len(obj) && freq[obj[j]] >= k {
            j++
        }
        if j - i == len(obj) {
            return j - i
        }
        res = maxv(res, search(obj[i:j], k))
        i = j
    }
    return res
}

func longestSubstring(s string, k int) int {
    bytes := []byte(s)
    return search(bytes, k)
}
