func singleNumber(nums []int) int {
    var x int = 0
    for _,v:=range nums{
        x ^= v
    }
    return x
}
