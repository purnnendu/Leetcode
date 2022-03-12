func pushDominoes(dominoes string) string {
    var i, tmp int
    b, leftIndex := []byte(dominoes), 0
    for i = 1; i < len(b); i++ {
        switch b[i] {
            case 'L':
                if b[leftIndex] == 'R' {
                    tmp = leftIndex + i
                    set(b[leftIndex:tmp/2], 'R')
                    set(b[tmp/2+1:i], 'L')
                    if tmp & 1 == 1 {
                        b[tmp/2] = 'R'
                    }
                } else if leftIndex < i {
                    set(b[leftIndex:i], 'L')
                }

            case 'R':
                if b[leftIndex] == 'R' && leftIndex+1 < i {
                    set(b[leftIndex+1:i], 'R')
                }

            case '.':
                continue
        }

        leftIndex = i
    }

    if b[leftIndex] == 'R' {
        set(b[leftIndex:], 'R')
    }

    return string(b)
}

func set(b []byte, direction byte) {
    for i := 0; i < len(b); i++ {
        b[i] = direction
    }
}
