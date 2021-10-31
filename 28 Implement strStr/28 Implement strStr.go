func strStr(haystack string, needle string) int {
    if len(needle) == 0 {
        return 0
    }

    for i := 0; i + len(needle) - 1 < len(haystack); i++ {
        if haystack[i] == needle[0] && haystack[i + len(needle) - 1] == needle[len(needle) - 1] {
            for j := 0; j < len(needle); j++ {
                if (needle[j] != haystack[i + j]) {
                    break
                } else if j == len(needle) - 1 {
                    return i
                }
            }
        }
    }

    return -1
}
