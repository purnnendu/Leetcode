func findLength(nums1 []int, nums2 []int) int {
	maxLength := 0
	dp := make([]int, len(nums2))

	for i := len(nums1) - 1; i >= 0; i-- {
		prev := 0
		for j := len(nums2) - 1; j >= 0; j-- {
			if nums1[i] == nums2[j] {
				prev, dp[j] = dp[j], 1+prev
                if dp[j] > maxLength {
                    maxLength = dp[j]
                }
				//maxLength = max(maxLength, dp[j])
			} else {
				prev, dp[j] = dp[j], 0
			}
		}
	}
	return maxLength
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}
