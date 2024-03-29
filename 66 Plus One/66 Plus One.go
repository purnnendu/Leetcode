func plusOne(digits []int) []int {
    carry := 1

    for i := len(digits) - 1; i >= 0; i-- {
        digits[i], carry = (digits[i] + carry) % 10, (digits[i] + carry) / 10
    }

    if carry != 0 {
        return append([]int{carry}, digits...)
    }

    return digits
}
