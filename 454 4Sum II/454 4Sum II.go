func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
    m := make(map[int]int, len(nums1)*len(nums2))
    for _, v := range nums1{
        for _, v2 := range nums2{
            m[v+v2] ++
        }
    }

    res := 0
    for _, v3 := range nums3{
        for _, v4 := range nums4{
            res += m[0-v3-v4]
        }
    }
    return res


}
