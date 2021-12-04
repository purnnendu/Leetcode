func partition(s string) [][]string {
    m := isPalindrome(s)
    return backTracking(s, 0, m, []string{}, [][]string{})
}

func backTracking(s string, index int, m [][]bool, cur []string, ans [][]string) [][]string{
    if index >= len(s) {
        cloned := make([]string, len(cur))
        copy(cloned, cur)
        ans = append(ans, cloned)
        return ans
    }
    for j := index+1; j <= len(s); j ++{
        if m[index][j-1] {
            cur = append(cur, s[index:j])
            ans = backTracking(s, j, m, cur, ans)
            cur = cur[:len(cur)-1]
        }
    }
    return ans
}

func isPalindrome(s string) [][]bool{
    dp := make([][]bool, len(s))
    for i := range dp{
        dp[i] = make([]bool, len(s))
    }
    for i := 0; i < len(s); i ++{
        dp[i][i] = true
    }
    for i := 0; i +1 < len(s); i ++{
        dp[i][i+1] = (s[i] == s[i+1])
    }
    for l := 3; l <= len(s); l ++{
        for i:= 0; i + l <= len(s); i ++{
            j := i+l-1
            if s[i] == s[j]{
                dp[i][j] = dp[i+1][j-1]
            }else{
                dp[i][j] = false
            }
        }
    }
    return dp
}
