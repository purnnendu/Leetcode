func intersect(nums1 []int, nums2 []int) []int {
    res := make([]int, 0)
	min, max := nums1, nums2
	if len(nums1) > len(nums2) {
		min, max = nums2, nums1
	}
	count := make(map[int]int)
	for i := 0; i < len(min); i++ {
		count[min[i]]++
	}
	for k := 0; k < len(max); k++ {
		_, ok := count[max[k]]
		if ok {
			res = append(res, max[k])
			if count[max[k]]-1 == 0 {
				delete(count, max[k])
			} else {
				count[max[k]]--
			}
		}
		if len(count) == 0 {
			return res
		}
	}
    return res
}
