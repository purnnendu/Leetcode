func mySqrt(x int) int {
    left := 1
    right :=x
    point := 0
    for left<=right {
        point = left+(right-left)/2
        if point*point == x{
            return point
        } else if point*point > x {
            right = point - 1
        } else {
            left = point +1
        }

    }
    if point*point > x{
        return point-1
    }
    return point
}
