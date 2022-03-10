func largestSumOfAverages(nums []int, k int) float64 {
    arr:=make([]float64,len(nums))
    curSum:=float64(0.0)
    p:=make([]float64,len(nums))
    for i:=0;i<len(nums);i++{
        curSum+=float64(nums[i])
        arr[i]=curSum/float64(i+1)
        p[i]=curSum
    }
    for loop:=1;loop<k;loop++{
        for i:=len(nums)-1;i>=loop;i--{
            max:=float64(0.0)
            for j:=i-1;j>=loop-1;j--{
                v:=(p[i]-p[j])/float64(i-j)+arr[j]
                if v>max{
                    max=v
                }
            }
            arr[i]=max
        }
    }
    return arr[len(arr)-1]
}
