func subsets(nums []int) [][]int {
    res := [][]int{}
    temp := []int{}
    dfs(nums, 0, &temp, &res)
    return res
}

func dfs(nums []int, idx int, temp *[]int, res *[][]int) {
    if idx == len(nums) {
        cur := make([]int, len(*temp))
        copy(cur, *temp)
        *res = append(*res, cur)
        return
    }

    dfs(nums, idx+1, temp, res)
    *temp = append(*temp, nums[idx])
    dfs(nums, idx+1, temp, res)
    *temp = (*temp)[0:len(*temp)-1]
}
