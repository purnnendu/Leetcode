func nextPermutation(nums []int)  {

  l:=len(nums)

    var i,index int
    for i=l-1;i>0;i--{
        if nums[i]>nums[i-1]{

            var j int
            for j=i;j<l;j++{
                if nums[j]<=nums[i-1]{
                    break
                }
            }
            j--
            index = i
            nums[j],nums[i-1]=nums[i-1],nums[j]

            break
        }
    }


    i,j:=index,l-1
        for i<j{
            nums[i],nums[j]=nums[j],nums[i]
            i++

            j--
        }

    return

}
