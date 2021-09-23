import "sort"
func longestConsecutive(nums []int) int {
    result := 0
    streak := 1
    sort.Ints(nums)
    for i, e := range nums {

        if i == 0 {
            result = 1
        } else if nums[i-1] == e - 1 {
            streak += 1
        } else if nums[i -1] == e {
            continue
        } else {
            streak = 1
        }
        if streak > result {
            result = streak
        }
    }
    return result
}
