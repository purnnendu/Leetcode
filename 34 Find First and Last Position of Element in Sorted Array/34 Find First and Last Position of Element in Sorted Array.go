func searchRange(nums []int, target int) []int {
    start := find(nums, target, true)
    if start == -1 {
        return []int{-1, -1}
    }
    end := find(nums, target, false)
    return []int{start, end}
}

func find(nums []int, target int, start bool) int {
    n := len(nums)
    left, right := 0, n-1
    res := -1
    for left <= right {
        mid := left + (right - left) / 2
        if nums[mid] < target {
            left = mid+1
        } else if nums[mid] > target {
            right = mid-1
        } else {
            res = mid
            if start {
                right = mid-1
            } else {
                left = mid+1
            }
        }
    }
    return res
}
