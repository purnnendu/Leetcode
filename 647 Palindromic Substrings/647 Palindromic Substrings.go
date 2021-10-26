func countSubstrings(s string) int {
    var ans int
    for i:=0; i<len(s); i++ {
        ans++ // count for each single substring
        for d:=0; d<=1; d++ { // check odd and even length of palindromic substring
            low, high := i-d, i+1
            for low >=0 && high<len(s) && s[low]==s[high] {
                ans++
                low--
                high++
            }
        }
    }

    return ans
}
