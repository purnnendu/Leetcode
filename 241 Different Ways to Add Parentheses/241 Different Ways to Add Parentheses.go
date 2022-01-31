func diffWaysToCompute(input string) []int {
    ret := make([]int, 0)

    for i:=0; i < len(input); i++ {
        if input[i] == '-' || input[i] == '*' || input[i] == '+' {
            part1 := input[0:i]
            part2 := input[i+1:]
            part1Ret := diffWaysToCompute(part1)
            part2Ret := diffWaysToCompute(part2)
            for _, p1 := range part1Ret {
                for _, p2 := range part2Ret {
                    c := 0
                    switch(input[i]) {
                        case '+':
                            c = p1 + p2
                        case '-':
                            c = p1 - p2
                        case '*':
                            c = p1 * p2
                    }
                    ret = append(ret, c)
                }
            }

        }

    }
    if len(ret) == 0 {
            x, _ := strconv.Atoi(input)
            ret = append(ret, x)
        }
        return ret
}
