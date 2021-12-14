func wiggleSort(nums []int)  {    
    wiggle(nums)
}

func wiggle(nums []int) {
    n := len(nums)

    sort.Slice(nums, func(i, j int) bool {
        return nums[i] < nums[j]
    })

    i, j, k := 0, 0, n - 1
    median := nums[n/2]

    for j <= k {
        nj, aj := A(nums, j)
        if nj > median {
            _, ai := A(nums, i)
            nums[ai], nums[aj] = nums[aj], nums[ai]
            i++
            j++
        } else if nj < median {
            _, ak := A(nums, k)
            nums[aj], nums[ak] = nums[ak], nums[aj]
            k--
        } else {
            j++
        }
    }
}

func A(nums[]int, i int) (int, int) {
    idx := (1 + 2*i) % (len(nums) | 1)
    return nums[idx], idx
}
