import "fmt"

func fractionToDecimal(numerator int, denominator int) string {

    if numerator == 0 {
        return "0"
    }
    if numerator == denominator {
        return "1"
    }

    sign := 1

    if numerator < 0 {
        numerator *= -1
        sign *= -1
    }

    if denominator < 0 {
        denominator *= -1
        sign *= -1
    }

    s := ""
    if sign < 0 {
        s += "-"
    }

    a := numerator/denominator
    s += fmt.Sprintf("%d", a)

    rem := numerator % denominator
    if rem > 0 {
        s += "."
    }

    index := len(s)
    ok := false
    m := make(map[int]int)

    for rem != 0 {

        index, ok = m[rem]
        if !ok {
            m[rem] = len(s)
        } else {
            s = s[0:index] + "(" + s[index:] + ")"
            break
        }

        rem *= 10

        a = rem/denominator
        rem = rem % denominator
        s += fmt.Sprintf("%d", a)
    }

    return s
}
