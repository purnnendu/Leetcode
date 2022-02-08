func wiggleMaxLength(a []int) int {

  // dp[i][0]: 0...i answer for i
    n := len(a)

  up, down := 1, 1
  for i:=1; i<n; i++ {
    if a[i-1] < a[i] {
     up = down+1
    } else if a[i] < a[i-1] {
      down = up+1
    } else {
    }
  }
  // fmt.Println(dp)
  return max(up, down)
}


func ans_n2(a []int) int {
    n := len(a)
  dp := make([][]int, n)

  //base case
  dp[0] = []int{1, 1}

  ans := 1
  for i:=1; i<n; i++ {
    dp[i] = make([]int, 2)
    for j:=0; j<i; j++ {

      if a[i] > a[j] {
        dp[i][0] = max(dp[i][0], dp[j][1]+1)
      } else if a[i] < a[j]{
        dp[i][1] = max(dp[i][1], dp[j][0]+1)
      }
    }
    ans = max(ans, max(dp[i][0], dp[i][1]))
  }
  return ans
}

func max(x, y int) int {
  if x < y {return y}
  return x
}
