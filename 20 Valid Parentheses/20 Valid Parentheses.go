func isValid(s string) bool {
    if s == "" {
        return true
    }

    tr := map[rune]rune{
        '}': '{',
        ')': '(',
        ']': '[',
    }

    stack := make([]rune, 0, 1)

    for _, ch := range s {
        switch ch {
        case 40,123,91:
            stack = append(stack, ch)
        case 41,125,93:
            if len(stack) == 0 || stack[len(stack)-1] != tr[ch] {
                return false
            } else {
                stack = stack[:len(stack)-1]
            }
        }
    }

    return len(stack) == 0
}
