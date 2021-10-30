func removeDuplicates(nums []int) int {
    length := len(nums)
    if length <=1 {
        return length
    }

    index := 1

    for i:=1; i < length; i++ {
        if nums[i] == nums[i-1]{
            continue
        } else {
            nums[index] = nums[i]
            index++
        }
    }
    return index
}
