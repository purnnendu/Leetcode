func minDifference(nums []int) int {
    mins := make([]int,4)
	maxs := make([]int,4)

    size := len(nums)
    if size <= 4 {
        return 0
    }

    mins[0] = nums[0]
    maxs[0] = nums[0]
    mincount := 1
    maxcount := 1

    for i := 1; i < size; i++ {
        if (nums[i] < mins[mincount-1] || mincount < 4) {
            mincount = ins(mins, nums[i], mincount)
        }

        if nums[i] > maxs[maxcount-1] || maxcount < 4 {
            maxcount = maxins(maxs, nums[i], maxcount)
        }
    }

    return diff(mins, maxs)
}

func ins(list []int, num int, count int) int {
    for i := 0; i < count; i++ {
        if num < list[i] {
            tmp := list[i]
            list[i] = num
            num = tmp
        }
    }
    if  count != 4 {
        list[count] = num
        count++
    }
    return count
}

func maxins(list []int, num int, count int) int {
    for i := 0; i < count; i++ {
        if num > list[i] {
            tmp := list[i]
            list[i] = num
            num = tmp
        }
    }
    if  count != 4 {
        list[count] = num
        count++
    }
    return count
}

func diff(mins []int, maxs[]int) int {
    minapl := 10000000000
    for i := 0; i < 4; i++ {
        if minapl > (maxs[3-i] - mins[i]) {
            minapl = maxs[3-i] - mins[i]
        }
    }
    return minapl
}
