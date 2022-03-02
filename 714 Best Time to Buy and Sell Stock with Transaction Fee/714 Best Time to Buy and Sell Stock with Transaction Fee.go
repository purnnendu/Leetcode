func maxProfit(prices []int, fee int) int {
    cash, hold := 0, -prices[0]

    for i:=1;i<len(prices);i++{
        cash = myMax(cash, hold+ prices[i]-fee)
        hold = myMax(hold, cash - prices[i])
    }


    return cash
}

func myMax(a, b int) int {
    if a > b {
        return a
    }

    return b
}
