func maxProduct(nums []int) int {
    minval := nums[0]
    maxval := nums[0]
    maxproduct := nums[0]
    for i := 1; i<len(nums); i++{
        if nums[i] < 0{
            minval, maxval = maxval, minval
        }
        minval = int(math.Min(float64(nums[i]),float64(minval*nums[i])))
        maxval = int(math.Max(float64(nums[i]),float64(maxval*nums[i])))
        if maxval > maxproduct{
            maxproduct = maxval
        }
    }
    return maxproduct
}
