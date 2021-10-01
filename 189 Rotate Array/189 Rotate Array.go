func rotate(nums []int, k int)  {
    l := len(nums)
	step := k % l
	if step == 0 {
		return
	}
	tmp := append(nums[l-step:], nums[0:(l-step)]...)
	for i := range nums {
		nums[i] = tmp[i]
    }

}
