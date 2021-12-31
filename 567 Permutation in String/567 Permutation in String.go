func equals(arr1, arr2 []int) bool {
    for index, _ := range arr1 {
        if arr1[index] != arr2[index] {
            return false
        }
    }
    return true
}
func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2) {
        return false
    } 
    countArray1, countArray2 := make([]int, 26), make([]int, 26)
    for _, val := range s1 {
        countArray1[int(val-'a')] += 1
    }
    k := 0
    for k<len(s1) {
        countArray2[int(s2[k] - 'a')] += 1
        k += 1
    }
    if equals(countArray1, countArray2) {
        return true
    }
    for k<len(s2) {
        countArray2[int(s2[k-len(s1)] - 'a')] -= 1
        countArray2[int(s2[k]-'a')] += 1
        if equals(countArray1, countArray2) {
            return true
        }
        k += 1
    }
    return false
}
