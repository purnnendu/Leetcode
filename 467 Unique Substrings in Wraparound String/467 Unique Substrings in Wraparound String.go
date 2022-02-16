func findSubstringInWraproundString(p string) int {
    if len(p) == 0 {
        return 0
    }
    pre := 1
    res := 0
    maxLen := make([]int, 26) //use maxLen slice to maintain the max len of substring of each letter
    maxLen[p[0] - 'a'] = 1

    for i := 1; i < len(p); i++ {
        if p[i] - p[i - 1] == 1 || p[i - 1] - p[i] == 25 {
            pre++ //if current letter is at alphabet sequence of previous letter, increase 1 to the max len
        } else {
            pre = 1 //otherwise the max len is 1
        }
        maxLen[p[i] - 'a'] = max(maxLen[p[i] - 'a'], pre) //update the maxLen of this letter
    }
    for _, v := range maxLen {
        res += v //sum up the max len of each letters
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
