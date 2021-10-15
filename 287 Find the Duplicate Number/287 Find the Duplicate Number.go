func findDuplicate(nums []int) int {
    i := 0
    for i < len(nums) {
        j := nums[i] - 1
        if nums[i] != nums[j] {
            nums[i], nums[j] = nums[j], nums[i]
        } else {
            i++
        }
    }

    for x := 0; x < len(nums); x++ {
        if nums[x] != x + 1 {
            return nums[x]
        }
    }
    return -1
}
