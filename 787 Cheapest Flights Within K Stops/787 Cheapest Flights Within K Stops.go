const MAX_INT = int(^uint(0) >> 1)
func findCheapestPrice(n int, flights [][]int, src int, dst int, K int) int {
    ret := MAX_INT
    graph := make([][][]int, n)
    for _, flight := range flights {
        graph[flight[0]] = append(graph[flight[0]], flight[1:])
    }
    DFS(src, 0, 0, graph, dst, K, &ret)
    if ret == MAX_INT { return -1 } else { return ret }
}


func DFS(root, dist, depth int, graph [][][]int, dst, K int, min *int) {
    if depth > K + 1 { return }
    if root == dst && dist < *min { *min = dist }
    for _, edge := range graph[root] {
        if temp := dist + edge[1]; temp < *min {
            DFS(edge[0], temp, depth+1, graph, dst, K, min)
        }
    }
}
