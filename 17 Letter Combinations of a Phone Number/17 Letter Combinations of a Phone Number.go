func letterCombinations(digits string) []string {
    var cache = map[int]string{
        2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz",
    }
    var ans = []string{}
    var getComb func(string, string)
    getComb = func(selected string, rest string){
        currentDigit, _ := strconv.Atoi(string(rest[0]))
        for _, ch := range cache[currentDigit] {
            if len(rest[1:]) == 0 {
                ans = append(ans, selected + string(ch))
            } else {
                getComb(selected+string(ch), rest[1:])
            }
        }
    }
    if len(digits)>0 {
        getComb("", digits)
    }
    return ans
}
