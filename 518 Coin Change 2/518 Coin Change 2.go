func change(amount int, coins []int) int {
    dp := make([]int, amount+1)
    dp[0] = 1
    //note here we use each coin once
    //this is to avoid 2,1 = 3 and 1, 2 = 3
    //we will only account for 1,1,1 = 3, and 1, 2 = 3
    //since coin 2 is used only once
    //also note that for the inner for loop
    //we start from small to large
    //this is to account for that we can use each coin multiple times
    //it is a little confusing here
    for _, coin := range coins {
        for i := coin; i <= amount; i++ {
            dp[i] += dp[i-coin]
        }
    }
    return dp[amount]
}
