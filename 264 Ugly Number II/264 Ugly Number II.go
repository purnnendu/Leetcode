func nthUglyNumber(n int) int {
    if n == 1 {
        return 1
    }
    u := make([]int, n)
    u[0] = 1
    i2, i3, i5 := 0, 0, 0
    two, three, five := 2, 3, 5
    for i := 1; i < n; i++ {

        if three == two {
            i3++
            three = 3*u[i3]
        }
        if five == two {
            i5++
            five = 5*u[i5]
        }
        if five == three {
            i5++
            five = 5*u[i5]
        }
        if two < three && two < five {
            u[i] = two
            i2++
            two = 2*u[i2]
        } else if three < two && three < five {
            u[i] = three
            i3++
            three = 3 * u[i3]
        } else {
            u[i] = five
            i5++
            five = 5 * u[i5]
        }
    }
    return u[n-1]
}
