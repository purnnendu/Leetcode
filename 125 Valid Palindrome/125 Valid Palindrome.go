func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    for i, j:= 0, len(s) - 1; i <= j; {
        if !isAlphaNum(s[i]) {
            i++
            continue
        }
        if !isAlphaNum(s[j]) {
            j--
            continue
        }

        if s[i] != s[j] {
            return false
        }

        i++
        j--
    }

    return true
}

func isAlphaNum(a byte) bool {
    if (a <= 'z' && a >= 'a') || (a >= 'A' && a <= 'Z') || (a >= '0' && a <= '9'){
        return true
    }

    return false
}
