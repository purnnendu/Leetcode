func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    sol := [][]int{}
    for i := 0; i < len(nums)-2; i++ {
        if i > 0 && nums[i] == nums[i-1] {
            continue
        }
        j, k := i+1, len(nums)-1
        for j < k {
            sum := nums[i] + nums[j] + nums[k]
            if sum == 0 {
                sol = append(sol, []int{nums[i], nums[j], nums[k]})
                j, k = j+1, k-1
                for j < k && nums[j] == nums[j-1] {
                    j++
                }
                for j < k && nums[k] == nums[k+1] {
                    k--
                }
            } else if sum < 0 {
                j++
            } else {
                k--
            }
        }
    }
    return sol
}
