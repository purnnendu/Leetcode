func calculate(s string) int {
    return betterEval(s)
}

func betterEval(s string) int {
    n := len(s)
    res, lastNumber, currentNumber := 0, 0, 0
    sign := byte('+')

    for i := 0; i < n; i++ {
        c := s[i]
        if c == ' ' {
            continue
        }
        if c >= '0' {
            currentNumber = currentNumber * 10 + int(c - '0')
            continue
        }

        if sign == '+' || sign == '-' {
            res += lastNumber
            if sign == '+' {
                lastNumber = currentNumber
            } else {
                lastNumber = -currentNumber
            }
        } else if sign == '*' {
            lastNumber *= currentNumber
        } else if sign == '/' {
            lastNumber /= currentNumber
        }
        sign = c
        currentNumber = 0
    }


    if sign == '+' || sign == '-' {
        res += lastNumber
        if sign == '+' {
            lastNumber = currentNumber
        } else {
            lastNumber = -currentNumber
        }
    } else if sign == '*' {
        lastNumber *= currentNumber
    } else if sign == '/' {
        lastNumber /= currentNumber
    }

    res += lastNumber

    return res
}

func evaluate(numbers []int, operators []byte) int {
    n := len(numbers)
    m := n - 1
    // evaluate * and /
    completed := 0
    for i := 0; i < m; i++ {
        operator := operators[i]
        //fmt.Println(string(operator))
        if operator == '*' {
            result := numbers[i] * numbers[i+1]
            numbers[i+1] = result
        } else if operator == '/' {
            result := numbers[i] / numbers[i+1]
            numbers[i+1] = result
        } else {
            result := numbers[i]
            for j := 1; j <= completed && i - j >= 0; j++ {
                numbers[i-j] = result
            }
            completed = 0
            continue
        }
        // mark operator as used
        operators[i] = '$'
        completed++
        //fmt.Println(numbers)
    }
    result := numbers[n-1]
    for j := 1; j <= completed && n - 1 - j >= 0; j++ {
        numbers[n-1-j] = result
    }
    // evaluate + and -
    for i := 0; i < m; i++ {
        operator := operators[i]

        //fmt.Println(string(operator))
        if operator == '+' {
            result := numbers[i] + numbers[i+1]
            numbers[i], numbers[i+1] = result, result
        } else if operator == '-' {
            result := numbers[i] - numbers[i+1]
            numbers[i], numbers[i+1] = result, result
        } else {
            // operator has been used; carry over value
            numbers[i+1] = numbers[i]
        }
        //fmt.Println(numbers)
    }
    return numbers[len(numbers)-1]
}

func getNumsAndOps(s string) ([]int, []byte) {
    n := len(s)
    num := 0

    numbers, operators := make([]int, 0, n), make([]byte, 0, n)

    for i := 0; i < n; i++ {
        char := s[i]
        if char < '0' {
            // operation
            operators = append(operators, char)
            numbers = append(numbers, num)
            num = 0
        } else {
            // digit
            num *= 10
            num += int(char - '0')
        }
    }

    if len(s) > 0 {
        numbers = append(numbers, num)
    }

    return numbers, operators
}

func doOperation(s string, operatorA, operatorB byte) string {
    n := len(s)
    lastOp := -1
    for i := 0; i < n; i++ {
        letter := s[i]
        if letter < '0' {
            lastOp = i
            continue
        }
        if letter == 'n' {
            continue
        }
        if letter != operatorA && letter != operatorB {

        }
        j := i + 1
        //fmt.Println("precheck", s[i])
        for j < n && s[j] >= '0' {
            //fmt.Println("incing")
            j++
        }
        //fmt.Println("found div op", lastOp, j, i, s)
        lDigits, rDigits := s[lastOp+1:i], s[i+1:j]
        s1, s2 := 1, 1
        if lDigits[0] == 'n' {
            s1 = -1
            lDigits = lDigits[1:]
        }
        if rDigits[0] == 'n' {
            s2 = -1
            rDigits = rDigits[1:]
        }
        d1, _ := strconv.Atoi(lDigits)
        d2, _ := strconv.Atoi(rDigits)

        d3:= 0
        if letter == operatorA {
            d3 = operation(d1 * s1, d2 * s2, operatorA)
        } else {
            d3 = operation(d1 * s1, d2 * s2, operatorB)
        }
        sign := ""
        if d3 < 0 {
            d3 *= -1
            sign = "n"
        }
        //fmt.Println("found op", d1, d2, d3, sign)
        s = doOperation(fmt.Sprintf("%s%s%v%s", s[:lastOp+1], sign, d3, s[j:]), operatorA, operatorB)
        break
        //fmt.Println(s[i])
    }
    return s
}

func operation(a, b int, operator byte) int {
    if operator == '*' {
        return a * b
    } else if operator == '/' {
        return a / b
    } else if operator == '+' {
        return a + b
    }
    return a - b
}

func trimInput(s string) string {
    n := len(s)
    res := ""
    for i := 0; i < n; i++ {
        if s[i] == ' ' {
            continue
        }
        res += string(s[i])
    }
    return res
}
