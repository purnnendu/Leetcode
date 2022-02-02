func maxProfit(prices []int) int {
  len := len(prices)
  k := make([]int, 3)     //0 buy, 1sell, 2 cool
  if len <= 1 {
    return 0
  }
  k[0] = -prices[0]
  for i:= 1;i<len ;i++ {
    k[0], k[1], k[2] = max(k[0], k[2]-prices[i]),max(k[1], k[0] + prices[i]), k[1]
  }

  return max(max(k[0], k[1]), k[2])
}

func max(a,b int) int {
  if a>b {
    return a
  }
  return b
}
