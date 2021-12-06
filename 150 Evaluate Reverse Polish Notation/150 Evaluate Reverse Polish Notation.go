var ops map[string]func(a, b int) int = map[string]func(a, b int) int{
	"+": func(a, b int) int { return a + b },
	"-": func(a, b int) int { return a - b },
	"*": func(a, b int) int { return a * b },
	"/": func(a, b int) int { return a / b },
}

func evalRPN(tokens []string) int {
	stk := make([]int, 0, len(tokens))
	for _, s := range tokens {
		if f, ok := ops[s]; ok {
			a := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			b := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			stk = append(stk, f(b, a))
		} else {
			n, _ := strconv.Atoi(s)
			stk = append(stk, n)
		}
	}
	return stk[len(stk)-1]
}
