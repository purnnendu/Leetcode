import "sort"

func combinationSum(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    res := [][]int{}
    tmp := []int{}
    var dfs func(int, int)
    dfs = func(curTotal int, ind int) {
        if curTotal == target {
            copied := make([]int, len(tmp))
            copy(copied, tmp)
            res = append(res, copied)
            return
        }
        if ind == len(candidates) {
            return
        }
        for i := ind; i < len(candidates); i++ {
            if i > ind && candidates[i] == candidates[i-1] {
                continue
            }
            if curTotal + candidates[i] > target {
                break
            }
            tmp = append(tmp, candidates[i])
            dfs(curTotal + candidates[i], i)
            tmp = tmp[0:len(tmp)-1]
        }
    }
    dfs(0, 0)
    return res
}
