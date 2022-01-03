type Vertex struct {
    r int
    c int
}

func orangesRotting(grid [][]int) int {
    row, col := len(grid), len(grid[0])
    iter := [][]int{[]int{0,-1},[]int{0,1},[]int{1,0},[]int{-1,0}}
    q := []Vertex{}

    for i, rows := range grid {
        for j, col := range rows {
            if col == 2 {
                q = append(q, Vertex{i, j})
            }
        }
    }

    min := 0

    for len(q) > 0 {
        min++
        l := len(q)
        for i := 0; i < l; i++ {
            n := q[0]
            q = q[1:]
            for _, cor := range iter {
                x, y := n.r+cor[0], n.c+cor[1]
                if x >= 0 && x < row &&
                    y >=0 && y < col &&
                    grid[x][y] == 1 {
                    grid[x][y] = 2
                    q = append(q, Vertex{x, y})
                }
            }
        }
        if len(q) == 0 {
            min--
        }
    }

    for _, rows := range grid {
        for _, col := range rows {
            if col == 1 {
                return -1
            }
        }
    }

    return min
}
