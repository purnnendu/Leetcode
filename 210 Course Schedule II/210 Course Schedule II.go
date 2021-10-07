func findOrder(numCourses int, prerequisites [][]int) []int {
    prev := make([]int, numCourses)
    next := make([][]int, numCourses)
    for _, p := range prerequisites {
        prev[p[0]] ++
        next[p[1]] = append(next[p[1]], p[0])
    }

    var q []int
    for i := 0; i < numCourses; i ++ {
        if prev[i] == 0 {
            q = append(q, i)
        }
    }
    res := make([]int, 0, numCourses)
    for len(q) > 0 {
        course := q[0]
        q = q[1:]
        res = append(res, course)
        for _, n := range next[course] {
            prev[n] --
            if prev[n] == 0 {
                q = append(q, n)
            }
        }
    }
    if len(res) != numCourses {
        return nil
    }
    return res
}
