type Stack []byte

func (s *Stack) Push(b byte) {
    *s = append(*s, b)
}

func (s *Stack) Pop() byte {
    slice := []byte(*s)
    b := slice[len(slice)-1]

    *s = slice[:len(slice)-1]

    return b
}

func (s *Stack) Len() int {
    return len(*s)
}

func (s *Stack) String() string {
    return string(*s)
}

func letterCasePermutation(s string) []string {
    maxLen := len(s)
    stack := &Stack{}

    result := make([]string, 0, 1)

    var generate func(i int)
    generate = func(i int) {
        if i == maxLen {
            result = append(result, stack.String())
            return
        }

        letter := s[i]

        stack.Push(letter)
        generate(i+1)
        stack.Pop()

        if isDigit(letter) {
            return
        }

        lower := toLower(letter)
        if letter == lower {
            stack.Push(toUpper(letter))
        } else {
            stack.Push(lower)
        }

        generate(i+1)
        stack.Pop()
    }

    generate(0)

    return result
}

func isDigit(b byte) bool {
    return b >= '0' && b <= '9'
}

func toLower(b byte) byte {
    if b >= 'a' && b <= 'z' {
        return b
    }

    return b+32
}

func toUpper(b byte) byte {
    if b >= 'A' && b <= 'Z' {
        return b
    }

    return b-32
}
