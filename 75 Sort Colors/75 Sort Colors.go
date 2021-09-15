func sortColors(nums []int)  {
    low := -1
    mid := -1
    high := len(nums)
    for mid + 1 < high {
        if nums[mid+1] == 2 {
		    nums[mid+1], nums[high-1] = nums[high-1], nums[mid+1]
            high--
	    } else if nums[mid+1] == 1 {
		    mid++
	    } else {
		    nums[mid+1], nums[low+1] = nums[low+1], nums[mid+1]
            low++
            mid++
	    }
    }
}
