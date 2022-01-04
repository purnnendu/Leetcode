func convert(s string, numRows int) string {
    if len(s) < 2 || numRows == 1 {
        return s
    }
    res := make([]byte, 0, len(s))
    numRows = min(len(s), numRows)
    for row := 1; row <= numRows; row++ {
        skipBefore, skipAfter := (row-1)*2, (numRows-row)*2
        idx := row-1
        res = append(res, s[idx])
        for {
            if skipAfter > 0 {
                idx += skipAfter
                if idx >= len(s) {
                    break
                }
                res = append(res, s[idx])
            }
            if skipBefore > 0 {
                idx += skipBefore
                if idx >= len(s) {
                    break
                }
                res = append(res, s[idx])
            }
        }
    }
    return string(res)
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
