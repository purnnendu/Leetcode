func spiralOrder(matrix [][]int) []int {
    rStart := 0
    rEnd := len(matrix) - 1
    cStart := 0
    cEnd := len(matrix[0]) - 1
    var result []int
    for rStart <= rEnd && cStart <= cEnd {
        // Traverse Right
        for j:= cStart; j <= cEnd; j++{
            result = append(result,matrix[rStart][j])
        }
        rStart++
        // Traverse Down
        for i:= rStart; i <= rEnd; i++{
            result = append(result,matrix[i][cEnd])
        }
        cEnd--
        //break the loop
        if rStart > rEnd || cStart > cEnd {
            break
        }
        // Traverse Left
        for j:= cEnd; j >= cStart; j--{
        result = append(result,matrix[rEnd][j])
        }
        rEnd--
         // Traverse Up
        for i:= rEnd; i >= rStart; i--{
        result = append(result,matrix[i][cStart])
        }
        cStart++
    }
    return result
}
