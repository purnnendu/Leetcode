func romanToInt(s string) int {
    n := len(s)
    if n < 1 {
        return 0
    }
    table := map[rune]int{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    val := 0
    for i := 0; i < n - 1; i++ {
        a := rune(s[i])
        b := rune(s[i + 1])
        if table[a] < table[b] {
            val -= table[a]
        } else {
            val += table[a]
        }
    }
    return val + table[rune(s[n - 1])]
}
