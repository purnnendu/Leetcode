func isPalindrome(x int) bool {
    if x < 0 {
		return false
	}
	f := x
	result := 0
	for x != 0 {
		result = result*10 + x%10
		x = x / 10

	}

    return f == result
}
