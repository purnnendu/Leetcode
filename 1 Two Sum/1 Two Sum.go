func twoSum(nums []int, target int) []int {
    seenNums := make(map[int]int)
	for index, thisNum := range nums {
		if seenIndex, ok := seenNums[target - thisNum]; ok {
			return []int{seenIndex, index}
		}
		seenNums[thisNum] = index
	}
    return []int{0, 0}
}
