func missingNumber(nums []int) int {
    ans := len(nums)
	for i, v := range nums {
		ans = ans ^ i ^ v
	}
    return ans
}
