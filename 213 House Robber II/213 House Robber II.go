func max(m, n int) int {
	if m > n {
		return m
	}
	return n
}
func rob_helper(nums []int) int {
	l := len(nums)
	var houses = make([]int, l)
	houses[0] = nums[0]
	houses[1] = max(nums[0], nums[1])
	for i := 2; i < l; i++ {
		houses[i] = max(nums[i]+houses[i-2], houses[i-1])
	}
	return houses[l-1]
}
func rob(nums []int) int {
	switch l := len(nums); l {
	case 0:
		return 0
	case 1:
		return nums[0]
	case 2:
		return max(nums[0], nums[1])
	default:

		return max(rob_helper(nums[:l-1]), rob_helper(nums[1:]))
	}
}
