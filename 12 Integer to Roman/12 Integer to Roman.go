func intToRoman(num int) string {
    result := []byte{}

    lookup := map[int]byte{
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    dec := []int{1000,100,10,1}

    for _,v := range dec {
        quantity := num/v
        num = num - quantity*v

        if quantity < 4 {
            for j:=0; j < quantity; j++ {
                result = append(result, lookup[v])
            }
            continue
        }
        if quantity == 4 {
            result = append(result, lookup[v])
            result = append(result, lookup[5*v])
            continue
        }
        if quantity == 5 {
            result = append(result, lookup[5*v])
            continue
        }
        if quantity > 5 {
            if quantity == 9 {
                result = append(result, lookup[v])
                result = append(result, lookup[10*v])
                continue

            } else {
                result = append(result, lookup[5*v])
                for j := 0; j < quantity -5; j++ {
                    result = append(result, lookup[v])
                }
                continue
            }
        }

    }
    return string(result)
}
